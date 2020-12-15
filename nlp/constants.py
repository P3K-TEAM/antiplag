stop_words_sk = [
    "a",
    "aby",
    "aj",
    "ak",
    "aká",
    "akáže",
    "aké",
    "akéže",
    "akého",
    "akéhože",
    "akej",
    "akejže",
    "akému",
    "akémuže",
    "ako",
    "akože",
    "akom",
    "akomže",
    "akou",
    "akouže",
    "akú",
    "akúže",
    "akých",
    "akýchže",
    "akým",
    "akýmže",
    "akými",
    "akýmiže",
    "ale",
    "alebo",
    "ani",
    "áno",
    "asi",
    "až",
    "ba",
    "bez",
    "bezo",
    "bol",
    "bola",
    "boli",
    "bolo",
    "bude",
    "budem",
    "budeme",
    "budeš",
    "budete",
    "budú",
    "by",
    "byť",
    "cez",
    "cezo",
    "čej",
    "či",
    "čí",
    "čia",
    "čie",
    "čieho",
    "čiemu",
    "čím",
    "čími",
    "čiu",
    "čo",
    "čoho",
    "čom",
    "čomu",
    "čou",
    "ďalšia",
    "ďalšie",
    "ďalšieho",
    "ďalšiemu",
    "ďalšiu",
    "ďalší",
    "ďalších",
    "ďalším",
    "ďalšími",
    "ďalšou",
    "dnes",
    "do",
    "ho",
    "ešte",
    "i",
    "iba",
    "ich",
    "im",
    "iná",
    "inej",
    "iné",
    "iného",
    "inému",
    "iní",
    "inom",
    "inú",
    "iný",
    "iných",
    "inými",
    "ja",
    "je",
    "jeho",
    "jej",
    "jemu",
    "ju",
    "k",
    "ká",
    "káže",
    "kam",
    "kamže",
    "každá",
    "každé",
    "každému",
    "každí",
    "každou",
    "každú",
    "každý",
    "každých",
    "každým",
    "každými",
    "kde",
    "keď",
    "kej",
    "kejže",
    "ké",
    "kéže",
    "kie",
    "kieho",
    "kiehože",
    "kiemu",
    "kiemuže",
    "kieže",
    "koho",
    "kom",
    "komu",
    "kou",
    "kouže",
    "kto",
    "ktorá",
    "ktorej",
    "ktoré",
    "ktorí",
    "ktorou",
    "ktorú",
    "ktorý",
    "ktorých",
    "ktorým",
    "ktorými",
    "ku",
    "kú",
    "kúže",
    "ký",
    "kýho",
    "kýhože",
    "kým",
    "kýmu",
    "kýmuže",
    "kýže",
    "lebo",
    "leda",
    "ledaže",
    "len",
    "ma",
    "má",
    "majú",
    "mám",
    "máme",
    "máš",
    "máte",
    "mať",
    "medzi",
    "mi",
    "mne",
    "mnou",
    "mňa",
    "moj",
    "moje",
    "mojej",
    "mojich",
    "mojim",
    "mojimi",
    "mojou",
    "moju",
    "môcť",
    "môj",
    "môjho",
    "môže",
    "môžem",
    "môžeme",
    "môžeš",
    "môžete",
    "môžu",
    "mu",
    "musieť",
    "musí",
    "musia",
    "musím",
    "musíme",
    "musíte",
    "musíš",
    "my",
    "na",
    "nad",
    "nado",
    "nám",
    "nami",
    "nás",
    "náš",
    "naša",
    "naše",
    "našej",
    "nášho",
    "naši",
    "našich",
    "našim",
    "našimi",
    "našou",
    "ne",
    "neho",
    "nech",
    "nej",
    "nejaká",
    "nejaké",
    "nejakého",
    "nejakej",
    "nejakému",
    "nejakom",
    "nejakou",
    "nejakú",
    "nejakých",
    "nejakým",
    "nejakými",
    "nemu",
    "než",
    "nich",
    "nič",
    "ničím",
    "ničoho",
    "ničom",
    "ničomu",
    "nie",
    "niektorá",
    "niektoré",
    "niektorého",
    "niektorej",
    "niektorému",
    "niektorom",
    "niektorou",
    "niektorú",
    "niektorý",
    "niektorých",
    "niektorým",
    "niektorými",
    "nim",
    "nimi",
    "ním",
    "ňom",
    "ňou",
    "ňu",
    "o",
    "od",
    "odo",
    "on",
    "ona",
    "oni",
    "ono",
    "ony",
    "oň",
    "oňho",
    "po",
    "pod",
    "podo",
    "podľa",
    "pokiaľ",
    "potom",
    "popod",
    "popri",
    "poza",
    "práve",
    "pre",
    "prečo",
    "preto",
    "pretože",
    "pred",
    "predo",
    "pri",
    "s",
    "sa",
    "si",
    "sme",
    "so",
    "som",
    "ste",
    "sú",
    "svoj",
    "svoja",
    "svoje",
    "svojho",
    "svojich",
    "svojim",
    "svojím",
    "svojimi",
    "svojou",
    "svoju",
    "ta",
    "tá",
    "tam",
    "tak",
    "takže",
    "táto",
    "teda",
    "tej",
    "ten",
    "tento",
    "tiež",
    "tí",
    "tie",
    "tieto",
    "títo",
    "to",
    "toho",
    "tohto",
    "tom",
    "tomto",
    "tomu",
    "tomuto",
    "toto",
    "tou",
    "touto",
    "tu",
    "tú",
    "túto",
    "tvoj",
    "tvoja",
    "tvoje",
    "tvojej",
    "tvojho",
    "tvoji",
    "tvojich",
    "tvojím",
    "tvojimi",
    "ty",
    "tých",
    "tým",
    "tými",
    "týmto",
    "už",
    "v",
    "vám",
    "vami",
    "vás",
    "váš",
    "vaša",
    "vaše",
    "vašej",
    "vášho",
    "vaši",
    "vašich",
    "vašim",
    "vaším",
    "viac",
    "vo",
    "však",
    "všetci",
    "všetka",
    "všetko",
    "všetky",
    "všetok",
    "vy",
    "z",
    "za",
    "začo",
    "začože",
    "zo",
    "že",
]

