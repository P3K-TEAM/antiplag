from django.shortcuts import render
from .models import Paper
from .serializers import PaperSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView


def index(request):
    return render(request, 'home.html')

class file_list(APIView):
    def get(self, request, format=None):
        papers = Paper.objects.all()
        serializer = PaperSerializer(papers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class file_detail(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = PaperSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Paper.objects.get(pk=pk)
        except Paper.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paper = self.get_object(pk)
        serializer = PaperSerializer(paper)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        paper = self.get_object(pk)
        serializer = PaperSerializer(paper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paper = self.get_object(pk)
        paper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class file_list_mixin(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class file_detail_mixin(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
