from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from . import serializers
from .models import Submission, Document
from .constants import *
from .tasks import process_documents

# Set max file size in requests, current 20MB
MAX_FILE_SIZE = 20*1024*1024

# Set max files in a request
MAX_FILES_PER_REQUEST = 50


class SubmissionList(APIView):
    serializer_class = serializers.SubmissionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        # TODO: Do not create save the submission to the DB unless all conditions are passing

        # create new submission
        submission = Submission.objects.create(
            status=Submission.SubmissionStatus.PENDING
        )

        # check for request content type
        is_file = CONTENT_TYPE_FILE in request.content_type
        is_text = CONTENT_TYPE_TEXT in request.content_type

        if not (is_file or is_text):
            return Response(
                {"error": "Unsupported Content-Type header"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if is_file:
            files = request.FILES.getlist("files")

            if len(files) > MAX_FILES_PER_REQUEST:
                 return Response(
                     {"error": "More than max allowed files per request"}, status=status.HTTP_400_BAD_REQUEST
                 )

            if not files:
                return Response(
                    {"error": "No files present"}, status=status.HTTP_400_BAD_REQUEST
                )

            for file in files:
                if file.size < MAX_FILE_SIZE:
                    Document.objects.create(
                        file=file,
                        name=file.name,
                        submission=submission,
                        type=Document.DocumentType.FILE,
                        )
                else:
                    return Response(
                        {"error": "File size limit breached"}, status=status.HTTP_400_BAD_REQUEST
                     )

        else:
            text_raw = request.body.decode()

            if not text_raw.strip():
                return Response(
                    {"error": "No text was specified"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            Document.objects.create(
                submission=submission,
                type=Document.DocumentType.TEXT,
                text_raw=text_raw,
            )

        # Run background task that processes documents
        process_documents.delay(submission.id)

        return Response(
            self.serializer_class(submission).data, status=status.HTTP_201_CREATED
        )


class SubmissionDetail(APIView):
    serializer_class = serializers.SubmissionSerializer

    def get(self, request, id):
        submission = get_object_or_404(Submission, pk=id)

        data = {
            **self.serializer_class(instance=submission).data,
        }

        # in case the submission is processed, include the documents
        if submission.status == Submission.SubmissionStatus.PROCESSED:
            data["documents"] = serializers.DocumentDetailedSerializer(
                submission.documents.all(), many=True
            ).data

        return Response(data=data)


class DocumentDetail(APIView):
    serializer_class = serializers.DocumentResultSerializer

    def get(self, request, id):
        document = get_object_or_404(Document, pk=id)

        if document.submission.status == Submission.SubmissionStatus.PROCESSED:
            return Response(
                {
                    "document": self.serializer_class(instance=document).data,
                    "submission_id": document.submission.id,
                    "is_multiple": document.submission.documents.count() > 1,
                }
            )
        else:
            # unprocessed submission documents should 'not exist' for the user
            return Response(status=status.HTTP_404_NOT_FOUND)