stop_words_cz = [
    "a",
    "aby",
    "aj",
    "ale",
    "anebo",
    "ani",
    "aniz",
    "ano",
    "asi",
    "avska",
    "az",
    "ba",
    "bez",
    "bude",
    "budem",
    "budes",
    "by",
    "byl",
    "byla",
    "byli",
    "bylo",
    "byt",
    "ci",
    "clanek",
    "clanku",
    "clanky",
    "co",
    "com",
    "coz",
    "cz",
    "dalsi",
    "design",
    "dnes",
    "do",
    "email",
    "ho",
    "i",
    "jak",
    "jake",
    "jako",
    "je",
    "jeho",
    "jej",
    "jeji",
    "jejich",
    "jen",
    "jeste",
    "jenz",
    "ji",
    "jine",
    "jiz",
    "jsem",
    "jses",
    "jsi",
    "jsme",
    "jsou",
    "jste",
    "k",
    "kam",
    "kde",
    "kdo",
    "kdyz",
    "ke",
    "ktera",
    "ktere",
    "kteri",
    "kterou",
    "ktery",
    "ku",
    "ma",
    "mate",
    "me",
    "mezi",
    "mi",
    "mit",
    "mne",
    "mnou",
    "muj",
    "muze",
    "my",
    "na",
    "nad",
    "nam",
    "napiste",
    "nas",
    "nasi",
    "ne",
    "nebo",
    "nebot",
    "necht",
    "nejsou",
    "není",
    "neni",
    "net",
    "nez",
    "ni",
    "nic",
    "nove",
    "novy",
    "nybrz",
    "o",
    "od",
    "ode",
    "on",
    "org",
    "pak",
    "po",
    "pod",
    "podle",
    "pokud",
    "pouze",
    "prave",
    "pred",
    "pres",
    "pri",
    "pro",
    "proc",
    "proto",
    "protoze",
    "prvni",
    "pta",
    "re",
    "s",
    "se",
    "si",
    "sice",
    "spol",
    "strana",
    "sve",
    "svuj",
    "svych",
    "svym",
    "svymi",
    "ta",
    "tak",
    "take",
    "takze",
    "tamhle",
    "tato",
    "tedy",
    "tema",
    "te",
    "ten",
    "tedy",
    "tento",
    "teto",
    "tim",
    "timto",
    "tipy",
    "to",
    "tohle",
    "toho",
    "tohoto",
    "tom",
    "tomto",
    "tomuto",
    "totiz",
    "tu",
    "tudiz",
    "tuto",
    "tvuj",
    "ty",
    "tyto",
    "u",
    "uz",
    "v",
    "vam",
    "vas",
    "vas",
    "vase",
    "ve",
    "vedle",
    "vice",
    "vsak",
    "vsechen",
    "vy",
    "vzdyt",
    "z",
    "za",
    "zda",
    "zde",
    "ze",
    "zpet",
    "zpravy",
]