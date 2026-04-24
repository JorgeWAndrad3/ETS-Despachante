import math

# BANCO DE DADOS GIGANTE EXTRAÍDO AUTOMATICAMENTE
CITY_DATA = {
    "winterland": {
        "name": "Winterland",
        "coords": [
            -159999.0,
            123949.0
        ],
        "region": "EU",
        "companies": []
    },
    "halloween": {
        "name": "Brackenreach",
        "coords": [
            -138442.0,
            97740.6
        ],
        "region": "EU",
        "companies": []
    },
    "aalborg": {
        "name": "Aalborg",
        "coords": [
            855.258,
            -35995.1
        ],
        "region": "EU",
        "companies": []
    },
    "aarhus": {
        "name": "Aarhus",
        "coords": [
            1808.59,
            -30744.9
        ],
        "region": "EU",
        "companies": []
    },
    "aberdeen": {
        "name": "Aberdeen",
        "coords": [
            -38846.7,
            -55270.3
        ],
        "region": "EU",
        "companies": []
    },
    "a": {
        "name": "A Coruna",
        "coords": [
            -82022.2,
            26714.3
        ],
        "region": "EU",
        "companies": []
    },
    "airolo": {
        "name": "Airolo",
        "coords": [
            -7945.0,
            22977.0
        ],
        "region": "EU",
        "companies": []
    },
    "akranes": {
        "name": "Akranes",
        "coords": [
            -91465.0,
            -101511.0
        ],
        "region": "EU",
        "companies": []
    },
    "akureyri": {
        "name": "Akureyri",
        "coords": [
            -77145.7,
            -101575.0
        ],
        "region": "EU",
        "companies": []
    },
    "alajarvi": {
        "name": "Alajärvi",
        "coords": [
            39005.8,
            -70673.2
        ],
        "region": "EU",
        "companies": []
    },
    "albacete": {
        "name": "Albacete",
        "coords": [
            -58305.4,
            58465.1
        ],
        "region": "EU",
        "companies": []
    },
    "alesund": {
        "name": "Ålesund",
        "coords": [
            -7676.78,
            -67160.3
        ],
        "region": "EU",
        "companies": []
    },
    "algeciras": {
        "name": "Algeciras",
        "coords": [
            -79942.5,
            70281.5
        ],
        "region": "EU",
        "companies": []
    },
    "almaraz": {
        "name": "Almaraz",
        "coords": [
            -74583.6,
            49536.4
        ],
        "region": "EU",
        "companies": []
    },
    "almeria": {
        "name": "Almeria",
        "coords": [
            -63592.0,
            69261.1
        ],
        "region": "EU",
        "companies": []
    },
    "alta": {
        "name": "Alta",
        "coords": [
            31414.82,
            -112629.4
        ],
        "region": "EU",
        "companies": []
    },
    "amsterdam": {
        "name": "Amsterdam",
        "coords": [
            -18598.7,
            -11736.2
        ],
        "region": "EU",
        "companies": []
    },
    "andenes": {
        "name": "Andenes",
        "coords": [
            19085.9,
            -108481.0
        ],
        "region": "EU",
        "companies": []
    },
    "andorra": {
        "name": "Andorra la Vella",
        "coords": [
            -39815.9,
            42009.7
        ],
        "region": "EU",
        "companies": []
    },
    "antwerp": {
        "name": "Antwerpen",
        "coords": [
            -21700.68,
            -5680.766
        ],
        "region": "EU",
        "companies": []
    },
    "arad": {
        "name": "Arad",
        "coords": [
            41265.9,
            24603.7
        ],
        "region": "EU",
        "companies": []
    },
    "are": {
        "name": "Åre",
        "coords": [
            11931.74,
            -71472.14
        ],
        "region": "EU",
        "companies": []
    },
    "argostoli": {
        "name": "Αργοστόλι",
        "coords": [
            41635.2,
            71521.2
        ],
        "region": "EU",
        "companies": []
    },
    "arnhem": {
        "name": "Arnhem",
        "coords": [
            -14732.1,
            -8798.42
        ],
        "region": "EU",
        "companies": []
    },
    "arvidsjaur": {
        "name": "Arvidsjaur",
        "coords": [
            26476.8,
            -83892.0
        ],
        "region": "EU",
        "companies": []
    },
    "athens": {
        "name": "Αθήνα",
        "coords": [
            56730.6,
            69993.6
        ],
        "region": "EU",
        "companies": []
    },
    "augustow": {
        "name": "Augustów",
        "coords": [
            43304.0,
            -19101.0
        ],
        "region": "EU",
        "companies": []
    },
    "aurach": {
        "name": "Aurach",
        "coords": [
            -441.102,
            8251.44
        ],
        "region": "EU",
        "companies": []
    },
    "bacau": {
        "name": "Bacău",
        "coords": [
            62137.4,
            18494.0
        ],
        "region": "EU",
        "companies": []
    },
    "bado": {
        "name": "Bad Oeynhausen",
        "coords": [
            -5724.91,
            -9493.73
        ],
        "region": "EU",
        "companies": []
    },
    "bakkebolle": {
        "name": "Bakkebølle",
        "coords": [
            6687.13,
            -24234.5
        ],
        "region": "EU",
        "companies": []
    },
    "baiamare": {
        "name": "Baia Mare",
        "coords": [
            49264.7,
            15764.6
        ],
        "region": "EU",
        "companies": []
    },
    "balvi": {
        "name": "Balvi",
        "coords": [
            54031.1,
            -39503.85
        ],
        "region": "EU",
        "companies": []
    },
    "barcelona": {
        "name": "Barcelona",
        "coords": [
            -38266.4,
            48093.5
        ],
        "region": "EU",
        "companies": []
    },
    "basel": {
        "name": "Basel",
        "coords": [
            -11649.5,
            17001.7
        ],
        "region": "EU",
        "companies": []
    },
    "bayonne": {
        "name": "Bayonne",
        "coords": [
            -52014.3,
            33499.0
        ],
        "region": "EU",
        "companies": []
    },
    "bbiala": {
        "name": "Bielsko-Biała",
        "coords": [
            31293.1,
            5749.52
        ],
        "region": "EU",
        "companies": []
    },
    "belfast": {
        "name": "Belfast",
        "coords": [
            -59692.36,
            -41394.61
        ],
        "region": "EU",
        "companies": []
    },
    "bergen": {
        "name": "Bergen",
        "coords": [
            -10512.6,
            -55447.4
        ],
        "region": "EU",
        "companies": []
    },
    "berlin": {
        "name": "Berlin",
        "coords": [
            10343.0,
            -9903.56
        ],
        "region": "EU",
        "companies": []
    },
    "bern": {
        "name": "Bern",
        "coords": [
            -12730.8,
            20130.1
        ],
        "region": "EU",
        "companies": []
    },
    "bialystok": {
        "name": "Białystok",
        "coords": [
            44098.4,
            -15083.4
        ],
        "region": "EU",
        "companies": []
    },
    "bilbao": {
        "name": "Bilbao",
        "coords": [
            -58108.2,
            32949.6
        ],
        "region": "EU",
        "companies": []
    },
    "birmingham": {
        "name": "Birmingham",
        "coords": [
            -45951.1,
            -20423.0
        ],
        "region": "EU",
        "companies": []
    },
    "birsay": {
        "name": "Birsay",
        "coords": [
            -38868.0,
            -69406.5
        ],
        "region": "EU",
        "companies": []
    },
    "blagoevgrad": {
        "name": "Благоевград",
        "coords": [
            50859.98,
            46605.68
        ],
        "region": "EU",
        "companies": []
    },
    "blonduos": {
        "name": "Blönduós",
        "coords": [
            -82233.6,
            -104774.0
        ],
        "region": "EU",
        "companies": []
    },
    "bodo": {
        "name": "Bodø",
        "coords": [
            15050.1,
            -93658.7
        ],
        "region": "EU",
        "companies": []
    },
    "bologna": {
        "name": "Bologna",
        "coords": [
            1895.71,
            34717.7
        ],
        "region": "EU",
        "companies": []
    },
    "bolungarvik": {
        "name": "Bolungarvík",
        "coords": [
            -87256.1,
            -112100.0
        ],
        "region": "EU",
        "companies": []
    },
    "bonn": {
        "name": "Bonn",
        "coords": [
            -12498.27,
            -467.13
        ],
        "region": "EU",
        "companies": []
    },
    "borgarnes": {
        "name": "Borgarnes",
        "coords": [
            -89285.6,
            -102462.0
        ],
        "region": "EU",
        "companies": []
    },
    "borlange": {
        "name": "Borlänge",
        "coords": [
            17542.5,
            -54327.3
        ],
        "region": "EU",
        "companies": []
    },
    "bratislava": {
        "name": "Bratislava",
        "coords": [
            24823.3,
            14831.0
        ],
        "region": "EU",
        "companies": []
    },
    "bremen": {
        "name": "Bremen",
        "coords": [
            -4919.98,
            -14099.2
        ],
        "region": "EU",
        "companies": []
    },
    "bremerhaven": {
        "name": "Bremerhaven",
        "coords": [
            -5715.6,
            -16976.6
        ],
        "region": "EU",
        "companies": []
    },
    "brno": {
        "name": "Brno",
        "coords": [
            22273.8,
            8964.95
        ],
        "region": "EU",
        "companies": []
    },
    "broadford": {
        "name": "Broadford",
        "coords": [
            -53239.6,
            -59401.6
        ],
        "region": "EU",
        "companies": []
    },
    "brugge": {
        "name": "Brugge",
        "coords": [
            -26592.49,
            -5502.55
        ],
        "region": "EU",
        "companies": []
    },
    "brussel": {
        "name": "Brussel",
        "coords": [
            -22100.25,
            -2415.148
        ],
        "region": "EU",
        "companies": []
    },
    "bucuresti": {
        "name": "București",
        "coords": [
            61121.0,
            31703.6
        ],
        "region": "EU",
        "companies": []
    },
    "budapest": {
        "name": "Budapest",
        "coords": [
            32367.8,
            17882.7
        ],
        "region": "EU",
        "companies": []
    },
    "burg": {
        "name": "Burg a. Fehmarn",
        "coords": [
            4095.55,
            -21142.2
        ],
        "region": "EU",
        "companies": []
    },
    "burgos": {
        "name": "Burgos",
        "coords": [
            -61834.0,
            37727.1
        ],
        "region": "EU",
        "companies": []
    },
    "bydgoszcz": {
        "name": "Bydgoszcz",
        "coords": [
            26440.3,
            -13850.1
        ],
        "region": "EU",
        "companies": []
    },
    "byvallen": {
        "name": "Byvallen",
        "coords": [
            17025.5,
            -61807.1
        ],
        "region": "EU",
        "companies": []
    },
    "bystrica": {
        "name": "Banská Bystrica",
        "coords": [
            32657.6,
            10680.5
        ],
        "region": "EU",
        "companies": []
    },
    "calais": {
        "name": "Calais",
        "coords": [
            -30243.0,
            -4985.64
        ],
        "region": "EU",
        "companies": []
    },
    "cambridge": {
        "name": "Cambridge",
        "coords": [
            -36822.7,
            -16119.4
        ],
        "region": "EU",
        "companies": []
    },
    "canterbury": {
        "name": "Canterbury",
        "coords": [
            -33881.88,
            -8782.05
        ],
        "region": "EU",
        "companies": []
    },
    "cardiff": {
        "name": "Cardiff",
        "coords": [
            -54005.3,
            -14698.4
        ],
        "region": "EU",
        "companies": []
    },
    "carlisle": {
        "name": "Carlisle",
        "coords": [
            -45889.2,
            -39573.5
        ],
        "region": "EU",
        "companies": []
    },
    "chania": {
        "name": "Χανιά",
        "coords": [
            58022.7,
            84933.6
        ],
        "region": "EU",
        "companies": []
    },
    "chelmsford": {
        "name": "Chelmsford",
        "coords": [
            -36472.1,
            -12878.6
        ],
        "region": "EU",
        "companies": []
    },
    "cherb": {
        "name": "Cherbourg",
        "coords": [
            -45091.8,
            -447.961
        ],
        "region": "EU",
        "companies": []
    },
    "chernyakh": {
        "name": "Черняховск (Chernyakhovsk)",
        "coords": [
            39226.42,
            -23167.04
        ],
        "region": "EU",
        "companies": []
    },
    "chios": {
        "name": "Χίος",
        "coords": [
            66300.0,
            66274.3
        ],
        "region": "EU",
        "companies": []
    },
    "cieszyn": {
        "name": "Cieszyn",
        "coords": [
            29295.3,
            6348.3
        ],
        "region": "EU",
        "companies": []
    },
    "clermont": {
        "name": "Clermont-Ferrand",
        "coords": [
            -30447.4,
            24698.4
        ],
        "region": "EU",
        "companies": []
    },
    "cluj": {
        "name": "Cluj-Napoca",
        "coords": [
            50303.3,
            18277.2
        ],
        "region": "EU",
        "companies": []
    },
    "constanta": {
        "name": "Constanța",
        "coords": [
            71731.7,
            30870.9
        ],
        "region": "EU",
        "companies": []
    },
    "craiova": {
        "name": "Craiova",
        "coords": [
            51918.5,
            33228.5
        ],
        "region": "EU",
        "companies": []
    },
    "croydon": {
        "name": "Croydon",
        "coords": [
            -39570.6,
            -10454.6
        ],
        "region": "EU",
        "companies": []
    },
    "debrecen": {
        "name": "Debrecen",
        "coords": [
            41641.6,
            17483.7
        ],
        "region": "EU",
        "companies": []
    },
    "dijon": {
        "name": "Dijon",
        "coords": [
            -22312.0,
            16721.5
        ],
        "region": "EU",
        "companies": []
    },
    "dombas": {
        "name": "Dombås",
        "coords": [
            -198.039,
            -64839.7
        ],
        "region": "EU",
        "companies": []
    },
    "donostia": {
        "name": "San Sebastian/Donostia",
        "coords": [
            -53789.7,
            34870.4
        ],
        "region": "EU",
        "companies": []
    },
    "dorotea": {
        "name": "Dorotea",
        "coords": [
            19996.0,
            -76524.2
        ],
        "region": "EU",
        "companies": []
    },
    "dortmund": {
        "name": "Dortmund",
        "coords": [
            -10270.5,
            -5598.41
        ],
        "region": "EU",
        "companies": []
    },
    "douglas": {
        "name": "Douglas",
        "coords": [
            -54292.5,
            -35572.3
        ],
        "region": "EU",
        "companies": []
    },
    "dover": {
        "name": "Dover",
        "coords": [
            -33321.9,
            -7884.36
        ],
        "region": "EU",
        "companies": []
    },
    "dresden": {
        "name": "Dresden",
        "coords": [
            12411.8,
            -1606.27
        ],
        "region": "EU",
        "companies": []
    },
    "dublin": {
        "name": "Dublin",
        "coords": [
            -63840.33,
            -31834.84
        ],
        "region": "EU",
        "companies": []
    },
    "duisburg": {
        "name": "Duisburg",
        "coords": [
            -12913.6,
            -6170.93
        ],
        "region": "EU",
        "companies": []
    },
    "dumfries": {
        "name": "Dumfries",
        "coords": [
            -49358.98,
            -41245.35
        ],
        "region": "EU",
        "companies": []
    },
    "dusseldorf": {
        "name": "Düsseldorf",
        "coords": [
            -13377.2,
            -4399.6
        ],
        "region": "EU",
        "companies": []
    },
    "edinburgh": {
        "name": "Edinburgh",
        "coords": [
            -44900.7,
            -47219.7
        ],
        "region": "EU",
        "companies": []
    },
    "eindhoven": {
        "name": "Eindhoven",
        "coords": [
            -17314.1,
            -6355.64
        ],
        "region": "EU",
        "companies": []
    },
    "elblag": {
        "name": "Elbląg",
        "coords": [
            31008.55,
            -19463.05
        ],
        "region": "EU",
        "companies": []
    },
    "elk": {
        "name": "Ełk",
        "coords": [
            41048.26,
            -18755.07
        ],
        "region": "EU",
        "companies": []
    },
    "erfurt": {
        "name": "Erfurt",
        "coords": [
            2436.19,
            -1733.77
        ],
        "region": "EU",
        "companies": []
    },
    "esbjerg": {
        "name": "Esbjerg",
        "coords": [
            -4699.43,
            -27555.9
        ],
        "region": "EU",
        "companies": []
    },
    "europoort": {
        "name": "Europoort",
        "coords": [
            -21791.1,
            -8987.42
        ],
        "region": "EU",
        "companies": []
    },
    "evie": {
        "name": "Evie",
        "coords": [
            -38532.4,
            -69291.6
        ],
        "region": "EU",
        "companies": []
    },
    "falun": {
        "name": "Falun",
        "coords": [
            18558.2,
            -56060.0
        ],
        "region": "EU",
        "companies": []
    },
    "fauske": {
        "name": "Fauske",
        "coords": [
            17549.3,
            -94905.7
        ],
        "region": "EU",
        "companies": []
    },
    "felixstowe": {
        "name": "Felixstowe",
        "coords": [
            -31664.6,
            -13837.2
        ],
        "region": "EU",
        "companies": []
    },
    "fishguard": {
        "name": "Fishguard",
        "coords": [
            -61284.68,
            -20395.5
        ],
        "region": "EU",
        "companies": []
    },
    "firenze": {
        "name": "Firenze",
        "coords": [
            2042.68,
            38929.3
        ],
        "region": "EU",
        "companies": []
    },
    "flensburg": {
        "name": "Flensburg",
        "coords": [
            -780.336,
            -22997.3
        ],
        "region": "EU",
        "companies": []
    },
    "folkestone": {
        "name": "Folkestone",
        "coords": [
            -35631.49,
            -6947.11
        ],
        "region": "EU",
        "companies": []
    },
    "forst": {
        "name": "Forst (Lausitz)",
        "coords": [
            13869.16,
            -5789.273
        ],
        "region": "EU",
        "companies": []
    },
    "frankfurt": {
        "name": "Frankfurt am Main",
        "coords": [
            -6112.34,
            2633.59
        ],
        "region": "EU",
        "companies": []
    },
    "fraserburgh": {
        "name": "Fraserburgh",
        "coords": [
            -36780.7,
            -58295.03
        ],
        "region": "EU",
        "companies": []
    },
    "frederikshv": {
        "name": "Frederikshavn",
        "coords": [
            2711.7,
            -38141.5
        ],
        "region": "EU",
        "companies": []
    },
    "ftwilliam": {
        "name": "Fort William",
        "coords": [
            -50854.3,
            -56132.7
        ],
        "region": "EU",
        "companies": []
    },
    "freiburg": {
        "name": "Freiburg im Breisgau",
        "coords": [
            -9528.0,
            11488.0
        ],
        "region": "EU",
        "companies": []
    },
    "furth": {
        "name": "Fürth",
        "coords": [
            1249.49,
            5970.42
        ],
        "region": "EU",
        "companies": []
    },
    "gaellivare": {
        "name": "Gällivare",
        "coords": [
            28533.1,
            -92701.2
        ],
        "region": "EU",
        "companies": []
    },
    "galway": {
        "name": "Galway",
        "coords": [
            -76553.42,
            -35578.97
        ],
        "region": "EU",
        "companies": []
    },
    "gavle": {
        "name": "Gävle",
        "coords": [
            23433.9,
            -56164.7
        ],
        "region": "EU",
        "companies": []
    },
    "gdansk": {
        "name": "Gdańsk",
        "coords": [
            28343.1,
            -20619.5
        ],
        "region": "EU",
        "companies": []
    },
    "gdynia": {
        "name": "Gdynia",
        "coords": [
            28154.4,
            -22045.9
        ],
        "region": "EU",
        "companies": []
    },
    "gedser": {
        "name": "Gedser",
        "coords": [
            6271.105,
            -22000.33
        ],
        "region": "EU",
        "companies": []
    },
    "geneve": {
        "name": "Genève",
        "coords": [
            -18099.1,
            23717.0
        ],
        "region": "EU",
        "companies": []
    },
    "genova": {
        "name": "Genova",
        "coords": [
            -8329.93,
            34875.6
        ],
        "region": "EU",
        "companies": []
    },
    "glasgow": {
        "name": "Glasgow",
        "coords": [
            -50384.7,
            -48471.6
        ],
        "region": "EU",
        "companies": []
    },
    "gorzow": {
        "name": "Gorzów Wlkp.",
        "coords": [
            17502.4,
            -11074.3
        ],
        "region": "EU",
        "companies": []
    },
    "goteborg": {
        "name": "Göteborg",
        "coords": [
            7235.89,
            -40227.5
        ],
        "region": "EU",
        "companies": []
    },
    "graz": {
        "name": "Graz",
        "coords": [
            18216.5,
            20552.7
        ],
        "region": "EU",
        "companies": []
    },
    "grimsby": {
        "name": "Grimsby",
        "coords": [
            -36117.9,
            -26575.2
        ],
        "region": "EU",
        "companies": []
    },
    "groedig": {
        "name": "Grödig",
        "coords": [
            8008.66,
            16688.1
        ],
        "region": "EU",
        "companies": []
    },
    "groningen": {
        "name": "Groningen",
        "coords": [
            -12662.06,
            -15700.68
        ],
        "region": "EU",
        "companies": []
    },
    "grudziadz": {
        "name": "Grudziądz",
        "coords": [
            31238.0,
            -16550.4
        ],
        "region": "EU",
        "companies": []
    },
    "gulbene": {
        "name": "Gulbene",
        "coords": [
            52449.3,
            -39194.3
        ],
        "region": "EU",
        "companies": []
    },
    "gyor": {
        "name": "Györ",
        "coords": [
            26889.0,
            17105.46
        ],
        "region": "EU",
        "companies": []
    },
    "haapsalu": {
        "name": "Haapsalu",
        "coords": [
            41258.4,
            -47857.6
        ],
        "region": "EU",
        "companies": []
    },
    "halle": {
        "name": "Halle (Saale)",
        "coords": [
            5833.82,
            -5407.88
        ],
        "region": "EU",
        "companies": []
    },
    "hamar": {
        "name": "Hamar",
        "coords": [
            5641.92,
            -57373.8
        ],
        "region": "EU",
        "companies": []
    },
    "hamburg": {
        "name": "Hamburg",
        "coords": [
            -1689.938,
            -16335.5
        ],
        "region": "EU",
        "companies": []
    },
    "hameenlinna": {
        "name": "Hämeenlinna",
        "coords": [
            42545.3,
            -59899.2
        ],
        "region": "EU",
        "companies": []
    },
    "hammerdal": {
        "name": "Hammerdal",
        "coords": [
            17427.9,
            -72450.2
        ],
        "region": "EU",
        "companies": []
    },
    "hannover": {
        "name": "Hannover",
        "coords": [
            -1928.93,
            -8916.4
        ],
        "region": "EU",
        "companies": []
    },
    "haparanda": {
        "name": "Haparanda",
        "coords": [
            37198.7,
            -86732.9
        ],
        "region": "EU",
        "companies": []
    },
    "heilbronn": {
        "name": "Heilbronn",
        "coords": [
            -6325.54,
            8009.55
        ],
        "region": "EU",
        "companies": []
    },
    "helsingborg": {
        "name": "Helsingborg",
        "coords": [
            9405.2,
            -29882.4
        ],
        "region": "EU",
        "companies": []
    },
    "heraklion": {
        "name": "Ηράκλειο",
        "coords": [
            66307.0,
            85699.7
        ],
        "region": "EU",
        "companies": []
    },
    "herning": {
        "name": "Herning",
        "coords": [
            -3455.63,
            -30797.0
        ],
        "region": "EU",
        "companies": []
    },
    "hiorthhamn": {
        "name": "Hiorthhamn",
        "coords": [
            20205.05,
            -163145.2
        ],
        "region": "EU",
        "companies": []
    },
    "hirtshals": {
        "name": "Hirtshals",
        "coords": [
            1425.47,
            -38873.3
        ],
        "region": "EU",
        "companies": []
    },
    "hofn": {
        "name": "Höfn",
        "coords": [
            -73990.5,
            -88514.8
        ],
        "region": "EU",
        "companies": []
    },
    "holmavik": {
        "name": "Hólmavík",
        "coords": [
            -84765.7,
            -106902.0
        ],
        "region": "EU",
        "companies": []
    },
    "holstebro": {
        "name": "Holstebro",
        "coords": [
            -3816.61,
            -32659.8
        ],
        "region": "EU",
        "companies": []
    },
    "holyhead": {
        "name": "Holyhead",
        "coords": [
            -56908.0,
            -30171.0
        ],
        "region": "EU",
        "companies": []
    },
    "honningsvag": {
        "name": "Honningsvåg",
        "coords": [
            35671.0,
            -118483.0
        ],
        "region": "EU",
        "companies": []
    },
    "hradec": {
        "name": "Hradec Králové",
        "coords": [
            19073.79,
            2817.289
        ],
        "region": "EU",
        "companies": []
    },
    "huelva": {
        "name": "Huelva",
        "coords": [
            -84687.45,
            62584.29
        ],
        "region": "EU",
        "companies": []
    },
    "huesca": {
        "name": "Huesca",
        "coords": [
            -48769.32,
            43817.16
        ],
        "region": "EU",
        "companies": []
    },
    "hull": {
        "name": "Hull",
        "coords": [
            -35543.9,
            -29239.1
        ],
        "region": "EU",
        "companies": []
    },
    "ijmuiden": {
        "name": "IJmuiden",
        "coords": [
            -19700.3,
            -12077.1
        ],
        "region": "EU",
        "companies": []
    },
    "innsbruck": {
        "name": "Innsbruck",
        "coords": [
            2250.09,
            19214.1
        ],
        "region": "EU",
        "companies": []
    },
    "inverness": {
        "name": "Inverness",
        "coords": [
            -46444.2,
            -59141.8
        ],
        "region": "EU",
        "companies": []
    },
    "ioannina": {
        "name": "Ιωάννινα",
        "coords": [
            41143.9,
            61500.4
        ],
        "region": "EU",
        "companies": []
    },
    "irun": {
        "name": "Irun",
        "coords": [
            -52725.0,
            35051.0
        ],
        "region": "EU",
        "companies": []
    },
    "isafjordur": {
        "name": "Ísafjörður",
        "coords": [
            -87022.4,
            -111213.0
        ],
        "region": "EU",
        "companies": []
    },
    "ivalo": {
        "name": "Ivalo",
        "coords": [
            40549.3,
            -106997.0
        ],
        "region": "EU",
        "companies": []
    },
    "jekabpils": {
        "name": "Jēkabpils",
        "coords": [
            50524.74,
            -34794.42
        ],
        "region": "EU",
        "companies": []
    },
    "joensuu": {
        "name": "Joensuu",
        "coords": [
            55432.7,
            -72269.4
        ],
        "region": "EU",
        "companies": []
    },
    "jonkoping": {
        "name": "Jönköping",
        "coords": [
            14177.3,
            -39575.6
        ],
        "region": "EU",
        "companies": []
    },
    "jonquera": {
        "name": "La Jonquera",
        "coords": [
            -33815.4,
            44330.0
        ],
        "region": "EU",
        "companies": []
    },
    "jyvaskyla": {
        "name": "Jyväskylä",
        "coords": [
            44465.3,
            -67197.3
        ],
        "region": "EU",
        "companies": []
    },
    "kaaresuvanto": {
        "name": "Kaaresuvanto",
        "coords": [
            32249.43,
            -103122.0
        ],
        "region": "EU",
        "companies": []
    },
    "kabdalis": {
        "name": "Kabdalis",
        "coords": [
            27861.8,
            -87772.4
        ],
        "region": "EU",
        "companies": []
    },
    "kajaani": {
        "name": "Kajaani",
        "coords": [
            48135.2,
            -79059.1
        ],
        "region": "EU",
        "companies": []
    },
    "kalamata": {
        "name": "Καλαμάτα",
        "coords": [
            50786.1,
            77064.9
        ],
        "region": "EU",
        "companies": []
    },
    "kalmar": {
        "name": "Kalmar",
        "coords": [
            20559.5,
            -33634.5
        ],
        "region": "EU",
        "companies": []
    },
    "kardla": {
        "name": "Kärdla",
        "coords": [
            39138.0,
            -47985.5
        ],
        "region": "EU",
        "companies": []
    },
    "karesuando": {
        "name": "Karesuando",
        "coords": [
            30677.7,
            -102857.0
        ],
        "region": "EU",
        "companies": []
    },
    "karlskrona": {
        "name": "Karlskrona",
        "coords": [
            17145.6,
            -30862.4
        ],
        "region": "EU",
        "companies": []
    },
    "karlstad": {
        "name": "Karlstad",
        "coords": [
            12989.8,
            -48643.2
        ],
        "region": "EU",
        "companies": []
    },
    "karsamaki": {
        "name": "Kärsämäki",
        "coords": [
            43370.3,
            -77032.8
        ],
        "region": "EU",
        "companies": []
    },
    "kassel": {
        "name": "Kassel",
        "coords": [
            -3031.32,
            -3898.7
        ],
        "region": "EU",
        "companies": []
    },
    "katowice": {
        "name": "Katowice",
        "coords": [
            30728.8,
            2458.83
        ],
        "region": "EU",
        "companies": []
    },
    "kavala": {
        "name": "Καβάλα",
        "coords": [
            57735.3,
            52360.8
        ],
        "region": "EU",
        "companies": []
    },
    "keflavik": {
        "name": "Keflavík Airport",
        "coords": [
            -94118.3,
            -98004.0
        ],
        "region": "EU",
        "companies": []
    },
    "kemi": {
        "name": "Kemi",
        "coords": [
            40102.53,
            -85560.6
        ],
        "region": "EU",
        "companies": []
    },
    "kemijarvi": {
        "name": "Kemijärvi",
        "coords": [
            44421.9,
            -92994.8
        ],
        "region": "EU",
        "companies": []
    },
    "kiel": {
        "name": "Kiel",
        "coords": [
            188.074,
            -20826.7
        ],
        "region": "EU",
        "companies": []
    },
    "kielce": {
        "name": "Kielce",
        "coords": [
            36896.1,
            -1011.63
        ],
        "region": "EU",
        "companies": []
    },
    "kirkwall": {
        "name": "Kirkwall",
        "coords": [
            -38213.7,
            -68910.3
        ],
        "region": "EU",
        "companies": []
    },
    "kiruna": {
        "name": "Kiruna",
        "coords": [
            27489.6,
            -98263.8
        ],
        "region": "EU",
        "companies": []
    },
    "klagenfurt": {
        "name": "Klagenfurt am Wörthersee",
        "coords": [
            14001.3,
            23027.6
        ],
        "region": "EU",
        "companies": []
    },
    "klaksvik": {
        "name": "Klaksvík",
        "coords": [
            -49964.0,
            -83155.7
        ],
        "region": "EU",
        "companies": []
    },
    "kobenhavn": {
        "name": "København",
        "coords": [
            7430.59,
            -27923.0
        ],
        "region": "EU",
        "companies": []
    },
    "koblenz": {
        "name": "Koblenz",
        "coords": [
            -11350.14,
            1411.76
        ],
        "region": "EU",
        "companies": []
    },
    "kokkola": {
        "name": "Kokkola",
        "coords": [
            36959.3,
            -74942.5
        ],
        "region": "EU",
        "companies": []
    },
    "kolding": {
        "name": "Kolding",
        "coords": [
            -1459.68,
            -27181.4
        ],
        "region": "EU",
        "companies": []
    },
    "kolka": {
        "name": "Kolka",
        "coords": [
            39247.91,
            -40718.97
        ],
        "region": "EU",
        "companies": []
    },
    "koln": {
        "name": "Köln",
        "coords": [
            -13150.8,
            -2732.75
        ],
        "region": "EU",
        "companies": []
    },
    "koper": {
        "name": "Koper",
        "coords": [
            11233.91,
            29456.66
        ],
        "region": "EU",
        "companies": []
    },
    "kosice": {
        "name": "Košice",
        "coords": [
            39843.9,
            10494.4
        ],
        "region": "EU",
        "companies": []
    },
    "koszalin": {
        "name": "Koszalin",
        "coords": [
            20321.5,
            -19548.9
        ],
        "region": "EU",
        "companies": []
    },
    "krafla": {
        "name": "Krafla",
        "coords": [
            -72508.4,
            -99684.3
        ],
        "region": "EU",
        "companies": []
    },
    "krakow": {
        "name": "Kraków",
        "coords": [
            34470.3,
            3249.68
        ],
        "region": "EU",
        "companies": []
    },
    "kristiansand": {
        "name": "Kristiansand",
        "coords": [
            -4638.28,
            -42891.5
        ],
        "region": "EU",
        "companies": []
    },
    "kristiansund": {
        "name": "Kristiansund",
        "coords": [
            -1544.84,
            -71305.13
        ],
        "region": "EU",
        "companies": []
    },
    "kristianstad": {
        "name": "Kristianstad",
        "coords": [
            13704.1,
            -29967.9
        ],
        "region": "EU",
        "companies": []
    },
    "kristiinank": {
        "name": "Kristiinankaupunki",
        "coords": [
            32474.3,
            -66055.6
        ],
        "region": "EU",
        "companies": []
    },
    "krosno": {
        "name": "Krosno",
        "coords": [
            40842.8,
            4645.48
        ],
        "region": "EU",
        "companies": []
    },
    "kuopio": {
        "name": "Kuopio",
        "coords": [
            49162.0,
            -71794.0
        ],
        "region": "EU",
        "companies": []
    },
    "kuressaare": {
        "name": "Kuressaare",
        "coords": [
            38652.6,
            -43361.0
        ],
        "region": "EU",
        "companies": []
    },
    "kuusamo": {
        "name": "Kuusamo",
        "coords": [
            49211.8,
            -89679.4
        ],
        "region": "EU",
        "companies": []
    },
    "lamia": {
        "name": "Λαμία",
        "coords": [
            49889.7,
            65483.1
        ],
        "region": "EU",
        "companies": []
    },
    "lappeenranta": {
        "name": "Lappeenranta",
        "coords": [
            52720.7,
            -63232.1
        ],
        "region": "EU",
        "companies": []
    },
    "larissa": {
        "name": "Λάρισα",
        "coords": [
            50113.6,
            62125.7
        ],
        "region": "EU",
        "companies": []
    },
    "lillehammer": {
        "name": "Lillehammer",
        "coords": [
            4658.43,
            -59429.31
        ],
        "region": "EU",
        "companies": []
    },
    "lleida": {
        "name": "Lleida",
        "coords": [
            -44866.44,
            46568.61
        ],
        "region": "EU",
        "companies": []
    },
    "leipzig": {
        "name": "Leipzig",
        "coords": [
            7238.62,
            -3384.61
        ],
        "region": "EU",
        "companies": []
    },
    "libramont": {
        "name": "Libramont-Chevigny",
        "coords": [
            -19318.04,
            1442.6846
        ],
        "region": "EU",
        "companies": []
    },
    "liege": {
        "name": "Liège",
        "coords": [
            -17144.41,
            -844.0664
        ],
        "region": "EU",
        "companies": []
    },
    "liepaja": {
        "name": "Liepāja",
        "coords": [
            35501.9,
            -33348.1
        ],
        "region": "EU",
        "companies": []
    },
    "lille": {
        "name": "Lille",
        "coords": [
            -26495.9,
            -2483.4
        ],
        "region": "EU",
        "companies": []
    },
    "limerick": {
        "name": "Limerick (Luimneach)",
        "coords": [
            -74455.1,
            -30004.85
        ],
        "region": "EU",
        "companies": []
    },
    "linkoping": {
        "name": "Linköping",
        "coords": [
            18586.1,
            -43325.2
        ],
        "region": "EU",
        "companies": []
    },
    "linz": {
        "name": "Linz",
        "coords": [
            13665.7,
            15754.6
        ],
        "region": "EU",
        "companies": []
    },
    "lisburn": {
        "name": "Lisburn",
        "coords": [
            -60535.71,
            -40179.05
        ],
        "region": "EU",
        "companies": []
    },
    "liverpool": {
        "name": "Liverpool",
        "coords": [
            -48871.7,
            -29091.8
        ],
        "region": "EU",
        "companies": []
    },
    "livorno": {
        "name": "Livorno",
        "coords": [
            -2974.56,
            40352.3
        ],
        "region": "EU",
        "companies": []
    },
    "lodz": {
        "name": "Łódź",
        "coords": [
            31532.9,
            -6276.34
        ],
        "region": "EU",
        "companies": []
    },
    "london": {
        "name": "London",
        "coords": [
            -39546.9,
            -11564.2
        ],
        "region": "EU",
        "companies": []
    },
    "londonderry": {
        "name": "Londonderry",
        "coords": [
            -64011.9,
            -45948.3
        ],
        "region": "EU",
        "companies": []
    },
    "longyearbyen": {
        "name": "Longyearbyen",
        "coords": [
            18949.57,
            -161887.1
        ],
        "region": "EU",
        "companies": []
    },
    "lublin": {
        "name": "Lublin",
        "coords": [
            42859.6,
            -3967.52
        ],
        "region": "EU",
        "companies": []
    },
    "lulea": {
        "name": "Luleå",
        "coords": [
            33242.7,
            -84747.6
        ],
        "region": "EU",
        "companies": []
    },
    "luxembourg": {
        "name": "Luxembourg",
        "coords": [
            -16345.31,
            3665.301
        ],
        "region": "EU",
        "companies": []
    },
    "lyon": {
        "name": "Lyon",
        "coords": [
            -23869.8,
            25892.3
        ],
        "region": "EU",
        "companies": []
    },
    "maastricht": {
        "name": "Maastricht",
        "coords": [
            -16694.99,
            -3208.71
        ],
        "region": "EU",
        "companies": []
    },
    "magdeburg": {
        "name": "Magdeburg",
        "coords": [
            4484.25,
            -7752.3
        ],
        "region": "EU",
        "companies": []
    },
    "mainz": {
        "name": "Mainz",
        "coords": [
            -10114.5,
            2678.53
        ],
        "region": "EU",
        "companies": []
    },
    "malmo": {
        "name": "Malmö",
        "coords": [
            10744.9,
            -27481.2
        ],
        "region": "EU",
        "companies": []
    },
    "manchester": {
        "name": "Manchester",
        "coords": [
            -45548.7,
            -27815.0
        ],
        "region": "EU",
        "companies": []
    },
    "mannheim": {
        "name": "Mannheim",
        "coords": [
            -7751.22,
            6075.05
        ],
        "region": "EU",
        "companies": []
    },
    "manresa": {
        "name": "Manresa",
        "coords": [
            -39339.8,
            46488.6
        ],
        "region": "EU",
        "companies": []
    },
    "mariehamn": {
        "name": "Mariehamn",
        "coords": [
            30310.66,
            -52861.73
        ],
        "region": "EU",
        "companies": []
    },
    "mengibar": {
        "name": "Mengibar",
        "coords": [
            -67814.9,
            63139.8
        ],
        "region": "EU",
        "companies": []
    },
    "metz": {
        "name": "Metz",
        "coords": [
            -16294.5,
            7463.71
        ],
        "region": "EU",
        "companies": []
    },
    "mikkeli": {
        "name": "Mikkeli",
        "coords": [
            49501.3,
            -64918.8
        ],
        "region": "EU",
        "companies": []
    },
    "milano": {
        "name": "Milano",
        "coords": [
            -6616.31,
            28982.8
        ],
        "region": "EU",
        "companies": []
    },
    "mitilini": {
        "name": "Μυτιλήνη",
        "coords": [
            67458.6,
            61970.7
        ],
        "region": "EU",
        "companies": []
    },
    "mlada": {
        "name": "Mladá Boleslav",
        "coords": [
            15578.04,
            1804.367
        ],
        "region": "EU",
        "companies": []
    },
    "modena": {
        "name": "Modena",
        "coords": [
            -110.371,
            34033.2
        ],
        "region": "EU",
        "companies": []
    },
    "mo": {
        "name": "Mo i Rana",
        "coords": [
            14312.2,
            -87673.5
        ],
        "region": "EU",
        "companies": []
    },
    "mosjoen": {
        "name": "Mosjoen",
        "coords": [
            12554.1,
            -86771.5
        ],
        "region": "EU",
        "companies": []
    },
    "mukacheve": {
        "name": "Мукачеве (Mukacheve)",
        "coords": [
            45497.1,
            11834.6
        ],
        "region": "EU",
        "companies": []
    },
    "munchen": {
        "name": "München",
        "coords": [
            3179.07,
            14133.0
        ],
        "region": "EU",
        "companies": []
    },
    "narbonne": {
        "name": "Narbonne",
        "coords": [
            -33667.0,
            38783.3
        ],
        "region": "EU",
        "companies": []
    },
    "narvik": {
        "name": "Narvik",
        "coords": [
            20756.16,
            -102229.8
        ],
        "region": "EU",
        "companies": []
    },
    "newcastle": {
        "name": "Newcastle-upon-Tyne",
        "coords": [
            -39778.0,
            -38787.7
        ],
        "region": "EU",
        "companies": []
    },
    "nowogard": {
        "name": "Nowogard",
        "coords": [
            17888.8,
            -16557.9
        ],
        "region": "EU",
        "companies": []
    },
    "nurnberg": {
        "name": "Nürnberg",
        "coords": [
            1987.47,
            6221.02
        ],
        "region": "EU",
        "companies": []
    },
    "nynashamn": {
        "name": "Nynäshamn",
        "coords": [
            26448.2,
            -46165.7
        ],
        "region": "EU",
        "companies": []
    },
    "oban": {
        "name": "Oban",
        "coords": [
            -53420.4,
            -53472.1
        ],
        "region": "EU",
        "companies": []
    },
    "oberhausen": {
        "name": "Oberhausen",
        "coords": [
            -11793.2,
            -5322.95
        ],
        "region": "EU",
        "companies": []
    },
    "odense": {
        "name": "Odense",
        "coords": [
            1617.69,
            -26700.4
        ],
        "region": "EU",
        "companies": []
    },
    "ogre": {
        "name": "Ogre",
        "coords": [
            46996.41,
            -35785.24
        ],
        "region": "EU",
        "companies": []
    },
    "olsztyn": {
        "name": "Olsztyn",
        "coords": [
            34758.6,
            -17885.9
        ],
        "region": "EU",
        "companies": []
    },
    "opole": {
        "name": "Opole",
        "coords": [
            27536.9,
            -679.391
        ],
        "region": "EU",
        "companies": []
    },
    "oppdal": {
        "name": "Oppdal",
        "coords": [
            2560.71,
            -67492.96
        ],
        "region": "EU",
        "companies": []
    },
    "oradea": {
        "name": "Oradea",
        "coords": [
            43740.25,
            19397.16
        ],
        "region": "EU",
        "companies": []
    },
    "orebro": {
        "name": "Örebro",
        "coords": [
            17087.8,
            -48374.7
        ],
        "region": "EU",
        "companies": []
    },
    "orkanger": {
        "name": "Orkanger",
        "coords": [
            2744.29,
            -70840.44
        ],
        "region": "EU",
        "companies": []
    },
    "orlea": {
        "name": "Orléans",
        "coords": [
            -33526.4,
            11781.6
        ],
        "region": "EU",
        "companies": []
    },
    "ornskoldsvik": {
        "name": "Örnsköldsvik",
        "coords": [
            25702.1,
            -70706.0
        ],
        "region": "EU",
        "companies": []
    },
    "oslo": {
        "name": "Oslo",
        "coords": [
            4390.91,
            -53410.5
        ],
        "region": "EU",
        "companies": []
    },
    "osnabruck": {
        "name": "Osnabrück",
        "coords": [
            -7456.28,
            -9841.73
        ],
        "region": "EU",
        "companies": []
    },
    "ostersund": {
        "name": "Östersund",
        "coords": [
            15249.6,
            -70178.2
        ],
        "region": "EU",
        "companies": []
    },
    "ostrava": {
        "name": "Ostrava",
        "coords": [
            28231.9,
            5136.1
        ],
        "region": "EU",
        "companies": []
    },
    "ostroleka": {
        "name": "Ostrołęka",
        "coords": [
            38890.4,
            -14259.3
        ],
        "region": "EU",
        "companies": []
    },
    "ostrowm": {
        "name": "Ostrów Mazowiecka",
        "coords": [
            39853.73,
            -12808.68
        ],
        "region": "EU",
        "companies": []
    },
    "otta": {
        "name": "Otta",
        "coords": [
            1772.52,
            -62862.78
        ],
        "region": "EU",
        "companies": []
    },
    "oulu": {
        "name": "Oulu",
        "coords": [
            41759.8,
            -82463.4
        ],
        "region": "EU",
        "companies": []
    },
    "padborg": {
        "name": "Padborg",
        "coords": [
            -1608.62,
            -24340.2
        ],
        "region": "EU",
        "companies": []
    },
    "paris": {
        "name": "Paris",
        "coords": [
            -30494.9,
            6998.41
        ],
        "region": "EU",
        "companies": []
    },
    "parma": {
        "name": "Parma",
        "coords": [
            -2529.54,
            33610.7
        ],
        "region": "EU",
        "companies": []
    },
    "patras": {
        "name": "Πάτρα",
        "coords": [
            46684.7,
            71014.3
        ],
        "region": "EU",
        "companies": []
    },
    "pau": {
        "name": "Pau",
        "coords": [
            -47944.2,
            36082.7
        ],
        "region": "EU",
        "companies": []
    },
    "pecs": {
        "name": "Pécs",
        "coords": [
            29039.9,
            26311.6
        ],
        "region": "EU",
        "companies": []
    },
    "perpignan": {
        "name": "Perpignan",
        "coords": [
            -34520.9,
            41436.8
        ],
        "region": "EU",
        "companies": []
    },
    "perth": {
        "name": "Perth",
        "coords": [
            -43488.0,
            -52640.0
        ],
        "region": "EU",
        "companies": []
    },
    "piatra": {
        "name": "Piatra Neamţ",
        "coords": [
            59773.0,
            17823.8
        ],
        "region": "EU",
        "companies": []
    },
    "pila": {
        "name": "Piła",
        "coords": [
            23749.3,
            -13123.9
        ],
        "region": "EU",
        "companies": []
    },
    "plock": {
        "name": "Płock",
        "coords": [
            32393.4,
            -10665.9
        ],
        "region": "EU",
        "companies": []
    },
    "plymouth": {
        "name": "Plymouth",
        "coords": [
            -60041.4,
            -7882.32
        ],
        "region": "EU",
        "companies": []
    },
    "portree": {
        "name": "Portree",
        "coords": [
            -53845.9,
            -61021.8
        ],
        "region": "EU",
        "companies": []
    },
    "portsmouth": {
        "name": "Portsmouth",
        "coords": [
            -43034.2,
            -5752.09
        ],
        "region": "EU",
        "companies": []
    },
    "porvoo": {
        "name": "Porvoo",
        "coords": [
            47431.8,
            -57017.7
        ],
        "region": "EU",
        "companies": []
    },
    "poznan": {
        "name": "Poznań",
        "coords": [
            22863.4,
            -9112.2
        ],
        "region": "EU",
        "companies": []
    },
    "prague": {
        "name": "Praha",
        "coords": [
            14299.7,
            3978.97
        ],
        "region": "EU",
        "companies": []
    },
    "przemysl": {
        "name": "Przemyśl",
        "coords": [
            44670.6,
            3973.53
        ],
        "region": "EU",
        "companies": []
    },
    "puttgarden": {
        "name": "Puttgarden",
        "coords": [
            4001.17,
            -21612.7
        ],
        "region": "EU",
        "companies": []
    },
    "rakvere": {
        "name": "Rakvere",
        "coords": [
            48887.4,
            -50675.76
        ],
        "region": "EU",
        "companies": []
    },
    "radom": {
        "name": "Radom",
        "coords": [
            38543.6,
            -4837.94
        ],
        "region": "EU",
        "companies": []
    },
    "ramsey": {
        "name": "Ramsey",
        "coords": [
            -53660.9,
            -36755.5
        ],
        "region": "EU",
        "companies": []
    },
    "reims": {
        "name": "Reims",
        "coords": [
            -24021.9,
            5799.34
        ],
        "region": "EU",
        "companies": []
    },
    "reydar": {
        "name": "Reyðarfjörður",
        "coords": [
            -69235.1,
            -92368.9
        ],
        "region": "EU",
        "companies": []
    },
    "reykjavik": {
        "name": "Reykjavík",
        "coords": [
            -90723.9,
            -98482.6
        ],
        "region": "EU",
        "companies": []
    },
    "rhodes": {
        "name": "Ρόδος",
        "coords": [
            77441.7,
            76538.8
        ],
        "region": "EU",
        "companies": []
    },
    "rodbyhavn": {
        "name": "Rødbyhavn",
        "coords": [
            4378.43,
            -22326.5
        ],
        "region": "EU",
        "companies": []
    },
    "ronne": {
        "name": "Rønne",
        "coords": [
            15919.91,
            -24530.53
        ],
        "region": "EU",
        "companies": []
    },
    "rostock": {
        "name": "Rostock",
        "coords": [
            6490.95,
            -18588.9
        ],
        "region": "EU",
        "companies": []
    },
    "rotterdam": {
        "name": "Rotterdam",
        "coords": [
            -20156.0,
            -9135.8
        ],
        "region": "EU",
        "companies": []
    },
    "roudant": {
        "name": "Roudant",
        "coords": [
            -18600.44,
            33427.64
        ],
        "region": "EU",
        "companies": []
    },
    "rovaniemi": {
        "name": "Rovaniemi",
        "coords": [
            39885.0,
            -90311.4
        ],
        "region": "EU",
        "companies": []
    },
    "rzeszow": {
        "name": "Rzeszów",
        "coords": [
            42993.9,
            2919.09
        ],
        "region": "EU",
        "companies": []
    },
    "saldus": {
        "name": "Saldus",
        "coords": [
            39740.67,
            -33969.27
        ],
        "region": "EU",
        "companies": []
    },
    "salzburg": {
        "name": "Salzburg",
        "coords": [
            11075.84,
            18564.5
        ],
        "region": "EU",
        "companies": []
    },
    "sangerhausen": {
        "name": "Sangerhausen",
        "coords": [
            2204.59,
            -4672.66
        ],
        "region": "EU",
        "companies": []
    },
    "sanok": {
        "name": "Sanok",
        "coords": [
            43027.8,
            5134.43
        ],
        "region": "EU",
        "companies": []
    },
    "santander": {
        "name": "Santander",
        "coords": [
            -61881.09,
            31926.81
        ],
        "region": "EU",
        "companies": []
    },
    "selfoss": {
        "name": "Selfoss",
        "coords": [
            -89796.2,
            -95809.1
        ],
        "region": "EU",
        "companies": []
    },
    "seydis": {
        "name": "Seyðisfjörður",
        "coords": [
            -68112.5,
            -93717.5
        ],
        "region": "EU",
        "companies": []
    },
    "sheffield": {
        "name": "Sheffield",
        "coords": [
            -42688.8,
            -26687.6
        ],
        "region": "EU",
        "companies": []
    },
    "sibiu": {
        "name": "Sibiu",
        "coords": [
            52810.4,
            25058.37
        ],
        "region": "EU",
        "companies": []
    },
    "siedlce": {
        "name": "Siedlce",
        "coords": [
            41651.7,
            -9261.17
        ],
        "region": "EU",
        "companies": []
    },
    "skelleftea": {
        "name": "Skellefteå",
        "coords": [
            30527.3,
            -79989.0
        ],
        "region": "EU",
        "companies": []
    },
    "sligo": {
        "name": "Sligo (Sligeach)",
        "coords": [
            -71511.34,
            -42217.29
        ],
        "region": "EU",
        "companies": []
    },
    "soderhamn": {
        "name": "Söderhamn",
        "coords": [
            21956.2,
            -59633.3
        ],
        "region": "EU",
        "companies": []
    },
    "sodertalje": {
        "name": "Södertälje",
        "coords": [
            23525.2,
            -46319.9
        ],
        "region": "EU",
        "companies": []
    },
    "southampton": {
        "name": "Southampton",
        "coords": [
            -46338.7,
            -7523.25
        ],
        "region": "EU",
        "companies": []
    },
    "stargard": {
        "name": "Stargard",
        "coords": [
            17693.37,
            -14559.1
        ],
        "region": "EU",
        "companies": []
    },
    "stavanger": {
        "name": "Stavanger",
        "coords": [
            -10553.7,
            -48126.8
        ],
        "region": "EU",
        "companies": []
    },
    "steinkjer": {
        "name": "Steinkjer",
        "coords": [
            6718.09,
            -75178.3
        ],
        "region": "EU",
        "companies": []
    },
    "sthelier": {
        "name": "St Helier",
        "coords": [
            -47502.3,
            2063.23
        ],
        "region": "EU",
        "companies": []
    },
    "stockholm": {
        "name": "Stockholm",
        "coords": [
            24747.3,
            -47131.9
        ],
        "region": "EU",
        "companies": []
    },
    "stranraer": {
        "name": "Stranraer",
        "coords": [
            -55082.47,
            -41963.15
        ],
        "region": "EU",
        "companies": []
    },
    "strasbourg": {
        "name": "Strasbourg",
        "coords": [
            -10786.9,
            11198.7
        ],
        "region": "EU",
        "companies": []
    },
    "stroemsund": {
        "name": "Strömsund",
        "coords": [
            18192.0,
            -74358.9
        ],
        "region": "EU",
        "companies": []
    },
    "stromness": {
        "name": "Stromness",
        "coords": [
            -39126.5,
            -68742.7
        ],
        "region": "EU",
        "companies": []
    },
    "stuttgart": {
        "name": "Stuttgart",
        "coords": [
            -4957.84,
            10047.0
        ],
        "region": "EU",
        "companies": []
    },
    "sundsvall": {
        "name": "Sundsvall",
        "coords": [
            22379.4,
            -65796.6
        ],
        "region": "EU",
        "companies": []
    },
    "suomussalmi": {
        "name": "Suomussalmi",
        "coords": [
            49736.84,
            -83555.9
        ],
        "region": "EU",
        "companies": []
    },
    "suwalki": {
        "name": "Suwałki",
        "coords": [
            43448.6,
            -21045.2
        ],
        "region": "EU",
        "companies": []
    },
    "sveg": {
        "name": "Sveg",
        "coords": [
            15719.2,
            -63750.8
        ],
        "region": "EU",
        "companies": []
    },
    "svolvaer": {
        "name": "Svolvær",
        "coords": [
            13393.7,
            -100028.0
        ],
        "region": "EU",
        "companies": []
    },
    "swansea": {
        "name": "Swansea",
        "coords": [
            -56896.0,
            -16881.9
        ],
        "region": "EU",
        "companies": []
    },
    "swinoujscie": {
        "name": "Świnoujście",
        "coords": [
            13488.7,
            -17184.3
        ],
        "region": "EU",
        "companies": []
    },
    "szczecin": {
        "name": "Szczecin",
        "coords": [
            14765.1,
            -15406.9
        ],
        "region": "EU",
        "companies": []
    },
    "szeged": {
        "name": "Szeged",
        "coords": [
            36880.7,
            24565.7
        ],
        "region": "EU",
        "companies": []
    },
    "taurage": {
        "name": "Tauragė",
        "coords": [
            40034.53,
            -26589.28
        ],
        "region": "EU",
        "companies": []
    },
    "thessaloniki": {
        "name": "Θεσσαλονίκη",
        "coords": [
            51623.8,
            55931.2
        ],
        "region": "EU",
        "companies": []
    },
    "thurso": {
        "name": "Thurso",
        "coords": [
            -41731.6,
            -66122.4
        ],
        "region": "EU",
        "companies": []
    },
    "timisoara": {
        "name": "Timișoara",
        "coords": [
            41402.3,
            27128.0
        ],
        "region": "EU",
        "companies": []
    },
    "torino": {
        "name": "Torino",
        "coords": [
            -12697.3,
            30932.0
        ],
        "region": "EU",
        "companies": []
    },
    "tornio": {
        "name": "Tornio",
        "coords": [
            38089.9,
            -86729.5
        ],
        "region": "EU",
        "companies": []
    },
    "torshavn": {
        "name": "Tórshavn",
        "coords": [
            -51298.5,
            -81483.6
        ],
        "region": "EU",
        "companies": []
    },
    "travemuende": {
        "name": "Travemünde",
        "coords": [
            3471.27,
            -19526.9
        ],
        "region": "EU",
        "companies": []
    },
    "trelleborg": {
        "name": "Trelleborg",
        "coords": [
            10808.3,
            -25887.0
        ],
        "region": "EU",
        "companies": []
    },
    "trieste": {
        "name": "Trieste",
        "coords": [
            10593.79,
            27566.76
        ],
        "region": "EU",
        "companies": []
    },
    "trikala": {
        "name": "Τρίκαλα",
        "coords": [
            46870.0,
            62412.9
        ],
        "region": "EU",
        "companies": []
    },
    "trinity": {
        "name": "Trinity",
        "coords": [
            -47726.4,
            1242.87
        ],
        "region": "EU",
        "companies": []
    },
    "tromso": {
        "name": "Tromsø",
        "coords": [
            24296.79,
            -109134.6
        ],
        "region": "EU",
        "companies": []
    },
    "trondheim": {
        "name": "Trondheim",
        "coords": [
            3550.63,
            -72880.9
        ],
        "region": "EU",
        "companies": []
    },
    "tukums": {
        "name": "Tukums",
        "coords": [
            41200.5,
            -37187.2
        ],
        "region": "EU",
        "companies": []
    },
    "uelzen": {
        "name": "Uelzen",
        "coords": [
            3140.0,
            -12273.0
        ],
        "region": "EU",
        "companies": []
    },
    "ullapool": {
        "name": "Ullapool",
        "coords": [
            -48956.0,
            -64780.0
        ],
        "region": "EU",
        "companies": []
    },
    "ulm": {
        "name": "Ulm",
        "coords": [
            -2928.57,
            12657.0
        ],
        "region": "EU",
        "companies": []
    },
    "umea": {
        "name": "Umeå",
        "coords": [
            28991.3,
            -75080.6
        ],
        "region": "EU",
        "companies": []
    },
    "uppsala": {
        "name": "Uppsala",
        "coords": [
            24021.5,
            -51634.5
        ],
        "region": "EU",
        "companies": []
    },
    "uzhhorod": {
        "name": "Ужгород (Uzhhorod)",
        "coords": [
            43781.0,
            11200.1
        ],
        "region": "EU",
        "companies": []
    },
    "vaasa": {
        "name": "Vaasa",
        "coords": [
            32998.3,
            -71017.0
        ],
        "region": "EU",
        "companies": []
    },
    "vaduz": {
        "name": "Vaduz",
        "coords": [
            -3865.21,
            18906.6
        ],
        "region": "EU",
        "companies": []
    },
    "valga": {
        "name": "Valga",
        "coords": [
            49770.1,
            -42978.1
        ],
        "region": "EU",
        "companies": []
    },
    "valka": {
        "name": "Valka",
        "coords": [
            49463.9,
            -42752.1
        ],
        "region": "EU",
        "companies": []
    },
    "vantaa": {
        "name": "Vantaa",
        "coords": [
            45004.3,
            -56661.7
        ],
        "region": "EU",
        "companies": []
    },
    "varkaus": {
        "name": "Varkaus",
        "coords": [
            50510.6,
            -68975.5
        ],
        "region": "EU",
        "companies": []
    },
    "vasteraas": {
        "name": "Västerås",
        "coords": [
            20937.7,
            -50468.3
        ],
        "region": "EU",
        "companies": []
    },
    "vaxjo": {
        "name": "Växjö",
        "coords": [
            16044.4,
            -34835.6
        ],
        "region": "EU",
        "companies": []
    },
    "venezia": {
        "name": "Venezia",
        "coords": [
            5089.88,
            30078.9
        ],
        "region": "EU",
        "companies": []
    },
    "verona": {
        "name": "Verona",
        "coords": [
            39.1094,
            29453.3
        ],
        "region": "EU",
        "companies": []
    },
    "vestmannaeyjar": {
        "name": "Vestmannaeyjar",
        "coords": [
            -90650.19,
            -91439.36
        ],
        "region": "EU",
        "companies": []
    },
    "viborg": {
        "name": "Viborg",
        "coords": [
            -1033.26,
            -33233.7
        ],
        "region": "EU",
        "companies": []
    },
    "vicenza": {
        "name": "Vicenza",
        "coords": [
            3032.82,
            29533.5
        ],
        "region": "EU",
        "companies": []
    },
    "viitasaari": {
        "name": "Viitasaari",
        "coords": [
            44214.6,
            -72353.1
        ],
        "region": "EU",
        "companies": []
    },
    "vigo": {
        "name": "Vigo",
        "coords": [
            -84721.4,
            32600.7
        ],
        "region": "EU",
        "companies": []
    },
    "vik": {
        "name": "Vík",
        "coords": [
            -86702.3,
            -89729.3
        ],
        "region": "EU",
        "companies": []
    },
    "villach": {
        "name": "Villach",
        "coords": [
            11001.2,
            25584.0
        ],
        "region": "EU",
        "companies": []
    },
    "vilsund": {
        "name": "Vilsund",
        "coords": [
            -3192.332,
            -35727.34
        ],
        "region": "EU",
        "companies": []
    },
    "volgsjoen": {
        "name": "Volgsjön",
        "coords": [
            20440.0,
            -78561.2
        ],
        "region": "EU",
        "companies": []
    },
    "walcz": {
        "name": "Wałcz",
        "coords": [
            21139.41,
            -14321.42
        ],
        "region": "EU",
        "companies": []
    },
    "warszawa": {
        "name": "Warszawa",
        "coords": [
            37353.6,
            -9467.43
        ],
        "region": "EU",
        "companies": []
    },
    "werlte": {
        "name": "Werlte",
        "coords": [
            -9247.227,
            -12700.35
        ],
        "region": "EU",
        "companies": []
    },
    "wexford": {
        "name": "Wexford",
        "coords": [
            -67015.93,
            -25257.44
        ],
        "region": "EU",
        "companies": []
    },
    "wick": {
        "name": "Wick",
        "coords": [
            -39662.3,
            -64980.1
        ],
        "region": "EU",
        "companies": []
    },
    "wien": {
        "name": "Wien",
        "coords": [
            21298.3,
            14215.5
        ],
        "region": "EU",
        "companies": []
    },
    "wiesbaden": {
        "name": "Wiesbaden",
        "coords": [
            -9910.27,
            2026.05
        ],
        "region": "EU",
        "companies": []
    },
    "winsen": {
        "name": "Winsen",
        "coords": [
            1267.059,
            -15030.89
        ],
        "region": "EU",
        "companies": []
    },
    "wroclaw": {
        "name": "Wrocław",
        "coords": [
            23500.3,
            -1890.36
        ],
        "region": "EU",
        "companies": []
    },
    "ytterhogdal": {
        "name": "Ytterhogdal",
        "coords": [
            16561.7,
            -65028.8
        ],
        "region": "EU",
        "companies": []
    },
    "zamosc": {
        "name": "Zamość",
        "coords": [
            46167.3,
            -1538.1
        ],
        "region": "EU",
        "companies": []
    },
    "zelenogradsk": {
        "name": "Зеленоградск (Zelenogradsk)",
        "coords": [
            34230.9,
            -24320.9
        ],
        "region": "EU",
        "companies": []
    },
    "zgorzelec": {
        "name": "Zgorzelec",
        "coords": [
            16779.7,
            -1715.38
        ],
        "region": "EU",
        "companies": []
    },
    "zurich": {
        "name": "Zürich",
        "coords": [
            -8473.81,
            17968.5
        ],
        "region": "EU",
        "companies": []
    },
    "zwolle": {
        "name": "Zwolle",
        "coords": [
            -14526.0,
            -12292.1
        ],
        "region": "EU",
        "companies": []
    },
    "alakurtti": {
        "name": "Алакуртти",
        "coords": [
            48960.42,
            -94661.89
        ],
        "region": "EU",
        "companies": []
    },
    "alehovshina": {
        "name": "Алёховщина",
        "coords": [
            68741.08,
            -62768.01
        ],
        "region": "EU",
        "companies": []
    },
    "apatity": {
        "name": "Апатиты",
        "coords": [
            60257.51,
            -101063.1
        ],
        "region": "EU",
        "companies": []
    },
    "babruysk": {
        "name": "Бабруйск",
        "coords": [
            64394.4,
            -18096.8
        ],
        "region": "EU",
        "companies": []
    },
    "baranovichi": {
        "name": "Баранавічы",
        "coords": [
            54554.7,
            -16169.5
        ],
        "region": "EU",
        "companies": []
    },
    "belcity": {
        "name": "Бeлгoрoд",
        "coords": [
            92763.64,
            -10593.0
        ],
        "region": "EU",
        "companies": []
    },
    "boksitogorsk": {
        "name": "Бокситогорск",
        "coords": [
            74143.42,
            -57093.29
        ],
        "region": "EU",
        "companies": []
    },
    "borisoglebsk": {
        "name": "Борисоглебск",
        "coords": [
            112287.0,
            -21003.7
        ],
        "region": "EU",
        "companies": []
    },
    "brect": {
        "name": "Брэст",
        "coords": [
            46698.6,
            -9542.98
        ],
        "region": "EU",
        "companies": []
    },
    "bryansk": {
        "name": "Брянск",
        "coords": [
            82100.0,
            -22682.4
        ],
        "region": "EU",
        "companies": []
    },
    "engels": {
        "name": "Энгельс",
        "coords": [
            126205.3,
            -27772.72
        ],
        "region": "EU",
        "companies": []
    },
    "glubokoe": {
        "name": "Глыбокае",
        "coords": [
            58649.91,
            -29033.44
        ],
        "region": "EU",
        "companies": []
    },
    "gomel": {
        "name": "Гомель",
        "coords": [
            71456.1,
            -15102.4
        ],
        "region": "EU",
        "companies": []
    },
    "grodno": {
        "name": "Гродна",
        "coords": [
            47055.7,
            -18098.4
        ],
        "region": "EU",
        "companies": []
    },
    "kaluga": {
        "name": "Калуга",
        "coords": [
            86328.6,
            -31348.2
        ],
        "region": "EU",
        "companies": []
    },
    "kandalrm": {
        "name": "Кандалакша",
        "coords": [
            57059.25,
            -97006.81
        ],
        "region": "EU",
        "companies": []
    },
    "kem": {
        "name": "Кемь",
        "coords": [
            66736.8,
            -89467.5
        ],
        "region": "EU",
        "companies": []
    },
    "khimki": {
        "name": "Химки",
        "coords": [
            87717.91,
            -41049.2
        ],
        "region": "EU",
        "companies": []
    },
    "kholm": {
        "name": "Холм",
        "coords": [
            67228.7,
            -42842.4
        ],
        "region": "EU",
        "companies": []
    },
    "kingisepp": {
        "name": "Кингисепп",
        "coords": [
            55841.82,
            -52838.75
        ],
        "region": "EU",
        "companies": []
    },
    "kirishi": {
        "name": "Кириши",
        "coords": [
            67675.27,
            -56666.77
        ],
        "region": "EU",
        "companies": []
    },
    "kirovsk": {
        "name": "Кировск",
        "coords": [
            64341.34,
            -57445.91
        ],
        "region": "EU",
        "companies": []
    },
    "klin": {
        "name": "Клин",
        "coords": [
            84401.6,
            -42236.8
        ],
        "region": "EU",
        "companies": []
    },
    "kola": {
        "name": "Кола",
        "coords": [
            51681.66,
            -108565.9
        ],
        "region": "EU",
        "companies": []
    },
    "kolomna": {
        "name": "Коломна",
        "coords": [
            92995.8,
            -38100.1
        ],
        "region": "EU",
        "companies": []
    },
    "kolpino": {
        "name": "Колпино",
        "coords": [
            62728.22,
            -55253.77
        ],
        "region": "EU",
        "companies": []
    },
    "krasnoslob": {
        "name": "Краснослободск",
        "coords": [
            125747.5,
            -10103.79
        ],
        "region": "EU",
        "companies": []
    },
    "kursk": {
        "name": "Курск",
        "coords": [
            91396.1,
            -16073.8
        ],
        "region": "EU",
        "companies": []
    },
    "lida": {
        "name": "Ліда",
        "coords": [
            50463.5,
            -20712.3
        ],
        "region": "EU",
        "companies": []
    },
    "luki": {
        "name": "Великие Луки",
        "coords": [
            65110.6,
            -37441.8
        ],
        "region": "EU",
        "companies": []
    },
    "medved": {
        "name": "Медвежьегорск",
        "coords": [
            67868.83,
            -78117.56
        ],
        "region": "EU",
        "companies": []
    },
    "minsk": {
        "name": "Мінск",
        "coords": [
            58358.6,
            -22095.2
        ],
        "region": "EU",
        "companies": []
    },
    "mogilev": {
        "name": "Магілёў",
        "coords": [
            67307.6,
            -23216.2
        ],
        "region": "EU",
        "companies": []
    },
    "moncheg": {
        "name": "Мончегорск",
        "coords": [
            56111.91,
            -102972.0
        ],
        "region": "EU",
        "companies": []
    },
    "moscow": {
        "name": "Москва",
        "coords": [
            89644.41,
            -39792.41
        ],
        "region": "EU",
        "companies": []
    },
    "mozir": {
        "name": "Мазыр",
        "coords": [
            65983.0,
            -12548.9
        ],
        "region": "EU",
        "companies": []
    },
    "mstislavl": {
        "name": "Мсціслаў",
        "coords": [
            71206.8,
            -26136.8
        ],
        "region": "EU",
        "companies": []
    },
    "murmansk": {
        "name": "Мурманск",
        "coords": [
            53529.6,
            -110057.0
        ],
        "region": "EU",
        "companies": []
    },
    "nevel": {
        "name": "Невель",
        "coords": [
            63689.5,
            -35678.8
        ],
        "region": "EU",
        "companies": []
    },
    "nikolskoye": {
        "name": "Никольское",
        "coords": [
            106544.6,
            -38967.73
        ],
        "region": "EU",
        "companies": []
    },
    "novgorod": {
        "name": "Великий Новгород",
        "coords": [
            65052.4,
            -49111.5
        ],
        "region": "EU",
        "companies": []
    },
    "obninsk": {
        "name": "Обнинск",
        "coords": [
            85332.9,
            -35073.1
        ],
        "region": "EU",
        "companies": []
    },
    "oboyan": {
        "name": "Обоянь",
        "coords": [
            91077.0,
            -13813.0
        ],
        "region": "EU",
        "companies": []
    },
    "orel": {
        "name": "Орел",
        "coords": [
            87658.2,
            -23228.0
        ],
        "region": "EU",
        "companies": []
    },
    "orsha": {
        "name": "Орша",
        "coords": [
            67891.2,
            -26320.7
        ],
        "region": "EU",
        "companies": []
    },
    "ostashkov": {
        "name": "Осташков",
        "coords": [
            71691.7,
            -44016.8
        ],
        "region": "EU",
        "companies": []
    },
    "penza": {
        "name": "Пенза",
        "coords": [
            116891.6,
            -36117.17
        ],
        "region": "EU",
        "companies": []
    },
    "petersburg": {
        "name": "Санкт-Петербург",
        "coords": [
            59773.8,
            -57040.6
        ],
        "region": "EU",
        "companies": []
    },
    "petrozavodsk": {
        "name": "Петрозаводск",
        "coords": [
            66815.9,
            -70284.8
        ],
        "region": "EU",
        "companies": []
    },
    "pikalevo": {
        "name": "Пикалёво",
        "coords": [
            75280.78,
            -58081.39
        ],
        "region": "EU",
        "companies": []
    },
    "pinsk": {
        "name": "Пінск",
        "coords": [
            55678.1,
            -10592.7
        ],
        "region": "EU",
        "companies": []
    },
    "pole": {
        "name": "Лодейное Поле",
        "coords": [
            66287.48,
            -64918.8
        ],
        "region": "EU",
        "companies": []
    },
    "polotsk": {
        "name": "Полацк",
        "coords": [
            61905.28,
            -31507.19
        ],
        "region": "EU",
        "companies": []
    },
    "porkhov": {
        "name": "Порхов",
        "coords": [
            60948.5,
            -44020.6
        ],
        "region": "EU",
        "companies": []
    },
    "priozersk": {
        "name": "Приозерск",
        "coords": [
            56847.34,
            -63403.49
        ],
        "region": "EU",
        "companies": []
    },
    "razmetelevo": {
        "name": "Разметелево",
        "coords": [
            62858.83,
            -57694.02
        ],
        "region": "EU",
        "companies": []
    },
    "rgev": {
        "name": "Ржев",
        "coords": [
            77040.4,
            -39807.6
        ],
        "region": "EU",
        "companies": []
    },
    "roslavl": {
        "name": "Рославль",
        "coords": [
            77169.5,
            -25261.4
        ],
        "region": "EU",
        "companies": []
    },
    "saratov": {
        "name": "Саратов",
        "coords": [
            122162.3,
            -28779.4
        ],
        "region": "EU",
        "companies": []
    },
    "segezha": {
        "name": "Сегежа",
        "coords": [
            68648.11,
            -82188.78
        ],
        "region": "EU",
        "companies": []
    },
    "shatsk": {
        "name": "Шацк",
        "coords": [
            102748.0,
            -36572.32
        ],
        "region": "EU",
        "companies": []
    },
    "shlisselburg": {
        "name": "Шлиссельбург",
        "coords": [
            64110.6,
            -59343.8
        ],
        "region": "EU",
        "companies": []
    },
    "slonim": {
        "name": "Слонім",
        "coords": [
            51384.8,
            -16056.8
        ],
        "region": "EU",
        "companies": []
    },
    "sluck": {
        "name": "Слуцк",
        "coords": [
            59477.4,
            -16285.8
        ],
        "region": "EU",
        "companies": []
    },
    "smolensk": {
        "name": "Смоленск",
        "coords": [
            73118.6,
            -29374.4
        ],
        "region": "EU",
        "companies": []
    },
    "sortavala": {
        "name": "Сортавала",
        "coords": [
            58194.97,
            -66991.86
        ],
        "region": "EU",
        "companies": []
    },
    "stroitel": {
        "name": "Строитель",
        "coords": [
            92030.14,
            -11600.88
        ],
        "region": "EU",
        "companies": []
    },
    "suoyarvi": {
        "name": "Суоярви",
        "coords": [
            62996.3,
            -73603.1
        ],
        "region": "EU",
        "companies": []
    },
    "tambov": {
        "name": "Тамбов",
        "coords": [
            107369.0,
            -28733.2
        ],
        "region": "EU",
        "companies": []
    },
    "tihvin": {
        "name": "Тихвин",
        "coords": [
            69854.91,
            -58391.98
        ],
        "region": "EU",
        "companies": []
    },
    "tosno": {
        "name": "Тосно",
        "coords": [
            63880.8,
            -54082.9
        ],
        "region": "EU",
        "companies": []
    },
    "tula": {
        "name": "Тула",
        "coords": [
            91217.5,
            -32713.7
        ],
        "region": "EU",
        "companies": []
    },
    "tver": {
        "name": "Тверь",
        "coords": [
            81110.4,
            -43874.4
        ],
        "region": "EU",
        "companies": []
    },
    "valday": {
        "name": "Валдай",
        "coords": [
            70492.6,
            -49050.0
        ],
        "region": "EU",
        "companies": []
    },
    "velig": {
        "name": "Велиж",
        "coords": [
            68466.5,
            -34541.6
        ],
        "region": "EU",
        "companies": []
    },
    "vinnicy": {
        "name": "Винницы",
        "coords": [
            71575.91,
            -64179.57
        ],
        "region": "EU",
        "companies": []
    },
    "vitebsk": {
        "name": "Віцебск",
        "coords": [
            65397.11,
            -32575.59
        ],
        "region": "EU",
        "companies": []
    },
    "vitino": {
        "name": "Витино",
        "coords": [
            57669.54,
            -95417.22
        ],
        "region": "EU",
        "companies": []
    },
    "volgograd": {
        "name": "Волгоград",
        "coords": [
            123820.7,
            -12510.52
        ],
        "region": "EU",
        "companies": []
    },
    "volhov": {
        "name": "Волхов",
        "coords": [
            65984.48,
            -58614.18
        ],
        "region": "EU",
        "companies": []
    },
    "volkovysk": {
        "name": "Ваўкавыск",
        "coords": [
            49939.8,
            -15854.0
        ],
        "region": "EU",
        "companies": []
    },
    "volochyok": {
        "name": "Вышний Волочек",
        "coords": [
            75473.5,
            -46654.9
        ],
        "region": "EU",
        "companies": []
    },
    "volokolamsk": {
        "name": "Волоколамск",
        "coords": [
            82679.4,
            -40014.5
        ],
        "region": "EU",
        "companies": []
    },
    "volzhskiy": {
        "name": "Волжский",
        "coords": [
            126208.8,
            -13839.17
        ],
        "region": "EU",
        "companies": []
    },
    "voronezh": {
        "name": "Воронеж",
        "coords": [
            102488.0,
            -19897.4
        ],
        "region": "EU",
        "companies": []
    },
    "vyazma": {
        "name": "Вязьма",
        "coords": [
            78418.8,
            -33964.8
        ],
        "region": "EU",
        "companies": []
    },
    "yukhnov": {
        "name": "Юхнов",
        "coords": [
            80491.7,
            -30929.9
        ],
        "region": "EU",
        "companies": []
    },
    "zelenoborsky": {
        "name": "Зеленоборский",
        "coords": [
            57769.43,
            -92496.91
        ],
        "region": "EU",
        "companies": []
    },
    "alban": {
        "name": "Saint-Alban-du-Rhône",
        "coords": [
            -25953.6,
            28986.3
        ],
        "region": "EU",
        "companies": []
    },
    "bordeaux": {
        "name": "Bordeaux",
        "coords": [
            -46138.6,
            27274.4
        ],
        "region": "EU",
        "companies": []
    },
    "bourges": {
        "name": "Bourges",
        "coords": [
            -31951.8,
            16275.5
        ],
        "region": "EU",
        "companies": []
    },
    "brest": {
        "name": "Brest",
        "coords": [
            -56771.4,
            3869.3
        ],
        "region": "EU",
        "companies": []
    },
    "civaux": {
        "name": "Civaux",
        "coords": [
            -39029.7,
            18292.0
        ],
        "region": "EU",
        "companies": []
    },
    "golfech": {
        "name": "Golfech",
        "coords": [
            -40395.4,
            31472.6
        ],
        "region": "EU",
        "companies": []
    },
    "larochelle": {
        "name": "La Rochelle",
        "coords": [
            -46575.7,
            19532.5
        ],
        "region": "EU",
        "companies": []
    },
    "laurent": {
        "name": "Saint-Laurent",
        "coords": [
            -35649.6,
            13817.4
        ],
        "region": "EU",
        "companies": []
    },
    "lehavre": {
        "name": "Le Havre",
        "coords": [
            -37894.2,
            1515.48
        ],
        "region": "EU",
        "companies": []
    },
    "lemans": {
        "name": "Le Mans",
        "coords": [
            -39749.7,
            9718.43
        ],
        "region": "EU",
        "companies": []
    },
    "limoges": {
        "name": "Limoges",
        "coords": [
            -37417.3,
            23632.0
        ],
        "region": "EU",
        "companies": []
    },
    "marseille": {
        "name": "Marseille",
        "coords": [
            -23472.4,
            39210.8
        ],
        "region": "EU",
        "companies": []
    },
    "montpellier": {
        "name": "Montpellier",
        "coords": [
            -30052.4,
            36127.6
        ],
        "region": "EU",
        "companies": []
    },
    "nantes": {
        "name": "Nantes",
        "coords": [
            -47170.9,
            13162.0
        ],
        "region": "EU",
        "companies": []
    },
    "nice": {
        "name": "Nice",
        "coords": [
            -15520.4,
            38206.2
        ],
        "region": "EU",
        "companies": []
    },
    "paluel": {
        "name": "Paluel",
        "coords": [
            -33608.1,
            224.902
        ],
        "region": "EU",
        "companies": []
    },
    "rennes": {
        "name": "Rennes",
        "coords": [
            -46539.8,
            8064.61
        ],
        "region": "EU",
        "companies": []
    },
    "roscoff": {
        "name": "Roscoff",
        "coords": [
            -53697.9,
            3120.41
        ],
        "region": "EU",
        "companies": []
    },
    "toulouse": {
        "name": "Toulouse",
        "coords": [
            -39213.8,
            35665.6
        ],
        "region": "EU",
        "companies": []
    },
    "ajaccio": {
        "name": "Ajaccio",
        "coords": [
            -10031.5,
            48620.9
        ],
        "region": "EU",
        "companies": []
    },
    "bastia": {
        "name": "Bastia",
        "coords": [
            -7139.55,
            44186.3
        ],
        "region": "EU",
        "companies": []
    },
    "bonifacio": {
        "name": "Bonifacio",
        "coords": [
            -8469.77,
            52254.9
        ],
        "region": "EU",
        "companies": []
    },
    "calvi": {
        "name": "Calvi",
        "coords": [
            -10035.8,
            46017.5
        ],
        "region": "EU",
        "companies": []
    },
    "lile": {
        "name": "L'Île-Rousse",
        "coords": [
            -8914.71,
            44676.3
        ],
        "region": "EU",
        "companies": []
    },
    "porto": {
        "name": "Porto",
        "coords": [
            -85324.7,
            39550.9
        ],
        "region": "EU",
        "companies": []
    },
    "daugavpils": {
        "name": "Daugavpils",
        "coords": [
            53075.4,
            -31905.7
        ],
        "region": "EU",
        "companies": []
    },
    "helsinki": {
        "name": "Helsinki",
        "coords": [
            44945.4,
            -55691.5
        ],
        "region": "EU",
        "companies": []
    },
    "kaliningrad": {
        "name": "Калининград",
        "coords": [
            34365.2,
            -23181.4
        ],
        "region": "EU",
        "companies": []
    },
    "kaunas": {
        "name": "Kaunas",
        "coords": [
            45564.0,
            -25347.7
        ],
        "region": "EU",
        "companies": []
    },
    "klaipeda": {
        "name": "Klaipėda",
        "coords": [
            36342.8,
            -28719.6
        ],
        "region": "EU",
        "companies": []
    },
    "kotka": {
        "name": "Kotka",
        "coords": [
            50245.1,
            -58045.7
        ],
        "region": "EU",
        "companies": []
    },
    "kouvola": {
        "name": "Kouvola",
        "coords": [
            48776.3,
            -60408.9
        ],
        "region": "EU",
        "companies": []
    },
    "kunda": {
        "name": "Kunda",
        "coords": [
            49785.3,
            -52304.7
        ],
        "region": "EU",
        "companies": []
    },
    "lahti": {
        "name": "Lahti",
        "coords": [
            45529.8,
            -60557.0
        ],
        "region": "EU",
        "companies": []
    },
    "loviisa": {
        "name": "Loviisa",
        "coords": [
            47717.4,
            -57187.8
        ],
        "region": "EU",
        "companies": []
    },
    "luga": {
        "name": "Луга",
        "coords": [
            60046.5,
            -50045.2
        ],
        "region": "EU",
        "companies": []
    },
    "mazeikiai": {
        "name": "Mažeikiai",
        "coords": [
            39434.4,
            -32809.6
        ],
        "region": "EU",
        "companies": []
    },
    "naantali": {
        "name": "Naantali",
        "coords": [
            35110.2,
            -56362.4
        ],
        "region": "EU",
        "companies": []
    },
    "narva": {
        "name": "Narva",
        "coords": [
            54382.2,
            -52462.3
        ],
        "region": "EU",
        "companies": []
    },
    "naujieji": {
        "name": "Naujieji Valkininkai",
        "coords": [
            47940.6,
            -21636.4
        ],
        "region": "EU",
        "companies": []
    },
    "olkiluoto": {
        "name": "Olkiluoto",
        "coords": [
            34255.3,
            -60008.2
        ],
        "region": "EU",
        "companies": []
    },
    "paldiski": {
        "name": "Paldiski",
        "coords": [
            42570.0,
            -50011.9
        ],
        "region": "EU",
        "companies": []
    },
    "panevezys": {
        "name": "Panevėžys",
        "coords": [
            46202.3,
            -29962.8
        ],
        "region": "EU",
        "companies": []
    },
    "parnu": {
        "name": "Pärnu",
        "coords": [
            44626.8,
            -45237.7
        ],
        "region": "EU",
        "companies": []
    },
    "passau": {
        "name": "Passau",
        "coords": [
            9075.84,
            8564.5
        ],
        "region": "EU",
        "companies": []
    },
    "pori": {
        "name": "Pori",
        "coords": [
            34862.3,
            -61707.6
        ],
        "region": "EU",
        "companies": []
    },
    "pskov": {
        "name": "Псков",
        "coords": [
            56968.3,
            -44002.4
        ],
        "region": "EU",
        "companies": []
    },
    "rezekne": {
        "name": "Rēzekne",
        "coords": [
            54953.4,
            -36075.6
        ],
        "region": "EU",
        "companies": []
    },
    "riga": {
        "name": "Rīga",
        "coords": [
            44678.0,
            -37089.7
        ],
        "region": "EU",
        "companies": []
    },
    "siauliai": {
        "name": "Šiauliai",
        "coords": [
            43188.8,
            -30503.8
        ],
        "region": "EU",
        "companies": []
    },
    "sosnovy": {
        "name": "Сосновый Бор",
        "coords": [
            54949.1,
            -54394.3
        ],
        "region": "EU",
        "companies": []
    },
    "tallinn": {
        "name": "Tallinn",
        "coords": [
            44388.5,
            -50868.6
        ],
        "region": "EU",
        "companies": []
    },
    "tampere": {
        "name": "Tampere",
        "coords": [
            40238.8,
            -62490.7
        ],
        "region": "EU",
        "companies": []
    },
    "tartu": {
        "name": "Tartu",
        "coords": [
            50958.0,
            -46408.0
        ],
        "region": "EU",
        "companies": []
    },
    "turku": {
        "name": "Turku",
        "coords": [
            36697.8,
            -56006.0
        ],
        "region": "EU",
        "companies": []
    },
    "utena": {
        "name": "Utena",
        "coords": [
            50778.2,
            -29540.4
        ],
        "region": "EU",
        "companies": []
    },
    "valmiera": {
        "name": "Valmiera",
        "coords": [
            47973.1,
            -40783.7
        ],
        "region": "EU",
        "companies": []
    },
    "ventspils": {
        "name": "Ventspils",
        "coords": [
            36679.7,
            -38562.0
        ],
        "region": "EU",
        "companies": []
    },
    "vilnius": {
        "name": "Vilnius",
        "coords": [
            50562.6,
            -24885.7
        ],
        "region": "EU",
        "companies": []
    },
    "vyborg": {
        "name": "Выборг",
        "coords": [
            54465.3,
            -60221.8
        ],
        "region": "EU",
        "companies": []
    },
    "brasov": {
        "name": "Brașov",
        "coords": [
            58252.4,
            23552.8
        ],
        "region": "EU",
        "companies": []
    },
    "burgas": {
        "name": "Бургас",
        "coords": [
            68297.2,
            40880.7
        ],
        "region": "EU",
        "companies": []
    },
    "calarasi": {
        "name": "Călărași",
        "coords": [
            66074.6,
            31257.8
        ],
        "region": "EU",
        "companies": []
    },
    "cernavoda": {
        "name": "Cernavodă",
        "coords": [
            69579.5,
            30015.4
        ],
        "region": "EU",
        "companies": []
    },
    "edirne": {
        "name": "Edirne",
        "coords": [
            65624.3,
            48003.5
        ],
        "region": "EU",
        "companies": []
    },
    "galati": {
        "name": "Galați",
        "coords": [
            67046.2,
            24473.0
        ],
        "region": "EU",
        "companies": []
    },
    "hunedoara": {
        "name": "Hunedoara",
        "coords": [
            49016.9,
            26114.8
        ],
        "region": "EU",
        "companies": []
    },
    "iasi": {
        "name": "Iași",
        "coords": [
            64746.4,
            14963.9
        ],
        "region": "EU",
        "companies": []
    },
    "istanbul": {
        "name": "Istanbul",
        "coords": [
            76690.4,
            49416.7
        ],
        "region": "EU",
        "companies": []
    },
    "karlovo": {
        "name": "Карлово",
        "coords": [
            58056.4,
            42057.7
        ],
        "region": "EU",
        "companies": []
    },
    "kozloduy": {
        "name": "Козлодуй",
        "coords": [
            52658.2,
            36247.3
        ],
        "region": "EU",
        "companies": []
    },
    "mangalia": {
        "name": "Mangalia",
        "coords": [
            71577.7,
            33330.9
        ],
        "region": "EU",
        "companies": []
    },
    "pernik": {
        "name": "Перник",
        "coords": [
            48351.3,
            45310.5
        ],
        "region": "EU",
        "companies": []
    },
    "pirdop": {
        "name": "Пирдоп",
        "coords": [
            55937.9,
            42161.1
        ],
        "region": "EU",
        "companies": []
    },
    "pitesti": {
        "name": "Pitești",
        "coords": [
            56247.5,
            29912.5
        ],
        "region": "EU",
        "companies": []
    },
    "pleven": {
        "name": "Плевен (Pleven)",
        "coords": [
            57288.6,
            38731.3
        ],
        "region": "EU",
        "companies": []
    },
    "plovdiv": {
        "name": "Пловдив",
        "coords": [
            58234.8,
            46169.4
        ],
        "region": "EU",
        "companies": []
    },
    "resita": {
        "name": "Reșița",
        "coords": [
            43990.4,
            29154.6
        ],
        "region": "EU",
        "companies": []
    },
    "ruse": {
        "name": "Русе",
        "coords": [
            61454.0,
            35069.8
        ],
        "region": "EU",
        "companies": []
    },
    "schumen": {
        "name": "Шумен",
        "coords": [
            65001.3,
            36977.8
        ],
        "region": "EU",
        "companies": []
    },
    "sofia": {
        "name": "Со́фия",
        "coords": [
            51154.8,
            42490.6
        ],
        "region": "EU",
        "companies": []
    },
    "targu": {
        "name": "Târgu Mureș",
        "coords": [
            53959.7,
            20157.2
        ],
        "region": "EU",
        "companies": []
    },
    "tekirdag": {
        "name": "Tekirdag",
        "coords": [
            65903.9,
            52521.5
        ],
        "region": "EU",
        "companies": []
    },
    "varna": {
        "name": "Варна",
        "coords": [
            70143.4,
            36462.2
        ],
        "region": "EU",
        "companies": []
    },
    "veli": {
        "name": "Велико Търново",
        "coords": [
            60763.4,
            38859.5
        ],
        "region": "EU",
        "companies": []
    },
    "yambol": {
        "name": "Ямбол",
        "coords": [
            64390.54,
            42209.35
        ],
        "region": "EU",
        "companies": []
    },
    "adugeysk": {
        "name": "Адыгейск",
        "coords": [
            114837.0,
            17051.7
        ],
        "region": "EU",
        "companies": []
    },
    "aksai": {
        "name": "Аксай",
        "coords": [
            110815.0,
            494.762
        ],
        "region": "EU",
        "companies": []
    },
    "anapa": {
        "name": "Анапа",
        "coords": [
            103611.0,
            19799.3
        ],
        "region": "EU",
        "companies": []
    },
    "apsheronsk": {
        "name": "Апшеронск",
        "coords": [
            120064.0,
            18103.5
        ],
        "region": "EU",
        "companies": []
    },
    "armavir": {
        "name": "Армавир",
        "coords": [
            123337.0,
            12819.1
        ],
        "region": "EU",
        "companies": []
    },
    "ashe": {
        "name": "Аше",
        "coords": [
            118882.0,
            24433.9
        ],
        "region": "EU",
        "companies": []
    },
    "b": {
        "name": "Белая Калитва",
        "coords": [
            112562.0,
            -2447.66
        ],
        "region": "EU",
        "companies": []
    },
    "belorechensk": {
        "name": "Белореченск",
        "coords": [
            119969.0,
            16180.8
        ],
        "region": "EU",
        "companies": []
    },
    "cherkessk": {
        "name": "Черкесск",
        "coords": [
            128038.0,
            15938.1
        ],
        "region": "EU",
        "companies": []
    },
    "chinary": {
        "name": "Чинары",
        "coords": [
            116938.0,
            19920.7
        ],
        "region": "EU",
        "companies": []
    },
    "dahovskaya": {
        "name": "Даховская",
        "coords": [
            122965.0,
            19703.3
        ],
        "region": "EU",
        "companies": []
    },
    "dombai": {
        "name": "Домбай",
        "coords": [
            126040.0,
            22560.9
        ],
        "region": "EU",
        "companies": []
    },
    "dshubga": {
        "name": "Джубга",
        "coords": [
            112083.0,
            21924.9
        ],
        "region": "EU",
        "companies": []
    },
    "egorlik": {
        "name": "Егорлыкская",
        "coords": [
            122341.0,
            4648.5
        ],
        "region": "EU",
        "companies": []
    },
    "eisk": {
        "name": "Ейск",
        "coords": [
            106086.0,
            9614.21
        ],
        "region": "EU",
        "companies": []
    },
    "enem": {
        "name": "Энем",
        "coords": [
            111346.0,
            17508.4
        ],
        "region": "EU",
        "companies": []
    },
    "gagra": {
        "name": "გაგრა",
        "coords": [
            120667.0,
            24969.09
        ],
        "region": "EU",
        "companies": []
    },
    "gali": {
        "name": "გალი",
        "coords": [
            127245.4,
            25864.04
        ],
        "region": "EU",
        "companies": []
    },
    "gelendshik": {
        "name": "Геленджик",
        "coords": [
            109179.0,
            20453.8
        ],
        "region": "EU",
        "companies": []
    },
    "gorkluch": {
        "name": "Горячий Ключ",
        "coords": [
            113313.0,
            18654.4
        ],
        "region": "EU",
        "companies": []
    },
    "guamka": {
        "name": "Гуамка",
        "coords": [
            120395.0,
            21029.6
        ],
        "region": "EU",
        "companies": []
    },
    "gudauta": {
        "name": "გუდაუთა",
        "coords": [
            122975.6,
            24720.8
        ],
        "region": "EU",
        "companies": []
    },
    "guzeripl": {
        "name": "Гузерипль",
        "coords": [
            123566.0,
            22255.6
        ],
        "region": "EU",
        "companies": []
    },
    "haduzhensk": {
        "name": "Хадыженск",
        "coords": [
            119311.0,
            18461.5
        ],
        "region": "EU",
        "companies": []
    },
    "hadzhico": {
        "name": "Хаджико",
        "coords": [
            119524.0,
            23160.9
        ],
        "region": "EU",
        "companies": []
    },
    "kagalnik": {
        "name": "Кагальницкая",
        "coords": [
            117857.0,
            5278.2
        ],
        "region": "EU",
        "companies": []
    },
    "kamenomost": {
        "name": "Каменномостский",
        "coords": [
            122698.0,
            18734.0
        ],
        "region": "EU",
        "companies": []
    },
    "kamensk": {
        "name": "Каменск-Шахтинский",
        "coords": [
            110355.0,
            -3140.31
        ],
        "region": "EU",
        "companies": []
    },
    "karachaevsk": {
        "name": "Карачаевск",
        "coords": [
            127712.0,
            19190.6
        ],
        "region": "EU",
        "companies": []
    },
    "kirov": {
        "name": "Киров",
        "coords": [
            112940.5,
            -68335.58
        ],
        "region": "EU",
        "companies": []
    },
    "korenovsk": {
        "name": "Кореновск",
        "coords": [
            114597.0,
            12165.9
        ],
        "region": "EU",
        "companies": []
    },
    "krasn": {
        "name": "Красногвардейское",
        "coords": [
            126658.0,
            7217.68
        ],
        "region": "EU",
        "companies": []
    },
    "krasnodar": {
        "name": "Краснодар",
        "coords": [
            112672.0,
            14746.1
        ],
        "region": "EU",
        "companies": []
    },
    "krimsk": {
        "name": "Крымск",
        "coords": [
            107760.0,
            17712.4
        ],
        "region": "EU",
        "companies": []
    },
    "kropotkin": {
        "name": "Кропоткин",
        "coords": [
            120585.0,
            11550.6
        ],
        "region": "EU",
        "companies": []
    },
    "kushevskaya": {
        "name": "Кущёвская",
        "coords": [
            112872.0,
            7272.83
        ],
        "region": "EU",
        "companies": []
    },
    "lazarevskoe": {
        "name": "Лазаревское",
        "coords": [
            120313.0,
            24516.4
        ],
        "region": "EU",
        "companies": []
    },
    "lerwick": {
        "name": "Lerwick",
        "coords": [
            -30340.71,
            -75768.77
        ],
        "region": "EU",
        "companies": []
    },
    "mamedovashel": {
        "name": "Мамедова Щель",
        "coords": [
            120105.0,
            23865.2
        ],
        "region": "EU",
        "companies": []
    },
    "maykop": {
        "name": "Майкоп",
        "coords": [
            121732.0,
            16914.4
        ],
        "region": "EU",
        "companies": []
    },
    "morozovsk": {
        "name": "Морозовск",
        "coords": [
            115640.0,
            -3966.79
        ],
        "region": "EU",
        "companies": []
    },
    "nadzhigo": {
        "name": "Наджиго",
        "coords": [
            118134.0,
            23115.8
        ],
        "region": "EU",
        "companies": []
    },
    "nevinnomyssk": {
        "name": "Невинномысск",
        "coords": [
            128374.0,
            14641.5
        ],
        "region": "EU",
        "companies": []
    },
    "nizhegorod": {
        "name": "Нижегородская",
        "coords": [
            120984.0,
            19727.7
        ],
        "region": "EU",
        "companies": []
    },
    "nov": {
        "name": "Новопокровская",
        "coords": [
            120243.0,
            7770.38
        ],
        "region": "EU",
        "companies": []
    },
    "novoa": {
        "name": "Новоалександровск",
        "coords": [
            126234.0,
            9044.26
        ],
        "region": "EU",
        "companies": []
    },
    "novorossiysk": {
        "name": "Новороссийск",
        "coords": [
            106610.0,
            19800.8
        ],
        "region": "EU",
        "companies": []
    },
    "ochamchire": {
        "name": "ოჩამჩირის",
        "coords": [
            125603.3,
            25819.69
        ],
        "region": "EU",
        "companies": []
    },
    "pavlovsk": {
        "name": "Павловск",
        "coords": [
            106221.0,
            -14277.3
        ],
        "region": "EU",
        "companies": []
    },
    "pavlovskya": {
        "name": "Павловская",
        "coords": [
            114214.0,
            9594.3
        ],
        "region": "EU",
        "companies": []
    },
    "rostov": {
        "name": "Ростов",
        "coords": [
            90248.06,
            -50973.56
        ],
        "region": "EU",
        "companies": []
    },
    "sem": {
        "name": "Семикаракорск",
        "coords": [
            116272.0,
            -520.988
        ],
        "region": "EU",
        "companies": []
    },
    "shabanovskoe": {
        "name": "Шабановское",
        "coords": [
            111488.0,
            19540.9
        ],
        "region": "EU",
        "companies": []
    },
    "shaumyan": {
        "name": "Перевал Шаумянский",
        "coords": [
            118048.0,
            20409.8
        ],
        "region": "EU",
        "companies": []
    },
    "shepsi": {
        "name": "Шепси",
        "coords": [
            116852.0,
            23959.5
        ],
        "region": "EU",
        "companies": []
    },
    "slavyansk": {
        "name": "Славянск-на-Кубани",
        "coords": [
            107653.0,
            15241.4
        ],
        "region": "EU",
        "companies": []
    },
    "sokhum": {
        "name": "სოხუმი",
        "coords": [
            124208.3,
            25324.68
        ],
        "region": "EU",
        "companies": []
    },
    "sovkvadje": {
        "name": "Совет-Квадже",
        "coords": [
            117540.0,
            24364.1
        ],
        "region": "EU",
        "companies": []
    },
    "staromin": {
        "name": "Староминская",
        "coords": [
            109370.0,
            7574.92
        ],
        "region": "EU",
        "companies": []
    },
    "stavropol": {
        "name": "Ставрополь",
        "coords": [
            129205.0,
            9584.94
        ],
        "region": "EU",
        "companies": []
    },
    "teberda": {
        "name": "Теберда",
        "coords": [
            127258.0,
            20847.7
        ],
        "region": "EU",
        "companies": []
    },
    "ticoreck": {
        "name": "Тихорецк",
        "coords": [
            116730.0,
            10284.6
        ],
        "region": "EU",
        "companies": []
    },
    "timashevsk": {
        "name": "Тимашевск",
        "coords": [
            110896.0,
            12663.0
        ],
        "region": "EU",
        "companies": []
    },
    "tuapse": {
        "name": "Туапсе",
        "coords": [
            116070.0,
            22453.9
        ],
        "region": "EU",
        "companies": []
    },
    "ust": {
        "name": "Усть-Уса",
        "coords": [
            110550.1,
            -112383.7
        ],
        "region": "EU",
        "companies": []
    },
    "ustdjeguta": {
        "name": "Усть-Джегута",
        "coords": [
            128096.0,
            16823.1
        ],
        "region": "EU",
        "companies": []
    },
    "verhnebak": {
        "name": "Верхнебаканский",
        "coords": [
            105965.0,
            18703.5
        ],
        "region": "EU",
        "companies": []
    },
    "jvari": {
        "name": "ჯვარი",
        "coords": [
            128468.9,
            23542.18
        ],
        "region": "EU",
        "companies": []
    },
    "khaishi": {
        "name": "ხაიში",
        "coords": [
            128292.8,
            22248.4
        ],
        "region": "EU",
        "companies": []
    },
    "zugdidi": {
        "name": "ზუგდიდი",
        "coords": [
            128726.8,
            25476.98
        ],
        "region": "EU",
        "companies": []
    },
    "aberystwyth": {
        "name": "Aberystwyth",
        "coords": [
            -56093.8,
            -22086.8
        ],
        "region": "EU",
        "companies": []
    },
    "grumantbyen": {
        "name": "Grumantbyen",
        "coords": [
            17790.41,
            -161440.2
        ],
        "region": "EU",
        "companies": []
    },
    "jaca": {
        "name": "Jaca",
        "coords": [
            -48340.5,
            40521.8
        ],
        "region": "EU",
        "companies": []
    },
    "kalix": {
        "name": "Kalix",
        "coords": [
            35232.8,
            -86653.0
        ],
        "region": "EU",
        "companies": []
    },
    "larnaka": {
        "name": "Λάρνακα",
        "coords": [
            103263.0,
            77087.2
        ],
        "region": "EU",
        "companies": []
    },
    "lefkosia": {
        "name": "Λευκωσία",
        "coords": [
            101945.0,
            75661.0
        ],
        "region": "EU",
        "companies": []
    },
    "lemesos": {
        "name": "Λεμεσός",
        "coords": [
            100517.0,
            79269.4
        ],
        "region": "EU",
        "companies": []
    },
    "moerdijk": {
        "name": "Moerdijk",
        "coords": [
            -19855.5,
            -7533.8
        ],
        "region": "EU",
        "companies": []
    },
    "montana": {
        "name": "Монтана (Montana)",
        "coords": [
            50655.6,
            40189.5
        ],
        "region": "EU",
        "companies": []
    },
    "pafos": {
        "name": "Πάφος",
        "coords": [
            97732.6,
            79057.9
        ],
        "region": "EU",
        "companies": []
    },
    "pamplona": {
        "name": "Pamplona-Iruña",
        "coords": [
            -52500.4,
            38359.3
        ],
        "region": "EU",
        "companies": []
    },
    "porthmadog": {
        "name": "Porthmadog",
        "coords": [
            -55048.5,
            -26313.9
        ],
        "region": "EU",
        "companies": []
    },
    "soria": {
        "name": "Soria",
        "coords": [
            -58986.9,
            43033.8
        ],
        "region": "EU",
        "companies": []
    },
    "teruel": {
        "name": "Teruel",
        "coords": [
            -54139.6,
            52141.6
        ],
        "region": "EU",
        "companies": []
    },
    "ukmerge": {
        "name": "Ukmergė",
        "coords": [
            47637.1,
            -27394.4
        ],
        "region": "EU",
        "companies": []
    },
    "valencia": {
        "name": "Valencia",
        "coords": [
            -51181.4,
            58089.9
        ],
        "region": "EU",
        "companies": []
    },
    "vidin": {
        "name": "Видин (Vidin)",
        "coords": [
            48163.9,
            36115.1
        ],
        "region": "EU",
        "companies": []
    },
    "vinaros": {
        "name": "Vinaròs",
        "coords": [
            -46540.2,
            54007.8
        ],
        "region": "EU",
        "companies": []
    },
    "ystad": {
        "name": "Ystad",
        "coords": [
            13120.8,
            -26398.2
        ],
        "region": "EU",
        "companies": []
    },
    "zaragoza": {
        "name": "Zaragoza",
        "coords": [
            -51973.9,
            45516.3
        ],
        "region": "EU",
        "companies": []
    },
    "faaro": {
        "name": "Fårö",
        "coords": [
            30291.48,
            -40677.71
        ],
        "region": "EU",
        "companies": []
    },
    "gusev": {
        "name": "Гусев",
        "coords": [
            40194.3,
            -22661.2
        ],
        "region": "EU",
        "companies": []
    },
    "hawes": {
        "name": "Hawes",
        "coords": [
            -43473.4,
            -34247.8
        ],
        "region": "EU",
        "companies": []
    },
    "hoburg": {
        "name": "Hoburg",
        "coords": [
            27090.92,
            -35390.24
        ],
        "region": "EU",
        "companies": []
    },
    "ljugarn": {
        "name": "Ljugarn",
        "coords": [
            28080.7,
            -37363.0
        ],
        "region": "EU",
        "companies": []
    },
    "olomouc": {
        "name": "Olomouc",
        "coords": [
            25109.3,
            5928.35
        ],
        "region": "EU",
        "companies": []
    },
    "stornoway": {
        "name": "Stornoway",
        "coords": [
            -52991.7,
            -66994.5
        ],
        "region": "EU",
        "companies": []
    },
    "trnava": {
        "name": "Trnava",
        "coords": [
            26441.8,
            13133.2
        ],
        "region": "EU",
        "companies": []
    },
    "vasaros": {
        "name": "Vásárosnamény",
        "coords": [
            42627.0,
            13498.0
        ],
        "region": "EU",
        "companies": []
    },
    "visby": {
        "name": "Visby",
        "coords": [
            26564.0,
            -39164.1
        ],
        "region": "EU",
        "companies": []
    },
    "kappellskar": {
        "name": "Kappelskär",
        "coords": [
            28473.7,
            -51357.2
        ],
        "region": "EU",
        "companies": []
    },
    "hammerfest": {
        "name": "Hammerfest",
        "coords": [
            32017.0,
            -117025.0
        ],
        "region": "EU",
        "companies": []
    },
    "jihlava": {
        "name": "Jihlava",
        "coords": [
            18401.4,
            8814.57
        ],
        "region": "EU",
        "companies": []
    },
    "kandalaksha": {
        "name": "Кандалакша",
        "coords": [
            54976.9,
            -100226.0
        ],
        "region": "EU",
        "companies": []
    },
    "kirkenes": {
        "name": "Kirkenes",
        "coords": [
            44095.6,
            -113739.0
        ],
        "region": "EU",
        "companies": []
    },
    "kittila": {
        "name": "Kittilä",
        "coords": [
            38063.9,
            -97622.9
        ],
        "region": "EU",
        "companies": []
    },
    "nikel": {
        "name": "Никель",
        "coords": [
            45926.7,
            -109791.0
        ],
        "region": "EU",
        "companies": []
    },
    "satumare": {
        "name": "Satu Mare",
        "coords": [
            46031.3,
            15033.6
        ],
        "region": "EU",
        "companies": []
    },
    "sodankyla": {
        "name": "Sodankylä",
        "coords": [
            42257.3,
            -96694.4
        ],
        "region": "EU",
        "companies": []
    },
    "tanabru": {
        "name": "Tana bru",
        "coords": [
            40291.7,
            -114736.0
        ],
        "region": "EU",
        "companies": []
    },
    "utsjoki": {
        "name": "Utsjoki",
        "coords": [
            38931.0,
            -112825.0
        ],
        "region": "EU",
        "companies": []
    },
    "verkhnetulom": {
        "name": "Верхнетуломский",
        "coords": [
            50257.8,
            -106321.0
        ],
        "region": "EU",
        "companies": []
    },
    "anklam": {
        "name": "Anklam",
        "coords": [
            12357.3,
            -16805.98
        ],
        "region": "EU",
        "companies": []
    },
    "balivanich": {
        "name": "Balivanich",
        "coords": [
            -59010.39,
            -63254.07
        ],
        "region": "EU",
        "companies": []
    },
    "balti": {
        "name": "Bălţi",
        "coords": [
            66036.4,
            12143.2
        ],
        "region": "EU",
        "companies": []
    },
    "batumi": {
        "name": "Batumi",
        "coords": [
            132497.0,
            36298.7
        ],
        "region": "EU",
        "companies": []
    },
    "chelm": {
        "name": "Chełm",
        "coords": [
            46458.93,
            -4006.082
        ],
        "region": "EU",
        "companies": []
    },
    "chemnitz": {
        "name": "Chemnitz",
        "coords": [
            8381.26,
            196.84
        ],
        "region": "EU",
        "companies": []
    },
    "chisinau": {
        "name": "Chişinău",
        "coords": [
            70134.7,
            16235.3
        ],
        "region": "EU",
        "companies": []
    },
    "ciudadreal": {
        "name": "Ciudad Real",
        "coords": [
            -68250.4,
            57201.3
        ],
        "region": "EU",
        "companies": []
    },
    "exeter": {
        "name": "Exeter",
        "coords": [
            -57903.7,
            -10544.3
        ],
        "region": "EU",
        "companies": []
    },
    "geta": {
        "name": "Geta",
        "coords": [
            30211.0,
            -55443.6
        ],
        "region": "EU",
        "companies": []
    },
    "godby": {
        "name": "Godby",
        "coords": [
            30947.3,
            -54314.7
        ],
        "region": "EU",
        "companies": []
    },
    "granville": {
        "name": "Granville",
        "coords": [
            -46068.84,
            4072.789
        ],
        "region": "EU",
        "companies": []
    },
    "kovel": {
        "name": "Ковель",
        "coords": [
            50267.7,
            -5276.61
        ],
        "region": "EU",
        "companies": []
    },
    "krasnystaw": {
        "name": "Krasnystaw",
        "coords": [
            45176.6,
            -3092.67
        ],
        "region": "EU",
        "companies": []
    },
    "lochboisdale": {
        "name": "Lochboisdale",
        "coords": [
            -59185.82,
            -60837.93
        ],
        "region": "EU",
        "companies": []
    },
    "lutsk": {
        "name": "Луцьк",
        "coords": [
            53567.8,
            -2108.44
        ],
        "region": "EU",
        "companies": []
    },
    "lviv": {
        "name": "Львів",
        "coords": [
            49784.45,
            3263.109
        ],
        "region": "EU",
        "companies": []
    },
    "mulhouse": {
        "name": "Mulhouse",
        "coords": [
            -13075.14,
            15601.06
        ],
        "region": "EU",
        "companies": []
    },
    "muonio": {
        "name": "Muonio",
        "coords": [
            34199.8,
            -100131.0
        ],
        "region": "EU",
        "companies": []
    },
    "norwich": {
        "name": "Norwich",
        "coords": [
            -30444.7,
            -19256.9
        ],
        "region": "EU",
        "companies": []
    },
    "novovolynsk": {
        "name": "Нововолинськ",
        "coords": [
            49916.4,
            -901.023
        ],
        "region": "EU",
        "companies": []
    },
    "polyanytsya": {
        "name": "Поляниця",
        "coords": [
            50315.04,
            10996.24
        ],
        "region": "EU",
        "companies": []
    },
    "piotrkowt": {
        "name": "Piotrków Trybunalski",
        "coords": [
            33627.6,
            -3904.72
        ],
        "region": "EU",
        "companies": []
    },
    "poti": {
        "name": "ფოთი",
        "coords": [
            128280.0,
            28397.5
        ],
        "region": "EU",
        "companies": []
    },
    "soltau": {
        "name": "Soltau",
        "coords": [
            -364.7773,
            -12814.87
        ],
        "region": "EU",
        "companies": []
    },
    "stryi": {
        "name": "Стрий",
        "coords": [
            49503.3,
            6186.38
        ],
        "region": "EU",
        "companies": []
    },
    "sumeg": {
        "name": "Sümeg",
        "coords": [
            25193.6,
            21183.7
        ],
        "region": "EU",
        "companies": []
    },
    "szombathely": {
        "name": "Szombathely",
        "coords": [
            24040.9,
            19867.5
        ],
        "region": "EU",
        "companies": []
    },
    "thorlakshofn": {
        "name": "Þorlákshöfn",
        "coords": [
            -91379.0,
            -95046.1
        ],
        "region": "EU",
        "companies": []
    },
    "varmahlid": {
        "name": "Varmahlíð",
        "coords": [
            -80411.98,
            -102474.7
        ],
        "region": "EU",
        "companies": []
    },
    "vestero": {
        "name": "Vesterø Havn",
        "coords": [
            4178.344,
            -37163.5
        ],
        "region": "EU",
        "companies": []
    },
    "zvolen": {
        "name": "Zvolen",
        "coords": [
            32792.97,
            12590.47
        ],
        "region": "EU",
        "companies": []
    },
    "andalsnes": {
        "name": "Åndalsnes",
        "coords": [
            -2391.539,
            -68787.44
        ],
        "region": "EU",
        "companies": []
    },
    "batsfjord": {
        "name": "Båtsfjord",
        "coords": [
            42847.58,
            -117492.9
        ],
        "region": "EU",
        "companies": []
    },
    "berlevag": {
        "name": "Berlevåg",
        "coords": [
            41324.86,
            -118032.9
        ],
        "region": "EU",
        "companies": []
    },
    "bidjovagge": {
        "name": "Bidjovagge",
        "coords": [
            30955.17,
            -108304.3
        ],
        "region": "EU",
        "companies": []
    },
    "canfranc": {
        "name": "Canfranc-Estación",
        "coords": [
            -48987.39,
            38274.56
        ],
        "region": "EU",
        "companies": []
    },
    "chernivtsi": {
        "name": "Чернівці",
        "coords": [
            56111.12,
            10513.7
        ],
        "region": "EU",
        "companies": []
    },
    "contreras": {
        "name": "Contreras",
        "coords": [
            -56443.04,
            56805.04
        ],
        "region": "EU",
        "companies": []
    },
    "dax": {
        "name": "Dax",
        "coords": [
            -48863.81,
            33009.8
        ],
        "region": "EU",
        "companies": []
    },
    "foix": {
        "name": "Foix",
        "coords": [
            -39070.86,
            38649.75
        ],
        "region": "EU",
        "companies": []
    },
    "giurgiulesti": {
        "name": "Giurgiulești",
        "coords": [
            70050.16,
            23286.54
        ],
        "region": "EU",
        "companies": []
    },
    "ivanofrank": {
        "name": "Івано-Франківськ",
        "coords": [
            52215.86,
            8255.016
        ],
        "region": "EU",
        "companies": []
    },
    "karasjok": {
        "name": "Karasjok",
        "coords": [
            35935.45,
            -110560.4
        ],
        "region": "EU",
        "companies": []
    },
    "kaustinen": {
        "name": "Kaustinen",
        "coords": [
            38800.68,
            -73772.19
        ],
        "region": "EU",
        "companies": []
    },
    "kautokeino": {
        "name": "Kautokeino",
        "coords": [
            32340.15,
            -107199.0
        ],
        "region": "EU",
        "companies": []
    },
    "kjollefjord": {
        "name": "Kjøllefjord",
        "coords": [
            38660.5,
            -118681.2
        ],
        "region": "EU",
        "companies": []
    },
    "lakselv": {
        "name": "Lakselv",
        "coords": [
            34723.86,
            -113360.8
        ],
        "region": "EU",
        "companies": []
    },
    "lebesby": {
        "name": "Lebesby",
        "coords": [
            38653.41,
            -116463.7
        ],
        "region": "EU",
        "companies": []
    },
    "llivia": {
        "name": "Llívia",
        "coords": [
            -36828.14,
            43060.66
        ],
        "region": "EU",
        "companies": []
    },
    "mehamn": {
        "name": "Mehamn",
        "coords": [
            39356.19,
            -119092.8
        ],
        "region": "EU",
        "companies": []
    },
    "michalovce": {
        "name": "Michalovce",
        "coords": [
            42403.23,
            10198.44
        ],
        "region": "EU",
        "companies": []
    },
    "molde": {
        "name": "Molde",
        "coords": [
            -3566.844,
            -69333.64
        ],
        "region": "EU",
        "companies": []
    },
    "mragowo": {
        "name": "Mrągowo",
        "coords": [
            37610.28,
            -18811.24
        ],
        "region": "EU",
        "companies": []
    },
    "newport": {
        "name": "Newport",
        "coords": [
            -53091.15,
            -15517.18
        ],
        "region": "EU",
        "companies": []
    },
    "nordurfjord": {
        "name": "Norðurfjörður",
        "coords": [
            -83583.28,
            -109283.3
        ],
        "region": "EU",
        "companies": []
    },
    "olafsvik": {
        "name": "Ólafsvík",
        "coords": [
            -94035.47,
            -106360.8
        ],
        "region": "EU",
        "companies": []
    },
    "pello": {
        "name": "Pello",
        "coords": [
            36296.51,
            -91209.48
        ],
        "region": "EU",
        "companies": []
    },
    "port": {
        "name": "Port de Sóller",
        "coords": [
            -37286.65,
            57312.64
        ],
        "region": "EU",
        "companies": []
    },
    "savonlinna": {
        "name": "Savonlinna",
        "coords": [
            54522.92,
            -66390.95
        ],
        "region": "EU",
        "companies": []
    },
    "seinajoki": {
        "name": "Seinäjoki",
        "coords": [
            36915.07,
            -68926.15
        ],
        "region": "EU",
        "companies": []
    },
    "siracusa": {
        "name": "Siracusa",
        "coords": [
            17780.54,
            78109.8
        ],
        "region": "EU",
        "companies": []
    },
    "storslett": {
        "name": "Storslett",
        "coords": [
            28152.17,
            -110156.0
        ],
        "region": "EU",
        "companies": []
    },
    "stykkisholmur": {
        "name": "Stykkishólmur",
        "coords": [
            -90510.41,
            -104725.6
        ],
        "region": "EU",
        "companies": []
    },
    "vadso": {
        "name": "Vadsø",
        "coords": [
            43934.94,
            -115231.0
        ],
        "region": "EU",
        "companies": []
    },
    "valenciennes": {
        "name": "Valenciennes",
        "coords": [
            -25048.98,
            -978.5313
        ],
        "region": "EU",
        "companies": []
    },
    "valletta": {
        "name": "il-Belt Valletta",
        "coords": [
            13586.7,
            83228.8
        ],
        "region": "EU",
        "companies": []
    },
    "varash": {
        "name": "Вараш",
        "coords": [
            54920.42,
            -5942.145
        ],
        "region": "EU",
        "companies": []
    },
    "vardo": {
        "name": "Vardø",
        "coords": [
            45565.54,
            -117029.7
        ],
        "region": "EU",
        "companies": []
    },
    "wadowice": {
        "name": "Wadowice",
        "coords": [
            33552.8,
            4762.188
        ],
        "region": "EU",
        "companies": []
    },
    "ylivieska": {
        "name": "Ylivieska",
        "coords": [
            40487.65,
            -76723.53
        ],
        "region": "EU",
        "companies": []
    },
    "amstetten": {
        "name": "Amstetten",
        "coords": [
            16040.51,
            14873.95
        ],
        "region": "EU",
        "companies": []
    },
    "ballangen": {
        "name": "Ballangen",
        "coords": [
            19570.09,
            -101287.2
        ],
        "region": "EU",
        "companies": []
    },
    "bardufoss": {
        "name": "Bardufoss",
        "coords": [
            23239.85,
            -105655.8
        ],
        "region": "EU",
        "companies": []
    },
    "bischofsh": {
        "name": "Bischofshofen",
        "coords": [
            10585.67,
            19834.13
        ],
        "region": "EU",
        "companies": []
    },
    "coquelles": {
        "name": "Coquelles",
        "coords": [
            -31598.87,
            -1694.344
        ],
        "region": "EU",
        "companies": []
    },
    "corlu": {
        "name": "Çorlu",
        "coords": [
            70491.88,
            48112.96
        ],
        "region": "EU",
        "companies": []
    },
    "dobrich": {
        "name": "Добрич",
        "coords": [
            69604.63,
            34660.93
        ],
        "region": "EU",
        "companies": []
    },
    "finnsnes": {
        "name": "Finnsnes",
        "coords": [
            21730.42,
            -106497.1
        ],
        "region": "EU",
        "companies": []
    },
    "leoben": {
        "name": "Leoben",
        "coords": [
            17024.05,
            18312.98
        ],
        "region": "EU",
        "companies": []
    },
    "macon": {
        "name": "Mâcon",
        "coords": [
            -22099.46,
            23033.09
        ],
        "region": "EU",
        "companies": []
    },
    "saalfelden": {
        "name": "Saalfelden",
        "coords": [
            7934.309,
            19164.35
        ],
        "region": "EU",
        "companies": []
    },
    "sebes": {
        "name": "Sebeș",
        "coords": [
            50442.66,
            23482.44
        ],
        "region": "EU",
        "companies": []
    },
    "setermoen": {
        "name": "Setermoen",
        "coords": [
            22586.16,
            -104614.9
        ],
        "region": "EU",
        "companies": []
    },
    "shumen": {
        "name": "Шумен",
        "coords": [
            66615.86,
            37987.6
        ],
        "region": "EU",
        "companies": []
    },
    "silistra": {
        "name": "Силистра",
        "coords": [
            65484.71,
            33148.2
        ],
        "region": "EU",
        "companies": []
    },
    "stockerau": {
        "name": "Stockerau",
        "coords": [
            20602.39,
            12160.02
        ],
        "region": "EU",
        "companies": []
    },
    "trofors": {
        "name": "Trofors",
        "coords": [
            13019.88,
            -84668.54
        ],
        "region": "EU",
        "companies": []
    },
    "tulcea": {
        "name": "Tulcea",
        "coords": [
            73225.2,
            25999.17
        ],
        "region": "EU",
        "companies": []
    },
    "winklern": {
        "name": "Winklern",
        "coords": [
            9149.836,
            22700.78
        ],
        "region": "EU",
        "companies": []
    },
    "akhaltsikhe": {
        "name": "ახალციხე",
        "coords": [
            133394.2,
            28578.61
        ],
        "region": "EU",
        "companies": []
    },
    "antrim": {
        "name": "Antrim",
        "coords": [
            -61706.63,
            -42747.58
        ],
        "region": "EU",
        "companies": []
    },
    "ballymena": {
        "name": "Ballymena",
        "coords": [
            -61340.0,
            -44399.92
        ],
        "region": "EU",
        "companies": []
    },
    "borjomi": {
        "name": "ბორჯომი",
        "coords": [
            135744.0,
            27577.92
        ],
        "region": "EU",
        "companies": []
    },
    "buzau": {
        "name": "Buzău",
        "coords": [
            63777.5,
            26834.91
        ],
        "region": "EU",
        "companies": []
    },
    "focsani": {
        "name": "Focşani",
        "coords": [
            64481.08,
            23506.02
        ],
        "region": "EU",
        "companies": []
    },
    "gori": {
        "name": "გორი",
        "coords": [
            139229.5,
            26203.23
        ],
        "region": "EU",
        "companies": []
    },
    "grong": {
        "name": "Grong",
        "coords": [
            10000.58,
            -77827.08
        ],
        "region": "EU",
        "companies": []
    },
    "kecskemet": {
        "name": "Kecskemét",
        "coords": [
            35182.04,
            20955.21
        ],
        "region": "EU",
        "companies": []
    },
    "khashuri": {
        "name": "ხაშური",
        "coords": [
            137202.2,
            25952.71
        ],
        "region": "EU",
        "companies": []
    },
    "kilkenny": {
        "name": "Cill Chainnigh",
        "coords": [
            -69992.51,
            -28840.13
        ],
        "region": "EU",
        "companies": []
    },
    "kutaisi": {
        "name": "Kutaisi",
        "coords": [
            138379.0,
            33952.6
        ],
        "region": "EU",
        "companies": []
    },
    "larne": {
        "name": "Larne",
        "coords": [
            -58116.9,
            -43448.91
        ],
        "region": "EU",
        "companies": []
    },
    "monaco": {
        "name": "Monaco",
        "coords": [
            -13983.91,
            38207.85
        ],
        "region": "EU",
        "companies": []
    },
    "namsskogan": {
        "name": "Namsskogan",
        "coords": [
            12168.84,
            -80602.89
        ],
        "region": "EU",
        "companies": []
    },
    "newry": {
        "name": "Newry",
        "coords": [
            -62079.07,
            -38481.16
        ],
        "region": "EU",
        "companies": []
    },
    "nuuk": {
        "name": "Nuuk",
        "coords": [
            -132205.7,
            -148163.3
        ],
        "region": "EU",
        "companies": []
    },
    "sarny": {
        "name": "Сарни",
        "coords": [
            57541.62,
            -5674.383
        ],
        "region": "EU",
        "companies": []
    },
    "stpeterport": {
        "name": "Saint Peter Port",
        "coords": [
            -48839.6,
            -1156.402
        ],
        "region": "EU",
        "companies": []
    },
    "tbilisi": {
        "name": "Tbilisi",
        "coords": [
            174312.0,
            44038.1
        ],
        "region": "EU",
        "companies": []
    },
    "turkgozu": {
        "name": "Türkgözü",
        "coords": [
            133388.4,
            30181.75
        ],
        "region": "EU",
        "companies": []
    },
    "verdalsora": {
        "name": "Verdalsøra",
        "coords": [
            7964.742,
            -74269.38
        ],
        "region": "EU",
        "companies": []
    },
    "vevelstad": {
        "name": "Vevelstad",
        "coords": [
            10385.04,
            -85384.78
        ],
        "region": "EU",
        "companies": []
    },
    "waterford": {
        "name": "Port Láirge",
        "coords": [
            -70834.98,
            -24783.81
        ],
        "region": "EU",
        "companies": []
    },
    "zeni": {
        "name": "ზენი",
        "coords": [
            128493.5,
            27030.51
        ],
        "region": "EU",
        "companies": []
    },
    "rijeka": {
        "name": "Rijeka",
        "coords": [
            14366.27,
            30236.26
        ],
        "region": "EU",
        "companies": []
    },
    "osijek": {
        "name": "Osijek",
        "coords": [
            31379.55,
            28718.71
        ],
        "region": "EU",
        "companies": []
    },
    "niš": {
        "name": "Ниш",
        "coords": [
            45301.26,
            39664.18
        ],
        "region": "EU",
        "companies": []
    },
    "vranje": {
        "name": "Врање",
        "coords": [
            45138.33,
            43968.55
        ],
        "region": "EU",
        "companies": []
    },
    "zadar": {
        "name": "Zadar",
        "coords": [
            17622.05,
            36990.14
        ],
        "region": "EU",
        "companies": []
    },
    "zagreb": {
        "name": "Zagreb",
        "coords": [
            21617.84,
            26970.24
        ],
        "region": "EU",
        "companies": []
    },
    "bihać": {
        "name": "Бихаћ",
        "coords": [
            21009.56,
            32936.13
        ],
        "region": "EU",
        "companies": []
    },
    "split": {
        "name": "Split",
        "coords": [
            22115.07,
            40582.68
        ],
        "region": "EU",
        "companies": []
    },
    "banja luka": {
        "name": "Бања Лука",
        "coords": [
            26087.24,
            33233.34
        ],
        "region": "EU",
        "companies": []
    },
    "ploče": {
        "name": "Ploče",
        "coords": [
            24457.65,
            42367.71
        ],
        "region": "EU",
        "companies": []
    },
    "sarajevo": {
        "name": "Сарајево",
        "coords": [
            30802.46,
            38346.24
        ],
        "region": "EU",
        "companies": []
    },
    "zenica": {
        "name": "Зеница",
        "coords": [
            28716.82,
            36216.93
        ],
        "region": "EU",
        "companies": []
    },
    "mostar": {
        "name": "Мостар",
        "coords": [
            28483.79,
            41005.78
        ],
        "region": "EU",
        "companies": []
    },
    "dubrovnik": {
        "name": "Dubrovnik",
        "coords": [
            29387.46,
            44586.13
        ],
        "region": "EU",
        "companies": []
    },
    "tuzla": {
        "name": "Тузла",
        "coords": [
            32062.65,
            33987.56
        ],
        "region": "EU",
        "companies": []
    },
    "karakaj": {
        "name": "Каракај",
        "coords": [
            34239.14,
            33699.96
        ],
        "region": "EU",
        "companies": []
    },
    "nikšić": {
        "name": "Никшић",
        "coords": [
            33588.23,
            43338.98
        ],
        "region": "EU",
        "companies": []
    },
    "podgorica": {
        "name": "Подгорица",
        "coords": [
            34326.11,
            45528.54
        ],
        "region": "EU",
        "companies": []
    },
    "bar": {
        "name": "Бар",
        "coords": [
            33913.29,
            48865.41
        ],
        "region": "EU",
        "companies": []
    },
    "novi sad": {
        "name": "Нови Сад",
        "coords": [
            36108.23,
            30002.01
        ],
        "region": "EU",
        "companies": []
    },
    "belgrade": {
        "name": "Београд",
        "coords": [
            39346.9,
            32075.29
        ],
        "region": "EU",
        "companies": []
    },
    "bijelo polje": {
        "name": "Бијело Поље",
        "coords": [
            36468.27,
            42041.97
        ],
        "region": "EU",
        "companies": []
    },
    "tirana": {
        "name": "Tiranë",
        "coords": [
            38274.93,
            51343.19
        ],
        "region": "EU",
        "companies": []
    },
    "durrës": {
        "name": "Durrës",
        "coords": [
            36191.71,
            52037.69
        ],
        "region": "EU",
        "companies": []
    },
    "fier": {
        "name": "Fier",
        "coords": [
            38304.82,
            55012.76
        ],
        "region": "EU",
        "companies": []
    },
    "vlorë": {
        "name": "Vlorë",
        "coords": [
            36890.57,
            57259.23
        ],
        "region": "EU",
        "companies": []
    },
    "kragujevac": {
        "name": "Крагујевац",
        "coords": [
            40681.15,
            36682.63
        ],
        "region": "EU",
        "companies": []
    },
    "skopje": {
        "name": "Скопје",
        "coords": [
            43657.36,
            48230.5
        ],
        "region": "EU",
        "companies": []
    },
    "bitola": {
        "name": "Битола",
        "coords": [
            45018.23,
            52990.2
        ],
        "region": "EU",
        "companies": []
    },
    "ljubljana": {
        "name": "Ljubljana",
        "coords": [
            15398.1,
            25965.21
        ],
        "region": "EU",
        "companies": []
    },
    "maribor": {
        "name": "Maribor",
        "coords": [
            18694.5,
            23210.31
        ],
        "region": "EU",
        "companies": []
    },
    "novo mesto": {
        "name": "Novo Mesto",
        "coords": [
            16812.72,
            27789.35
        ],
        "region": "EU",
        "companies": []
    },
    "pristina": {
        "name": "Prishtinë",
        "coords": [
            42673.64,
            43605.76
        ],
        "region": "EU",
        "companies": []
    },
    "senj": {
        "name": "Senj",
        "coords": [
            16446.93,
            32219.38
        ],
        "region": "EU",
        "companies": []
    },
    "slavonski": {
        "name": "Slavonski Brod",
        "coords": [
            28130.14,
            30801.36
        ],
        "region": "EU",
        "companies": []
    },
    "sarande": {
        "name": "Sarandë",
        "coords": [
            39013.13,
            61010.47
        ],
        "region": "EU",
        "companies": []
    },
    "zaqatala": {
        "name": "Zaqatala",
        "coords": [
            150145.0,
            22634.14
        ],
        "region": "EU",
        "companies": []
    },
    "mingachevir": {
        "name": "Mingaçevir",
        "coords": [
            155538.2,
            24624.12
        ],
        "region": "EU",
        "companies": []
    },
    "yevlakh": {
        "name": "Yevlax",
        "coords": [
            157279.6,
            25800.02
        ],
        "region": "EU",
        "companies": []
    },
    "kurdamir": {
        "name": "Kürdamir",
        "coords": [
            160624.7,
            25365.75
        ],
        "region": "EU",
        "companies": []
    },
    "hajiqabul": {
        "name": "Hacıqabul",
        "coords": [
            163766.8,
            25992.41
        ],
        "region": "EU",
        "companies": []
    },
    "alat": {
        "name": "Alat",
        "coords": [
            165634.0,
            25618.3
        ],
        "region": "EU",
        "companies": []
    },
    "vanadzor": {
        "name": "Vanadzor",
        "coords": [
            144184.9,
            30097.3
        ],
        "region": "EU",
        "companies": []
    },
    "yerevan": {
        "name": "Yerevan",
        "coords": [
            142801.0,
            33696.29
        ],
        "region": "EU",
        "companies": []
    },
    "marneuli": {
        "name": "მარნეული",
        "coords": [
            143507.2,
            26608.22
        ],
        "region": "EU",
        "companies": []
    },
    "rustavi": {
        "name": "რუსთავი",
        "coords": [
            145456.3,
            25909.37
        ],
        "region": "EU",
        "companies": []
    },
    "telavi": {
        "name": "თელავი",
        "coords": [
            146763.3,
            22578.39
        ],
        "region": "EU",
        "companies": []
    },
    "korinthos": {
        "name": "Κόρινθος",
        "coords": [
            52317.84,
            70737.48
        ],
        "region": "EU",
        "companies": []
    },
    "gibraltar": {
        "name": "Gibraltar",
        "coords": [
            -77600.09,
            71538.92
        ],
        "region": "EU",
        "companies": []
    },
    "kesan": {
        "name": "Keşan",
        "coords": [
            64941.3,
            51801.47
        ],
        "region": "EU",
        "companies": []
    },
    "izmail": {
        "name": "Ізмаїл",
        "coords": [
            72386.28,
            23993.07
        ],
        "region": "EU",
        "companies": []
    },
    "odessa": {
        "name": "Одеса",
        "coords": [
            77800.14,
            18119.77
        ],
        "region": "EU",
        "companies": []
    },
    "bodmin": {
        "name": "Bodmin",
        "coords": [
            -63758.66,
            -9313.863
        ],
        "region": "EU",
        "companies": []
    },
    "domat": {
        "name": "Domat/Ems",
        "coords": [
            -4810.898,
            21044.8
        ],
        "region": "EU",
        "companies": []
    },
    "subotica": {
        "name": "Суботица",
        "coords": [
            34209.18,
            27748.21
        ],
        "region": "EU",
        "companies": []
    },
    "susten": {
        "name": "Susten",
        "coords": [
            -11173.92,
            23683.05
        ],
        "region": "EU",
        "companies": []
    },
    "tours": {
        "name": "Tours",
        "coords": [
            -38188.21,
            13624.64
        ],
        "region": "EU",
        "companies": []
    },
    "afula": {
        "name": "Afula",
        "coords": [
            113560.0,
            87648.5
        ],
        "region": "EU",
        "companies": []
    },
    "akko": {
        "name": "Akko",
        "coords": [
            111914.0,
            85981.9
        ],
        "region": "EU",
        "companies": []
    },
    "alkarak": {
        "name": "Al-Karak",
        "coords": [
            117713.5,
            96172.7
        ],
        "region": "EU",
        "companies": []
    },
    "alnukhib": {
        "name": "Al Nukhib",
        "coords": [
            149413.9,
            81816.39
        ],
        "region": "EU",
        "companies": []
    },
    "alqaim": {
        "name": "Al-Qa'im",
        "coords": [
            142996.5,
            70572.55
        ],
        "region": "EU",
        "companies": []
    },
    "amman": {
        "name": "Amman",
        "coords": [
            117997.0,
            91263.0
        ],
        "region": "EU",
        "companies": []
    },
    "an": {
        "name": "An-Nabk",
        "coords": [
            119958.2,
            77127.59
        ],
        "region": "EU",
        "companies": []
    },
    "aqaba": {
        "name": "Aqaba",
        "coords": [
            115676.0,
            104015.0
        ],
        "region": "EU",
        "companies": []
    },
    "ashdod": {
        "name": "Ashdod",
        "coords": [
            111424.0,
            92862.0
        ],
        "region": "EU",
        "companies": []
    },
    "ashkelon": {
        "name": "Ashkelon",
        "coords": [
            110913.0,
            93785.6
        ],
        "region": "EU",
        "companies": []
    },
    "baalbek": {
        "name": "Baalbek",
        "coords": [
            115774.6,
            79086.56
        ],
        "region": "EU",
        "companies": []
    },
    "baiji": {
        "name": "Baiji",
        "coords": [
            152591.3,
            62036.2
        ],
        "region": "EU",
        "companies": []
    },
    "beersheva": {
        "name": "Beer Sheva",
        "coords": [
            112506.0,
            96046.8
        ],
        "region": "EU",
        "companies": []
    },
    "beirut": {
        "name": "Beirut",
        "coords": [
            113037.0,
            80662.3
        ],
        "region": "EU",
        "companies": []
    },
    "bethlehem": {
        "name": "Bethlehem",
        "coords": [
            113935.0,
            93047.44
        ],
        "region": "EU",
        "companies": []
    },
    "betshean": {
        "name": "Bet She'an",
        "coords": [
            114693.0,
            87845.3
        ],
        "region": "EU",
        "companies": []
    },
    "byblos": {
        "name": "Byblos",
        "coords": [
            113231.0,
            79176.8
        ],
        "region": "EU",
        "companies": []
    },
    "damascus": {
        "name": "Damascus",
        "coords": [
            117900.0,
            81594.5
        ],
        "region": "EU",
        "companies": []
    },
    "damietta": {
        "name": "Damietta",
        "coords": [
            99855.5,
            97062.2
        ],
        "region": "EU",
        "companies": []
    },
    "deraa": {
        "name": "Deraa",
        "coords": [
            117740.0,
            86145.0
        ],
        "region": "EU",
        "companies": []
    },
    "dimona": {
        "name": "Dimona",
        "coords": [
            114006.0,
            97336.5
        ],
        "region": "EU",
        "companies": []
    },
    "eilat": {
        "name": "Eilat",
        "coords": [
            114979.0,
            103848.0
        ],
        "region": "EU",
        "companies": []
    },
    "eingedi": {
        "name": "Ein Gedi",
        "coords": [
            115452.0,
            94729.5
        ],
        "region": "EU",
        "companies": []
    },
    "elarish": {
        "name": "El Arish",
        "coords": [
            108031.0,
            97150.4
        ],
        "region": "EU",
        "companies": []
    },
    "hadera": {
        "name": "Hadera",
        "coords": [
            112148.0,
            87975.3
        ],
        "region": "EU",
        "companies": []
    },
    "haditha": {
        "name": "Haditha",
        "coords": [
            146319.0,
            70940.06
        ],
        "region": "EU",
        "companies": []
    },
    "haifa": {
        "name": "Haifa",
        "coords": [
            111796.0,
            86732.1
        ],
        "region": "EU",
        "companies": []
    },
    "haql": {
        "name": "Haql",
        "coords": [
            115406.0,
            106289.0
        ],
        "region": "EU",
        "companies": []
    },
    "herzliya": {
        "name": "Herzliya",
        "coords": [
            112615.0,
            89625.3
        ],
        "region": "EU",
        "companies": []
    },
    "hims": {
        "name": "Homs",
        "coords": [
            119220.7,
            73513.72
        ],
        "region": "EU",
        "companies": []
    },
    "hit": {
        "name": "Hit",
        "coords": [
            148240.1,
            72657.38
        ],
        "region": "EU",
        "companies": []
    },
    "irbid": {
        "name": "Irbid",
        "coords": [
            116337.0,
            87668.7
        ],
        "region": "EU",
        "companies": []
    },
    "izra": {
        "name": "Izra",
        "coords": [
            118402.0,
            84567.7
        ],
        "region": "EU",
        "companies": []
    },
    "jericho": {
        "name": "Jericho",
        "coords": [
            115719.0,
            92042.1
        ],
        "region": "EU",
        "companies": []
    },
    "jerash": {
        "name": "Jerash",
        "coords": [
            116762.7,
            89222.38
        ],
        "region": "EU",
        "companies": []
    },
    "jerusalem": {
        "name": "Jerusalem",
        "coords": [
            113691.0,
            92277.8
        ],
        "region": "EU",
        "companies": []
    },
    "kshmona": {
        "name": "Kiryat Shmona",
        "coords": [
            114562.0,
            84137.3
        ],
        "region": "EU",
        "companies": []
    },
    "maan": {
        "name": "Ma'an",
        "coords": [
            118442.7,
            100769.2
        ],
        "region": "EU",
        "companies": []
    },
    "madaba": {
        "name": "Madaba",
        "coords": [
            117547.0,
            92957.8
        ],
        "region": "EU",
        "companies": []
    },
    "mafraq": {
        "name": "Mafraq",
        "coords": [
            118322.0,
            88451.3
        ],
        "region": "EU",
        "companies": []
    },
    "mersin": {
        "name": "Mersin",
        "coords": [
            107097.3,
            66435.42
        ],
        "region": "EU",
        "companies": []
    },
    "mitzpe": {
        "name": "Mitzpe Ramon",
        "coords": [
            112703.0,
            98894.4
        ],
        "region": "EU",
        "companies": []
    },
    "nabatieh": {
        "name": "Nabatieh",
        "coords": [
            113769.0,
            83721.5
        ],
        "region": "EU",
        "companies": []
    },
    "nakhl": {
        "name": "Nakhl",
        "coords": [
            109563.0,
            103987.0
        ],
        "region": "EU",
        "companies": []
    },
    "nazareth": {
        "name": "Nazareth",
        "coords": [
            113551.0,
            87167.6
        ],
        "region": "EU",
        "companies": []
    },
    "netanya": {
        "name": "Netanya",
        "coords": [
            111696.0,
            88953.3
        ],
        "region": "EU",
        "companies": []
    },
    "osmaniye": {
        "name": "Osmaniye",
        "coords": [
            113927.6,
            62851.54
        ],
        "region": "EU",
        "companies": []
    },
    "portsaid": {
        "name": "Port Said",
        "coords": [
            101740.0,
            97628.5
        ],
        "region": "EU",
        "companies": []
    },
    "ramallah": {
        "name": "Ramallah",
        "coords": [
            114230.0,
            91507.8
        ],
        "region": "EU",
        "companies": []
    },
    "rishon": {
        "name": "Rishon LeZion",
        "coords": [
            111850.0,
            91479.3
        ],
        "region": "EU",
        "companies": []
    },
    "rutba": {
        "name": "Ar-Rutbah",
        "coords": [
            137980.0,
            80112.0
        ],
        "region": "EU",
        "companies": []
    },
    "ruwaished": {
        "name": "Ruwaished",
        "coords": [
            127939.0,
            84836.5
        ],
        "region": "EU",
        "companies": []
    },
    "safawi": {
        "name": "Safawi",
        "coords": [
            123366.0,
            88165.9
        ],
        "region": "EU",
        "companies": []
    },
    "sanamayn": {
        "name": "Al-Sanamayn",
        "coords": [
            117458.6,
            83223.72
        ],
        "region": "EU",
        "companies": []
    },
    "sayda": {
        "name": "Sayda",
        "coords": [
            112609.0,
            82771.8
        ],
        "region": "EU",
        "companies": []
    },
    "silifke": {
        "name": "Silifke",
        "coords": [
            104684.0,
            69625.0
        ],
        "region": "EU",
        "companies": []
    },
    "taba": {
        "name": "Taba",
        "coords": [
            114517.0,
            104701.0
        ],
        "region": "EU",
        "companies": []
    },
    "telaviv": {
        "name": "Tel Aviv",
        "coords": [
            111764.0,
            90591.5
        ],
        "region": "EU",
        "companies": []
    },
    "tiberias": {
        "name": "Tiberias",
        "coords": [
            114292.0,
            86046.6
        ],
        "region": "EU",
        "companies": []
    },
    "tripolilb": {
        "name": "Tripoli",
        "coords": [
            113601.0,
            77400.8
        ],
        "region": "EU",
        "companies": []
    },
    "tyr": {
        "name": "Tyr",
        "coords": [
            112294.0,
            83905.7
        ],
        "region": "EU",
        "companies": []
    },
    "zahle": {
        "name": "Zahle",
        "coords": [
            114997.0,
            80176.0
        ],
        "region": "EU",
        "companies": []
    },
    "zarka": {
        "name": "Zarka",
        "coords": [
            118257.0,
            90744.4
        ],
        "region": "EU",
        "companies": []
    },
    "iskenderun": {
        "name": "İskenderun",
        "coords": [
            113050.9,
            65175.58
        ],
        "region": "EU",
        "companies": []
    },
    "antakya": {
        "name": "Antakya",
        "coords": [
            114645.3,
            66922.95
        ],
        "region": "EU",
        "companies": []
    },
    "latakia": {
        "name": "اللاذقية",
        "coords": [
            112815.5,
            70919.05
        ],
        "region": "EU",
        "companies": []
    },
    "tartus": {
        "name": "طَرْطُوس ",
        "coords": [
            113580.9,
            74175.76
        ],
        "region": "EU",
        "companies": []
    },
    "enfidha": {
        "name": "Enfidha",
        "coords": [
            -6258.188,
            82039.91
        ],
        "region": "EU",
        "companies": []
    },
    "kenitra": {
        "name": "Kénitra",
        "coords": [
            -87112.67,
            79902.2
        ],
        "region": "EU",
        "companies": []
    },
    "ksarkbir": {
        "name": "Ksar El Kbir",
        "coords": [
            -83107.34,
            77299.03
        ],
        "region": "EU",
        "companies": []
    },
    "larache": {
        "name": "Larache",
        "coords": [
            -84130.38,
            75400.34
        ],
        "region": "EU",
        "companies": []
    },
    "medtangier": {
        "name": "Port Med Tangier",
        "coords": [
            -78981.56,
            72667.91
        ],
        "region": "EU",
        "companies": []
    },
    "rabat": {
        "name": "Rabat",
        "coords": [
            -89554.86,
            80499.94
        ],
        "region": "EU",
        "companies": []
    },
    "sale": {
        "name": "Salé",
        "coords": [
            -88330.73,
            80608.2
        ],
        "region": "EU",
        "companies": []
    },
    "tangier": {
        "name": "Tangier",
        "coords": [
            -81449.96,
            72534.61
        ],
        "region": "EU",
        "companies": []
    },
    "tetouan": {
        "name": "Tétouan",
        "coords": [
            -79267.8,
            74788.69
        ],
        "region": "EU",
        "companies": []
    },
    "tunis": {
        "name": "Tunis",
        "coords": [
            -5537.71,
            76705.7
        ],
        "region": "EU",
        "companies": []
    },
    "utique": {
        "name": "Utique",
        "coords": [
            -6551.695,
            76575.57
        ],
        "region": "EU",
        "companies": []
    },
    "domitz": {
        "name": "Dömitz",
        "coords": [
            4272.0,
            -13488.0
        ],
        "region": "EU",
        "companies": []
    },
    "falkenberg": {
        "name": "Falkenberg",
        "coords": [
            7712.0,
            -34400.0
        ],
        "region": "EU",
        "companies": []
    },
    "virovitica": {
        "name": "Virovitica",
        "coords": [
            25862.7,
            28255.8
        ],
        "region": "EU",
        "companies": []
    },
    "gubkinskii": {
        "name": "Губкинский",
        "coords": [
            154107.3,
            -135867.5
        ],
        "region": "EU",
        "companies": []
    },
    "hanti": {
        "name": "Ханты-Мансийск",
        "coords": [
            154537.9,
            -111635.7
        ],
        "region": "EU",
        "companies": []
    },
    "harjg": {
        "name": "Харьягинский",
        "coords": [
            107315.8,
            -119299.0
        ],
        "region": "EU",
        "companies": []
    },
    "horei": {
        "name": "Хорей-Вер",
        "coords": [
            107536.3,
            -126203.5
        ],
        "region": "EU",
        "companies": []
    },
    "ijma": {
        "name": "Ижма",
        "coords": [
            111967.9,
            -104447.7
        ],
        "region": "EU",
        "companies": []
    },
    "inta": {
        "name": "Инта",
        "coords": [
            118726.0,
            -116817.5
        ],
        "region": "EU",
        "companies": []
    },
    "labit": {
        "name": "Лабытнанги",
        "coords": [
            126782.0,
            -132293.3
        ],
        "region": "EU",
        "companies": []
    },
    "muravlenko": {
        "name": "Муравленко",
        "coords": [
            153914.5,
            -130894.6
        ],
        "region": "EU",
        "companies": []
    },
    "nadim": {
        "name": "Надым",
        "coords": [
            141930.9,
            -136163.6
        ],
        "region": "EU",
        "companies": []
    },
    "narj": {
        "name": "Нарьян-Мар",
        "coords": [
            98898.18,
            -119378.2
        ],
        "region": "EU",
        "companies": []
    },
    "okunev": {
        "name": "Окунев Нос",
        "coords": [
            100383.8,
            -112382.0
        ],
        "region": "EU",
        "companies": []
    },
    "ozerni": {
        "name": "Озёрный",
        "coords": [
            119920.8,
            -105181.2
        ],
        "region": "EU",
        "companies": []
    },
    "salehard": {
        "name": "Салехард",
        "coords": [
            128965.1,
            -129911.7
        ],
        "region": "EU",
        "companies": []
    },
    "soviet": {
        "name": "Советский",
        "coords": [
            141030.7,
            -103236.9
        ],
        "region": "EU",
        "companies": []
    },
    "surgut": {
        "name": "Сургут",
        "coords": [
            162524.1,
            -119519.4
        ],
        "region": "EU",
        "companies": []
    },
    "tobolsk": {
        "name": "Тобольск",
        "coords": [
            162882.7,
            -96964.3
        ],
        "region": "EU",
        "companies": []
    },
    "ugorsk": {
        "name": "Югорск",
        "coords": [
            139823.3,
            -101862.3
        ],
        "region": "EU",
        "companies": []
    },
    "urengoi": {
        "name": "Новый Уренгой",
        "coords": [
            146765.3,
            -143578.1
        ],
        "region": "EU",
        "companies": []
    },
    "ustcil": {
        "name": "Усть-Цильма",
        "coords": [
            103208.1,
            -105580.6
        ],
        "region": "EU",
        "companies": []
    },
    "uxta": {
        "name": "Ухта",
        "coords": [
            113091.2,
            -94569.17
        ],
        "region": "EU",
        "companies": []
    },
    "v1": {
        "name": "В/Ч-1011",
        "coords": [
            94547.07,
            -115755.7
        ],
        "region": "EU",
        "companies": []
    },
    "v10": {
        "name": "В/Ч-1020",
        "coords": [
            123157.6,
            -133306.0
        ],
        "region": "EU",
        "companies": []
    },
    "v13": {
        "name": "В/Ч-1023",
        "coords": [
            131407.5,
            -95368.33
        ],
        "region": "EU",
        "companies": []
    },
    "v14": {
        "name": "В/Ч-1024",
        "coords": [
            161546.8,
            -103949.4
        ],
        "region": "EU",
        "companies": []
    },
    "v2": {
        "name": "В/Ч-1012",
        "coords": [
            111469.0,
            -113348.7
        ],
        "region": "EU",
        "companies": []
    },
    "v6": {
        "name": "В/Ч-1016",
        "coords": [
            115347.7,
            -137973.5
        ],
        "region": "EU",
        "companies": []
    },
    "v7": {
        "name": "В/Ч-1017",
        "coords": [
            111833.6,
            -139742.7
        ],
        "region": "EU",
        "companies": []
    },
    "v8": {
        "name": "В/Ч-1018",
        "coords": [
            110777.8,
            -136275.7
        ],
        "region": "EU",
        "companies": []
    },
    "v9": {
        "name": "В/Ч-1019",
        "coords": [
            113293.1,
            -135162.4
        ],
        "region": "EU",
        "companies": []
    },
    "velik": {
        "name": "Великовисочное",
        "coords": [
            96637.84,
            -116088.8
        ],
        "region": "EU",
        "companies": []
    },
    "vorkuta": {
        "name": "Воркута",
        "coords": [
            118490.4,
            -135093.8
        ],
        "region": "EU",
        "companies": []
    },
    "vuktil": {
        "name": "Вуктыл",
        "coords": [
            122953.0,
            -100439.5
        ],
        "region": "EU",
        "companies": []
    },
    "akshat": {
        "name": "Akshat",
        "coords": [
            151064.2,
            -35393.54
        ],
        "region": "EU",
        "companies": []
    },
    "aktau": {
        "name": "Aktau",
        "coords": [
            159261.6,
            3776.773
        ],
        "region": "EU",
        "companies": []
    },
    "aktobe": {
        "name": "Aktobe",
        "coords": [
            161421.5,
            -39913.42
        ],
        "region": "EU",
        "companies": []
    },
    "alga": {
        "name": "Alga",
        "coords": [
            163711.8,
            -36974.4
        ],
        "region": "EU",
        "companies": []
    },
    "atyrau": {
        "name": "Atyrau",
        "coords": [
            153502.8,
            -15039.41
        ],
        "region": "EU",
        "companies": []
    },
    "beyneu": {
        "name": "Beyneu",
        "coords": [
            170943.3,
            -13109.84
        ],
        "region": "EU",
        "companies": []
    },
    "dossor": {
        "name": "Dossor",
        "coords": [
            156829.4,
            -19091.21
        ],
        "region": "EU",
        "companies": []
    },
    "ershov": {
        "name": "Ершoв",
        "coords": [
            132827.9,
            -31037.85
        ],
        "region": "EU",
        "companies": []
    },
    "inderborsky": {
        "name": "Inderborsky",
        "coords": [
            149218.2,
            -22762.56
        ],
        "region": "EU",
        "companies": []
    },
    "jasliq": {
        "name": "Jasliq",
        "coords": [
            181382.7,
            -9029.109
        ],
        "region": "EU",
        "companies": []
    },
    "kandyagash": {
        "name": "Kandyagash",
        "coords": [
            165576.0,
            -35791.0
        ],
        "region": "EU",
        "companies": []
    },
    "karabalyk": {
        "name": "Karabalyk",
        "coords": [
            164293.7,
            -65292.33
        ],
        "region": "EU",
        "companies": []
    },
    "karabutak": {
        "name": "Karabutak",
        "coords": [
            171574.2,
            -44427.77
        ],
        "region": "EU",
        "companies": []
    },
    "karakalp": {
        "name": "Karakalpakstan",
        "coords": [
            175971.1,
            -11426.43
        ],
        "region": "EU",
        "companies": []
    },
    "kendirli": {
        "name": "Kendirli",
        "coords": [
            169046.1,
            5884.102
        ],
        "region": "EU",
        "companies": []
    },
    "khromtau": {
        "name": "Khromtau",
        "coords": [
            166482.4,
            -43515.1
        ],
        "region": "EU",
        "companies": []
    },
    "kobda": {
        "name": "Kobda",
        "coords": [
            156979.5,
            -36793.27
        ],
        "region": "EU",
        "companies": []
    },
    "kostanay": {
        "name": "Kostanay",
        "coords": [
            169870.9,
            -67177.3
        ],
        "region": "EU",
        "companies": []
    },
    "kulsari": {
        "name": "Kulsari",
        "coords": [
            160960.9,
            -17118.05
        ],
        "region": "EU",
        "companies": []
    },
    "kuryk": {
        "name": "Kuryk",
        "coords": [
            163371.2,
            4981.621
        ],
        "region": "EU",
        "companies": []
    },
    "kyrkkyz": {
        "name": "Qirqqiz",
        "coords": [
            186474.1,
            -6982.469
        ],
        "region": "EU",
        "companies": []
    },
    "lisakovsk": {
        "name": "Lisakovsk",
        "coords": [
            168357.7,
            -59523.86
        ],
        "region": "EU",
        "companies": []
    },
    "makat": {
        "name": "Makat",
        "coords": [
            159177.3,
            -23250.29
        ],
        "region": "EU",
        "companies": []
    },
    "mangystau": {
        "name": "Mangystau",
        "coords": [
            161613.0,
            2643.324
        ],
        "region": "EU",
        "companies": []
    },
    "martuk": {
        "name": "Martuk",
        "coords": [
            158454.5,
            -41929.16
        ],
        "region": "EU",
        "companies": []
    },
    "mukur": {
        "name": "Mukur",
        "coords": [
            160736.7,
            -25654.23
        ],
        "region": "EU",
        "companies": []
    },
    "rudnyy": {
        "name": "Rudnyy",
        "coords": [
            168627.2,
            -63225.5
        ],
        "region": "EU",
        "companies": []
    },
    "saiotes": {
        "name": "Saiotes",
        "coords": [
            168005.3,
            -5756.422
        ],
        "region": "EU",
        "companies": []
    },
    "shetpe": {
        "name": "Shetpe",
        "coords": [
            162941.6,
            -410.543
        ],
        "region": "EU",
        "companies": []
    },
    "shubarkuduk": {
        "name": "Shubarkuduk",
        "coords": [
            162721.4,
            -32494.64
        ],
        "region": "EU",
        "companies": []
    },
    "temir": {
        "name": "Temir",
        "coords": [
            165123.6,
            -33359.09
        ],
        "region": "EU",
        "companies": []
    },
    "temirbek": {
        "name": "Temirbek Zhurgenov",
        "coords": [
            171861.7,
            -47571.91
        ],
        "region": "EU",
        "companies": []
    },
    "tobol": {
        "name": "Tobol",
        "coords": [
            168140.4,
            -60783.46
        ],
        "region": "EU",
        "companies": []
    },
    "turysh": {
        "name": "Turysh",
        "coords": [
            174580.3,
            -15934.31
        ],
        "region": "EU",
        "companies": []
    },
    "uralsk": {
        "name": "Uralsk",
        "coords": [
            140101.5,
            -34312.2
        ],
        "region": "EU",
        "companies": []
    },
    "zatobolsk": {
        "name": "Tobil",
        "coords": [
            171611.4,
            -68402.68
        ],
        "region": "EU",
        "companies": []
    },
    "zhanaozen": {
        "name": "Zhanaozen",
        "coords": [
            169197.1,
            333.4336
        ],
        "region": "EU",
        "companies": []
    },
    "zhympity": {
        "name": "Zhympity",
        "coords": [
            146828.0,
            -31815.45
        ],
        "region": "EU",
        "companies": []
    },
    "adana": {
        "name": "Adana",
        "coords": [
            110348.0,
            64598.5
        ],
        "region": "EU",
        "companies": []
    },
    "adiyaman": {
        "name": "Adiyaman",
        "coords": [
            122214.3,
            56457.47
        ],
        "region": "EU",
        "companies": []
    },
    "afyon": {
        "name": "Afyonkarahisar",
        "coords": [
            84430.3,
            62509.7
        ],
        "region": "EU",
        "companies": []
    },
    "aksaray": {
        "name": "Aksaray",
        "coords": [
            102523.0,
            59107.41
        ],
        "region": "EU",
        "companies": []
    },
    "amasya": {
        "name": "Amasya",
        "coords": [
            105762.0,
            46634.9
        ],
        "region": "EU",
        "companies": []
    },
    "ankara": {
        "name": "Ankara",
        "coords": [
            94045.1,
            53673.6
        ],
        "region": "EU",
        "companies": []
    },
    "antalya": {
        "name": "Antalya",
        "coords": [
            89110.1,
            70171.3
        ],
        "region": "EU",
        "companies": []
    },
    "artvin": {
        "name": "Artvin",
        "coords": [
            130294.6,
            32912.18
        ],
        "region": "EU",
        "companies": []
    },
    "aydin": {
        "name": "Aydin",
        "coords": [
            74903.6,
            67276.95
        ],
        "region": "EU",
        "companies": []
    },
    "balikesir": {
        "name": "Balikesir",
        "coords": [
            73428.4,
            57320.3
        ],
        "region": "EU",
        "companies": []
    },
    "bartin": {
        "name": "Bartın",
        "coords": [
            90284.98,
            42424.71
        ],
        "region": "EU",
        "companies": []
    },
    "batman": {
        "name": "Batman",
        "coords": [
            133058.0,
            60849.7
        ],
        "region": "EU",
        "companies": []
    },
    "bingol": {
        "name": "Bingöl",
        "coords": [
            129623.9,
            46192.22
        ],
        "region": "EU",
        "companies": []
    },
    "bolu": {
        "name": "Bolu",
        "coords": [
            88176.2,
            48050.91
        ],
        "region": "EU",
        "companies": []
    },
    "bursa": {
        "name": "Bursa",
        "coords": [
            76821.57,
            53587.79
        ],
        "region": "EU",
        "companies": []
    },
    "canakkale": {
        "name": "Çanakkale",
        "coords": [
            66449.89,
            55577.14
        ],
        "region": "EU",
        "companies": []
    },
    "corum": {
        "name": "Çorum",
        "coords": [
            103013.7,
            45263.62
        ],
        "region": "EU",
        "companies": []
    },
    "denizli": {
        "name": "Denizli",
        "coords": [
            80310.3,
            66906.4
        ],
        "region": "EU",
        "companies": []
    },
    "diyarbakir": {
        "name": "Diyarbakir",
        "coords": [
            127757.0,
            60288.9
        ],
        "region": "EU",
        "companies": []
    },
    "elazig": {
        "name": "Elâzığ",
        "coords": [
            123943.9,
            50246.44
        ],
        "region": "EU",
        "companies": []
    },
    "erzincan": {
        "name": "Erzincan",
        "coords": [
            123188.1,
            43981.77
        ],
        "region": "EU",
        "companies": []
    },
    "erzurum": {
        "name": "Erzurum",
        "coords": [
            130149.4,
            40430.03
        ],
        "region": "EU",
        "companies": []
    },
    "eskisehir": {
        "name": "Eskisehir",
        "coords": [
            84895.9,
            54483.9
        ],
        "region": "EU",
        "companies": []
    },
    "gaziantep": {
        "name": "Gaziantep",
        "coords": [
            118770.0,
            62008.41
        ],
        "region": "EU",
        "companies": []
    },
    "giresun": {
        "name": "Giresun",
        "coords": [
            119370.0,
            42345.6
        ],
        "region": "EU",
        "companies": []
    },
    "girne": {
        "name": "Girne",
        "coords": [
            102544.0,
            101224.0
        ],
        "region": "EU",
        "companies": []
    },
    "hakkari": {
        "name": "Hakkari",
        "coords": [
            143458.0,
            60816.4
        ],
        "region": "EU",
        "companies": []
    },
    "hatay": {
        "name": "Hatay",
        "coords": [
            112386.0,
            71442.3
        ],
        "region": "EU",
        "companies": []
    },
    "igdir": {
        "name": "Iğdır",
        "coords": [
            141115.7,
            36948.11
        ],
        "region": "EU",
        "companies": []
    },
    "izmir": {
        "name": "İzmir",
        "coords": [
            71451.3,
            64719.0
        ],
        "region": "EU",
        "companies": []
    },
    "karabuk": {
        "name": "Karabük",
        "coords": [
            92682.58,
            44488.52
        ],
        "region": "EU",
        "companies": []
    },
    "karaman": {
        "name": "Karaman",
        "coords": [
            97197.8,
            68277.3
        ],
        "region": "EU",
        "companies": []
    },
    "kars": {
        "name": "Kars",
        "coords": [
            137061.2,
            34675.14
        ],
        "region": "EU",
        "companies": []
    },
    "kastamonu": {
        "name": "Kastamonu",
        "coords": [
            96470.9,
            42966.0
        ],
        "region": "EU",
        "companies": []
    },
    "kayseri": {
        "name": "Kayseri",
        "coords": [
            108385.2,
            54227.54
        ],
        "region": "EU",
        "companies": []
    },
    "kirikkale": {
        "name": "Kırıkkale",
        "coords": [
            98390.17,
            50824.5
        ],
        "region": "EU",
        "companies": []
    },
    "kirklareli": {
        "name": "Kirklareli",
        "coords": [
            68766.9,
            46790.2
        ],
        "region": "EU",
        "companies": []
    },
    "kirsehir": {
        "name": "Kirsehir",
        "coords": [
            100863.0,
            57390.7
        ],
        "region": "EU",
        "companies": []
    },
    "kmaras": {
        "name": "Kahramanmaras",
        "coords": [
            113249.0,
            62406.5
        ],
        "region": "EU",
        "companies": []
    },
    "konya": {
        "name": "Konya",
        "coords": [
            96310.73,
            62672.84
        ],
        "region": "EU",
        "companies": []
    },
    "lefkosa": {
        "name": "Lefkosa",
        "coords": [
            102847.0,
            103541.0
        ],
        "region": "EU",
        "companies": []
    },
    "malatya": {
        "name": "Malatya",
        "coords": [
            120853.6,
            53186.75
        ],
        "region": "EU",
        "companies": []
    },
    "mardin": {
        "name": "Mardin",
        "coords": [
            132927.5,
            55588.05
        ],
        "region": "EU",
        "companies": []
    },
    "mugla": {
        "name": "Muğla",
        "coords": [
            78415.7,
            70673.02
        ],
        "region": "EU",
        "companies": []
    },
    "ordu": {
        "name": "Ordu",
        "coords": [
            115070.1,
            39538.91
        ],
        "region": "EU",
        "companies": []
    },
    "rize": {
        "name": "Rize",
        "coords": [
            128517.0,
            40215.0
        ],
        "region": "EU",
        "companies": []
    },
    "sakarya": {
        "name": "Sakarya",
        "coords": [
            83003.33,
            48422.43
        ],
        "region": "EU",
        "companies": []
    },
    "samsun": {
        "name": "Samsun",
        "coords": [
            107297.0,
            39719.5
        ],
        "region": "EU",
        "companies": []
    },
    "sanliurfa": {
        "name": "Şanlıurfa",
        "coords": [
            124300.4,
            59584.64
        ],
        "region": "EU",
        "companies": []
    },
    "sinop": {
        "name": "Sinop",
        "coords": [
            101533.0,
            38543.8
        ],
        "region": "EU",
        "companies": []
    },
    "sirnak": {
        "name": "Sirnak",
        "coords": [
            137990.0,
            62569.1
        ],
        "region": "EU",
        "companies": []
    },
    "sivas": {
        "name": "Sivas",
        "coords": [
            112908.6,
            47132.48
        ],
        "region": "EU",
        "companies": []
    },
    "tokat": {
        "name": "Tokat",
        "coords": [
            110489.1,
            45347.49
        ],
        "region": "EU",
        "companies": []
    },
    "trabzon": {
        "name": "Trabzon",
        "coords": [
            121408.0,
            37133.9
        ],
        "region": "EU",
        "companies": []
    },
    "usak": {
        "name": "Uşak",
        "coords": [
            80995.97,
            61733.21
        ],
        "region": "EU",
        "companies": []
    },
    "van": {
        "name": "Van",
        "coords": [
            143754.0,
            54117.6
        ],
        "region": "EU",
        "companies": []
    },
    "yozgat": {
        "name": "Yozgat",
        "coords": [
            103212.9,
            49640.85
        ],
        "region": "EU",
        "companies": []
    },
    "zonguldak": {
        "name": "Zonguldak",
        "coords": [
            88663.5,
            44084.4
        ],
        "region": "EU",
        "companies": []
    },
    "ancona": {
        "name": "Ancona",
        "coords": [
            10260.4,
            40272.5
        ],
        "region": "EU",
        "companies": []
    },
    "aquila": {
        "name": "L'Aquila",
        "coords": [
            10098.9,
            46803.9
        ],
        "region": "EU",
        "companies": []
    },
    "bari": {
        "name": "Bari",
        "coords": [
            23803.7,
            54577.8
        ],
        "region": "EU",
        "companies": []
    },
    "cagliari": {
        "name": "Cagliari",
        "coords": [
            -9351.08,
            64225.5
        ],
        "region": "EU",
        "companies": []
    },
    "catania": {
        "name": "Catania",
        "coords": [
            16904.9,
            75107.5
        ],
        "region": "EU",
        "companies": []
    },
    "catanz": {
        "name": "Catanzaro",
        "coords": [
            23154.8,
            66889.7
        ],
        "region": "EU",
        "companies": []
    },
    "civitavec": {
        "name": "Civitavecchia",
        "coords": [
            3124.0,
            48749.1
        ],
        "region": "EU",
        "companies": []
    },
    "crotone": {
        "name": "Crotone",
        "coords": [
            25677.5,
            65250.7
        ],
        "region": "EU",
        "companies": []
    },
    "drammen": {
        "name": "Drammen",
        "coords": [
            2505.0,
            -50955.0
        ],
        "region": "EU",
        "companies": []
    },
    "enna": {
        "name": "Enna",
        "coords": [
            12818.1,
            74267.5
        ],
        "region": "EU",
        "companies": []
    },
    "foggia": {
        "name": "Foggia",
        "coords": [
            18927.3,
            52413.7
        ],
        "region": "EU",
        "companies": []
    },
    "imola": {
        "name": "Imola",
        "coords": [
            3285.87,
            35401.5
        ],
        "region": "EU",
        "companies": []
    },
    "laspezia": {
        "name": "La Spezia",
        "coords": [
            -5183.63,
            37196.4
        ],
        "region": "EU",
        "companies": []
    },
    "latina": {
        "name": "Latina",
        "coords": [
            7571.98,
            52219.6
        ],
        "region": "EU",
        "companies": []
    },
    "lecce": {
        "name": "Lecce",
        "coords": [
            30077.0,
            58629.2
        ],
        "region": "EU",
        "companies": []
    },
    "lucca": {
        "name": "Lucca",
        "coords": [
            -1316.87,
            38411.4
        ],
        "region": "EU",
        "companies": []
    },
    "messina": {
        "name": "Messina",
        "coords": [
            18557.4,
            70913.3
        ],
        "region": "EU",
        "companies": []
    },
    "napoli": {
        "name": "Napoli",
        "coords": [
            13301.3,
            55970.5
        ],
        "region": "EU",
        "companies": []
    },
    "olbia": {
        "name": "Olbia",
        "coords": [
            -6934.47,
            54933.6
        ],
        "region": "EU",
        "companies": []
    },
    "oristano": {
        "name": "Oristano",
        "coords": [
            -11619.1,
            59839.6
        ],
        "region": "EU",
        "companies": []
    },
    "palermo": {
        "name": "Palermo",
        "coords": [
            8961.45,
            71177.8
        ],
        "region": "EU",
        "companies": []
    },
    "perugia": {
        "name": "Perugia",
        "coords": [
            5484.8,
            42625.8
        ],
        "region": "EU",
        "companies": []
    },
    "pescara": {
        "name": "Pescara",
        "coords": [
            12380.7,
            47439.0
        ],
        "region": "EU",
        "companies": []
    },
    "pisa": {
        "name": "Pisa",
        "coords": [
            -2296.73,
            39358.6
        ],
        "region": "EU",
        "companies": []
    },
    "potenza": {
        "name": "Potenza",
        "coords": [
            19793.2,
            57224.2
        ],
        "region": "EU",
        "companies": []
    },
    "ravenna": {
        "name": "Ravenna",
        "coords": [
            5416.85,
            35514.5
        ],
        "region": "EU",
        "companies": []
    },
    "reggio": {
        "name": "Reggio",
        "coords": [
            20164.5,
            72275.1
        ],
        "region": "EU",
        "companies": []
    },
    "roma": {
        "name": "Roma",
        "coords": [
            5853.76,
            49761.7
        ],
        "region": "EU",
        "companies": []
    },
    "siena": {
        "name": "Siena",
        "coords": [
            1194.18,
            41722.3
        ],
        "region": "EU",
        "companies": []
    },
    "taranto": {
        "name": "Taranto",
        "coords": [
            25414.4,
            58739.8
        ],
        "region": "EU",
        "companies": []
    },
    "algiers": {
        "name": "Algiers",
        "coords": [
            -38215.8,
            76472.0
        ],
        "region": "EU",
        "companies": []
    },
    "annaba": {
        "name": "Annaba",
        "coords": [
            -16670.2,
            75892.2
        ],
        "region": "EU",
        "companies": []
    },
    "bizerte": {
        "name": "Bizerte",
        "coords": [
            -7092.85,
            74232.0
        ],
        "region": "EU",
        "companies": []
    },
    "constantine": {
        "name": "Constantine",
        "coords": [
            -21670.3,
            79061.1
        ],
        "region": "EU",
        "companies": []
    },
    "el": {
        "name": "El kef",
        "coords": [
            -12123.0,
            79825.3
        ],
        "region": "EU",
        "companies": []
    },
    "gabes": {
        "name": "Gabes",
        "coords": [
            -5781.2,
            91105.4
        ],
        "region": "EU",
        "companies": []
    },
    "gafsa": {
        "name": "Gafsa",
        "coords": [
            -12289.6,
            88399.2
        ],
        "region": "EU",
        "companies": []
    },
    "hammamet": {
        "name": "Hammamet",
        "coords": [
            -3332.37,
            78747.1
        ],
        "region": "EU",
        "companies": []
    },
    "houmt": {
        "name": "Houmt Souk",
        "coords": [
            -2800.36,
            91619.5
        ],
        "region": "EU",
        "companies": []
    },
    "kairouan": {
        "name": "Kairouan",
        "coords": [
            -6364.26,
            82307.5
        ],
        "region": "EU",
        "companies": []
    },
    "kasserine": {
        "name": "Kasserine",
        "coords": [
            -12202.3,
            85063.4
        ],
        "region": "EU",
        "companies": []
    },
    "medenine": {
        "name": "Medenine",
        "coords": [
            -3844.41,
            93878.2
        ],
        "region": "EU",
        "companies": []
    },
    "naftah": {
        "name": "Naftah",
        "coords": [
            -16572.2,
            91096.1
        ],
        "region": "EU",
        "companies": []
    },
    "qibilt": {
        "name": "Qibilt",
        "coords": [
            -11888.3,
            91866.5
        ],
        "region": "EU",
        "companies": []
    },
    "sfax": {
        "name": "Sfax",
        "coords": [
            -2305.61,
            86277.7
        ],
        "region": "EU",
        "companies": []
    },
    "skikda": {
        "name": "Skikda",
        "coords": [
            -20611.9,
            76010.8
        ],
        "region": "EU",
        "companies": []
    },
    "souk": {
        "name": "Souk ahras",
        "coords": [
            -15639.2,
            79294.3
        ],
        "region": "EU",
        "companies": []
    },
    "sousse": {
        "name": "Sousse",
        "coords": [
            -3402.8,
            81410.8
        ],
        "region": "EU",
        "companies": []
    },
    "badajoz": {
        "name": "Badajoz",
        "coords": [
            -78679.5,
            53325.3
        ],
        "region": "EU",
        "companies": []
    },
    "bedous": {
        "name": "Bedous",
        "coords": [
            -48149.8,
            33688.8
        ],
        "region": "EU",
        "companies": []
    },
    "coimbra": {
        "name": "Coimbra",
        "coords": [
            -86585.0,
            44747.0
        ],
        "region": "EU",
        "companies": []
    },
    "cordoba": {
        "name": "Córdoba",
        "coords": [
            -74352.0,
            61483.0
        ],
        "region": "EU",
        "companies": []
    },
    "evora": {
        "name": "Evora",
        "coords": [
            -83151.9,
            54120.0
        ],
        "region": "EU",
        "companies": []
    },
    "faro": {
        "name": "Faro",
        "coords": [
            -90480.2,
            62485.7
        ],
        "region": "EU",
        "companies": []
    },
    "gijon": {
        "name": "Gijón",
        "coords": [
            -70228.0,
            29264.0
        ],
        "region": "EU",
        "companies": []
    },
    "leon": {
        "name": "León",
        "coords": [
            -69888.2,
            32826.7
        ],
        "region": "EU",
        "companies": []
    },
    "lisboa": {
        "name": "Lisboa",
        "coords": [
            -92720.2,
            51001.9
        ],
        "region": "EU",
        "companies": []
    },
    "madrid": {
        "name": "Madrid",
        "coords": [
            -65397.7,
            49032.6
        ],
        "region": "EU",
        "companies": []
    },
    "malaga": {
        "name": "Malaga",
        "coords": [
            -73044.2,
            68830.0
        ],
        "region": "EU",
        "companies": []
    },
    "murcia": {
        "name": "Murcia",
        "coords": [
            -54158.5,
            65264.6
        ],
        "region": "EU",
        "companies": []
    },
    "o": {
        "name": "O Barco",
        "coords": [
            -77271.8,
            34199.9
        ],
        "region": "EU",
        "companies": []
    },
    "salamanca": {
        "name": "Salamanca",
        "coords": [
            -73475.9,
            43487.8
        ],
        "region": "EU",
        "companies": []
    },
    "sevilla": {
        "name": "Sevilla",
        "coords": [
            -79726.0,
            62856.0
        ],
        "region": "EU",
        "companies": []
    },
    "sines": {
        "name": "Sines",
        "coords": [
            -91831.4,
            56468.6
        ],
        "region": "EU",
        "companies": []
    },
    "valladolid": {
        "name": "Valladolid",
        "coords": [
            -66636.0,
            38485.7
        ],
        "region": "EU",
        "companies": []
    },
    "viseu": {
        "name": "Viseu",
        "coords": [
            -81381.6,
            44341.5
        ],
        "region": "EU",
        "companies": []
    },
    "baku": {
        "name": "Baku",
        "coords": [
            165128.0,
            41958.1
        ],
        "region": "EU",
        "companies": []
    },
    "gence": {
        "name": "Gence",
        "coords": [
            151490.0,
            40534.2
        ],
        "region": "EU",
        "companies": []
    },
    "yevlax": {
        "name": "Yevlax",
        "coords": [
            159787.0,
            38421.8
        ],
        "region": "EU",
        "companies": []
    },
    "afyonkarahisir": {
        "name": "Afyonkarahisir",
        "coords": [
            86341.8,
            59261.1
        ],
        "region": "EU",
        "companies": []
    },
    "agri": {
        "name": "Ağrı",
        "coords": [
            137610.7,
            38808.63
        ],
        "region": "EU",
        "companies": []
    },
    "alanya": {
        "name": "Alanya",
        "coords": [
            95598.67,
            70893.56
        ],
        "region": "EU",
        "companies": []
    },
    "ancara": {
        "name": "Ankara",
        "coords": [
            94318.16,
            51459.66
        ],
        "region": "EU",
        "companies": []
    },
    "ardahan": {
        "name": "Ardahan",
        "coords": [
            134315.9,
            33080.79
        ],
        "region": "EU",
        "companies": []
    },
    "bandirma": {
        "name": "Bandırma",
        "coords": [
            72889.91,
            53293.03
        ],
        "region": "EU",
        "companies": []
    },
    "bayburt": {
        "name": "Bayburt",
        "coords": [
            125258.4,
            40189.87
        ],
        "region": "EU",
        "companies": []
    },
    "bodrum": {
        "name": "Bodrum",
        "coords": [
            72652.4,
            72995.4
        ],
        "region": "EU",
        "companies": []
    },
    "diabakir": {
        "name": "Diyarbakır",
        "coords": [
            129061.8,
            53342.1
        ],
        "region": "EU",
        "companies": []
    },
    "ferizli": {
        "name": "Ferizli",
        "coords": [
            85003.61,
            47221.17
        ],
        "region": "EU",
        "companies": []
    },
    "fethiye": {
        "name": "Fethiye",
        "coords": [
            82471.69,
            73267.38
        ],
        "region": "EU",
        "companies": []
    },
    "hopa": {
        "name": "Hopa",
        "coords": [
            127689.2,
            32824.67
        ],
        "region": "EU",
        "companies": []
    },
    "horasan": {
        "name": "Horasan",
        "coords": [
            133569.5,
            37943.59
        ],
        "region": "EU",
        "companies": []
    },
    "isparta": {
        "name": "Isparta",
        "coords": [
            87457.6,
            65549.2
        ],
        "region": "EU",
        "companies": []
    },
    "kas": {
        "name": "Kaş",
        "coords": [
            85192.3,
            75176.2
        ],
        "region": "EU",
        "companies": []
    },
    "koycegiz": {
        "name": "Köyceğiz",
        "coords": [
            80508.78,
            71471.74
        ],
        "region": "EU",
        "companies": []
    },
    "kutahya": {
        "name": "Kütahya",
        "coords": [
            82964.73,
            56906.32
        ],
        "region": "EU",
        "companies": []
    },
    "manisa": {
        "name": "Manisa",
        "coords": [
            72564.27,
            63229.92
        ],
        "region": "EU",
        "companies": []
    },
    "sinopp": {
        "name": "Sinop",
        "coords": [
            100802.1,
            38041.05
        ],
        "region": "EU",
        "companies": []
    },
    "siverek": {
        "name": "Siverek",
        "coords": [
            127847.9,
            55452.14
        ],
        "region": "EU",
        "companies": []
    },
    "tunceli": {
        "name": "Tunceli",
        "coords": [
            124819.7,
            47278.65
        ],
        "region": "EU",
        "companies": []
    },
    "antracit": {
        "name": "Антрацит",
        "coords": [
            106670.9,
            100.8633
        ],
        "region": "EU",
        "companies": []
    },
    "bashtanka": {
        "name": "Баштанка",
        "coords": [
            84210.94,
            12045.5
        ],
        "region": "EU",
        "companies": []
    },
    "berdy": {
        "name": "Бердянськ",
        "coords": [
            99153.14,
            8773.641
        ],
        "region": "EU",
        "companies": []
    },
    "bilaterca": {
        "name": "Бiла Церква",
        "coords": [
            71649.02,
            -532.3242
        ],
        "region": "EU",
        "companies": []
    },
    "cernihiv": {
        "name": "Чернiгiв",
        "coords": [
            74001.04,
            -10369.67
        ],
        "region": "EU",
        "companies": []
    },
    "cernobil": {
        "name": "Чорнобиль",
        "coords": [
            70996.76,
            -8499.383
        ],
        "region": "EU",
        "companies": []
    },
    "cherk": {
        "name": "Черкаси",
        "coords": [
            79325.45,
            479.8359
        ],
        "region": "EU",
        "companies": []
    },
    "dnipro": {
        "name": "Днiпрo",
        "coords": [
            91563.31,
            3058.793
        ],
        "region": "EU",
        "companies": []
    },
    "donesk": {
        "name": "Донецьк",
        "coords": [
            102269.8,
            2440.184
        ],
        "region": "EU",
        "companies": []
    },
    "feodosia": {
        "name": "Феодосия",
        "coords": [
            96078.34,
            19890.57
        ],
        "region": "EU",
        "companies": []
    },
    "ialta": {
        "name": "Ялта",
        "coords": [
            92241.2,
            24201.97
        ],
        "region": "EU",
        "companies": []
    },
    "jankoi": {
        "name": "Джанкой",
        "coords": [
            91622.32,
            17378.76
        ],
        "region": "EU",
        "companies": []
    },
    "kerci": {
        "name": "Керчь",
        "coords": [
            99113.84,
            16428.29
        ],
        "region": "EU",
        "companies": []
    },
    "kerson": {
        "name": "Херсон",
        "coords": [
            85093.56,
            15804.07
        ],
        "region": "EU",
        "companies": []
    },
    "kharkiv": {
        "name": "Харкiв",
        "coords": [
            93827.67,
            -6729.859
        ],
        "region": "EU",
        "companies": []
    },
    "khmeln": {
        "name": "Хмельницький",
        "coords": [
            60662.65,
            4216.402
        ],
        "region": "EU",
        "companies": []
    },
    "kiev": {
        "name": "Киïв",
        "coords": [
            72491.15,
            -4126.684
        ],
        "region": "EU",
        "companies": []
    },
    "konotop": {
        "name": "Конотоп",
        "coords": [
            81082.3,
            -10517.96
        ],
        "region": "EU",
        "companies": []
    },
    "korostenn": {
        "name": "Коростень",
        "coords": [
            65747.06,
            -5817.996
        ],
        "region": "EU",
        "companies": []
    },
    "kramatorsk": {
        "name": "Краматорськ",
        "coords": [
            99068.03,
            -2454.352
        ],
        "region": "EU",
        "companies": []
    },
    "kreme": {
        "name": "Кременчук",
        "coords": [
            85724.71,
            495.8086
        ],
        "region": "EU",
        "companies": []
    },
    "kropy": {
        "name": "Кропивницький",
        "coords": [
            81184.3,
            5349.129
        ],
        "region": "EU",
        "companies": []
    },
    "krupets": {
        "name": "Крупец",
        "coords": [
            85618.06,
            -12714.74
        ],
        "region": "EU",
        "companies": []
    },
    "kryvy": {
        "name": "Кривий Рiг",
        "coords": [
            86238.09,
            7552.195
        ],
        "region": "EU",
        "companies": []
    },
    "lubni": {
        "name": "Лубни",
        "coords": [
            82648.97,
            -3315.617
        ],
        "region": "EU",
        "companies": []
    },
    "lugan": {
        "name": "Луганськ",
        "coords": [
            106961.6,
            -2963.199
        ],
        "region": "EU",
        "companies": []
    },
    "mariupo": {
        "name": "Марiуполь",
        "coords": [
            101180.8,
            6352.844
        ],
        "region": "EU",
        "companies": []
    },
    "melitopol": {
        "name": "Мелiтополь",
        "coords": [
            93688.73,
            10137.25
        ],
        "region": "EU",
        "companies": []
    },
    "mykol": {
        "name": "Миколаïв",
        "coords": [
            82318.01,
            14180.45
        ],
        "region": "EU",
        "companies": []
    },
    "naroulia": {
        "name": "Нароўля",
        "coords": [
            68502.36,
            -11098.8
        ],
        "region": "EU",
        "companies": []
    },
    "novak": {
        "name": "Нова Каховка",
        "coords": [
            87298.14,
            12851.09
        ],
        "region": "EU",
        "companies": []
    },
    "novogradd": {
        "name": "Звягель",
        "coords": [
            62471.81,
            -3141.609
        ],
        "region": "EU",
        "companies": []
    },
    "pervom": {
        "name": "Первомайськ",
        "coords": [
            76567.55,
            8678.91
        ],
        "region": "EU",
        "companies": []
    },
    "poltava": {
        "name": "Полтава",
        "coords": [
            87859.16,
            -2842.395
        ],
        "region": "EU",
        "companies": []
    },
    "rivnne": {
        "name": "Рiвне",
        "coords": [
            57140.34,
            -2206.461
        ],
        "region": "EU",
        "companies": []
    },
    "sevas": {
        "name": "Севастополь",
        "coords": [
            90259.83,
            24393.63
        ],
        "region": "EU",
        "companies": []
    },
    "shepe": {
        "name": "Шепетiвка",
        "coords": [
            60409.93,
            -270.7227
        ],
        "region": "EU",
        "companies": []
    },
    "simfer": {
        "name": "Симферополь",
        "coords": [
            91634.97,
            21646.71
        ],
        "region": "EU",
        "companies": []
    },
    "sumy": {
        "name": "Суми",
        "coords": [
            87046.91,
            -10482.41
        ],
        "region": "EU",
        "companies": []
    },
    "taman": {
        "name": "Тамань",
        "coords": [
            100869.0,
            17436.58
        ],
        "region": "EU",
        "companies": []
    },
    "terno": {
        "name": "Тернопiль",
        "coords": [
            55732.34,
            4270.848
        ],
        "region": "EU",
        "companies": []
    },
    "troyeb": {
        "name": "Троебортное",
        "coords": [
            84089.55,
            -15363.07
        ],
        "region": "EU",
        "companies": []
    },
    "uman": {
        "name": "Умань",
        "coords": [
            73093.39,
            5399.203
        ],
        "region": "EU",
        "companies": []
    },
    "vinny": {
        "name": "Вiнниця",
        "coords": [
            66368.63,
            3988.539
        ],
        "region": "EU",
        "companies": []
    },
    "vozne": {
        "name": "Вознесенськ",
        "coords": [
            79580.44,
            11732.81
        ],
        "region": "EU",
        "companies": []
    },
    "zappo": {
        "name": "Запорiжжя",
        "coords": [
            92258.12,
            5344.465
        ],
        "region": "EU",
        "companies": []
    },
    "zitomir": {
        "name": "Житомир",
        "coords": [
            66282.3,
            -2002.555
        ],
        "region": "EU",
        "companies": []
    },
    "ribnita": {
        "name": "Rîbniţa",
        "coords": [
            70193.56,
            11954.1
        ],
        "region": "EU",
        "companies": []
    },
    "tiraspol": {
        "name": "Tiraspol",
        "coords": [
            73208.3,
            17308.2
        ],
        "region": "EU",
        "companies": []
    },
    "botos": {
        "name": "Botoșani",
        "coords": [
            59613.72,
            13102.53
        ],
        "region": "EU",
        "companies": []
    },
    "suceava": {
        "name": "Suceava",
        "coords": [
            58617.45,
            14145.89
        ],
        "region": "EU",
        "companies": []
    },
    "cernaut": {
        "name": "Чернiвцi",
        "coords": [
            56727.96,
            10742.06
        ],
        "region": "EU",
        "companies": []
    },
    "ivan": {
        "name": "Iвано-Франкiвськ",
        "coords": [
            52367.41,
            8059.941
        ],
        "region": "EU",
        "companies": []
    },
    "kovell": {
        "name": "Ковель",
        "coords": [
            51179.11,
            -4998.398
        ],
        "region": "EU",
        "companies": []
    },
    "luttsk": {
        "name": "Луцьк",
        "coords": [
            53780.88,
            -2539.934
        ],
        "region": "EU",
        "companies": []
    },
    "lyviv": {
        "name": "Львiв",
        "coords": [
            49496.96,
            3381.316
        ],
        "region": "EU",
        "companies": []
    },
    "mukac": {
        "name": "Мукачево",
        "coords": [
            46075.43,
            11647.68
        ],
        "region": "EU",
        "companies": []
    },
    "sarni": {
        "name": "Сарни",
        "coords": [
            57819.87,
            -7488.094
        ],
        "region": "EU",
        "companies": []
    },
    "stry": {
        "name": "Стрий",
        "coords": [
            49146.06,
            6286.488
        ],
        "region": "EU",
        "companies": []
    },
    "uzgor": {
        "name": "Ужгород",
        "coords": [
            44580.31,
            10596.83
        ],
        "region": "EU",
        "companies": []
    },
    "alecsandria": {
        "name": "Alexandria",
        "coords": [
            58228.17,
            34036.36
        ],
        "region": "EU",
        "companies": []
    },
    "baiam": {
        "name": "Baia Mare",
        "coords": [
            49519.06,
            15444.44
        ],
        "region": "EU",
        "companies": []
    },
    "balt": {
        "name": "Bălţi",
        "coords": [
            65974.94,
            12548.63
        ],
        "region": "EU",
        "companies": []
    },
    "bechet": {
        "name": "Bechet",
        "coords": [
            54975.18,
            35614.17
        ],
        "region": "EU",
        "companies": []
    },
    "brad": {
        "name": "Brad",
        "coords": [
            46361.5,
            22726.32
        ],
        "region": "EU",
        "companies": []
    },
    "caracal": {
        "name": "Caracal",
        "coords": [
            55385.39,
            33640.17
        ],
        "region": "EU",
        "companies": []
    },
    "chisina": {
        "name": "Chişinău",
        "coords": [
            70370.05,
            16015.29
        ],
        "region": "EU",
        "companies": []
    },
    "giurgi": {
        "name": "Giurgiu",
        "coords": [
            61258.9,
            33424.59
        ],
        "region": "EU",
        "companies": []
    },
    "ploiest": {
        "name": "Ploieşti",
        "coords": [
            59957.26,
            27320.83
        ],
        "region": "EU",
        "companies": []
    },
    "sighet": {
        "name": "Sighetul Marmaţiei",
        "coords": [
            50456.48,
            14030.35
        ],
        "region": "EU",
        "companies": []
    },
    "silistr": {
        "name": "Силистра",
        "coords": [
            65394.85,
            33849.17
        ],
        "region": "EU",
        "companies": []
    },
    "slatina": {
        "name": "Slatina",
        "coords": [
            55216.3,
            31279.5
        ],
        "region": "EU",
        "companies": []
    },
    "tgjiu": {
        "name": "Târgu Jiu",
        "coords": [
            50228.21,
            29238.32
        ],
        "region": "EU",
        "companies": []
    },
    "valcea": {
        "name": "Râmnicu Vâlcea",
        "coords": [
            53860.87,
            28121.29
        ],
        "region": "EU",
        "companies": []
    },
    "zalau": {
        "name": "Zalău",
        "coords": [
            47486.9,
            18559.3
        ],
        "region": "EU",
        "companies": []
    },
    "amagasaki": {
        "name": "尼崎",
        "coords": [
            378808.0,
            95687.92
        ],
        "region": "EU",
        "companies": []
    },
    "awaji": {
        "name": "淡路",
        "coords": [
            372996.5,
            97383.87
        ],
        "region": "EU",
        "companies": []
    },
    "daikoku": {
        "name": "大黒",
        "coords": [
            415418.9,
            90018.8
        ],
        "region": "EU",
        "companies": []
    },
    "hakusan": {
        "name": "白山",
        "coords": [
            386991.4,
            77181.68
        ],
        "region": "EU",
        "companies": []
    },
    "hida": {
        "name": "飛騨",
        "coords": [
            393572.1,
            78616.82
        ],
        "region": "EU",
        "companies": []
    },
    "ikata": {
        "name": "伊方",
        "coords": [
            349181.7,
            109261.9
        ],
        "region": "EU",
        "companies": []
    },
    "imabari": {
        "name": "今治",
        "coords": [
            355735.9,
            102857.6
        ],
        "region": "EU",
        "companies": []
    },
    "innoshima": {
        "name": "因島",
        "coords": [
            357716.0,
            100665.9
        ],
        "region": "EU",
        "companies": []
    },
    "itoigawa": {
        "name": "糸魚川",
        "coords": [
            397576.5,
            71017.15
        ],
        "region": "EU",
        "companies": []
    },
    "joetsu": {
        "name": "上越",
        "coords": [
            398500.7,
            70432.93
        ],
        "region": "EU",
        "companies": []
    },
    "kanazawa": {
        "name": "金沢",
        "coords": [
            388329.4,
            76010.41
        ],
        "region": "EU",
        "companies": []
    },
    "kawasaki": {
        "name": "川崎",
        "coords": [
            417324.8,
            87491.74
        ],
        "region": "EU",
        "companies": []
    },
    "kitakyusyu": {
        "name": "北九州",
        "coords": [
            338418.2,
            104345.0
        ],
        "region": "EU",
        "companies": []
    },
    "kobe": {
        "name": "神戸",
        "coords": [
            375959.1,
            95243.5
        ],
        "region": "EU",
        "companies": []
    },
    "kurobe": {
        "name": "黒部",
        "coords": [
            394749.3,
            72873.31
        ],
        "region": "EU",
        "companies": []
    },
    "matsumoto": {
        "name": "松本",
        "coords": [
            397450.2,
            80232.0
        ],
        "region": "EU",
        "companies": []
    },
    "matsuyama": {
        "name": "松山",
        "coords": [
            354381.9,
            104719.8
        ],
        "region": "EU",
        "companies": []
    },
    "miyoshi": {
        "name": "三好",
        "coords": [
            365247.3,
            102068.7
        ],
        "region": "EU",
        "companies": []
    },
    "nishinomiya": {
        "name": "西宮",
        "coords": [
            377562.4,
            95333.13
        ],
        "region": "EU",
        "companies": []
    },
    "osaka": {
        "name": "大阪",
        "coords": [
            380273.6,
            96114.58
        ],
        "region": "EU",
        "companies": []
    },
    "saijo": {
        "name": "西条",
        "coords": [
            357888.3,
            103686.0
        ],
        "region": "EU",
        "companies": []
    },
    "seiyo": {
        "name": "西予",
        "coords": [
            354895.9,
            106829.1
        ],
        "region": "EU",
        "companies": []
    },
    "shikokuchuo": {
        "name": "四国中央",
        "coords": [
            360769.2,
            103238.8
        ],
        "region": "EU",
        "companies": []
    },
    "shirakawa": {
        "name": "白川村（飛騨）",
        "coords": [
            391099.1,
            78144.34
        ],
        "region": "EU",
        "companies": []
    },
    "suita": {
        "name": "吹田",
        "coords": [
            379125.3,
            92762.62
        ],
        "region": "EU",
        "companies": []
    },
    "suzuka": {
        "name": "鈴鹿",
        "coords": [
            370502.6,
            114099.7
        ],
        "region": "EU",
        "companies": []
    },
    "takayama": {
        "name": "高山",
        "coords": [
            394231.7,
            79806.71
        ],
        "region": "EU",
        "companies": []
    },
    "tokushima": {
        "name": "徳島",
        "coords": [
            369815.4,
            103230.8
        ],
        "region": "EU",
        "companies": []
    },
    "tokyo": {
        "name": "東京",
        "coords": [
            418610.0,
            84303.38
        ],
        "region": "EU",
        "companies": []
    },
    "toyama": {
        "name": "富山",
        "coords": [
            393468.8,
            74018.3
        ],
        "region": "EU",
        "companies": []
    },
    "toyonaka": {
        "name": "豊中",
        "coords": [
            378648.5,
            94565.09
        ],
        "region": "EU",
        "companies": []
    },
    "yokohama": {
        "name": "横浜",
        "coords": [
            415434.7,
            91503.34
        ],
        "region": "EU",
        "companies": []
    },
    "abatskoe": {
        "name": "Абатское",
        "coords": [
            175179.1,
            -94620.88
        ],
        "region": "EU",
        "companies": []
    },
    "akyar": {
        "name": "Акъяр",
        "coords": [
            159839.3,
            -49934.96
        ],
        "region": "EU",
        "companies": []
    },
    "almetevsk": {
        "name": "Альметьевск",
        "coords": [
            133016.0,
            -54956.61
        ],
        "region": "EU",
        "companies": []
    },
    "argayash": {
        "name": "Аргаяш",
        "coords": [
            153951.9,
            -70801.59
        ],
        "region": "EU",
        "companies": []
    },
    "arsk": {
        "name": "Арск",
        "coords": [
            120890.6,
            -59315.5
        ],
        "region": "EU",
        "companies": []
    },
    "asbest": {
        "name": "Асбест",
        "coords": [
            150035.4,
            -83341.09
        ],
        "region": "EU",
        "companies": []
    },
    "asha": {
        "name": "Аша",
        "coords": [
            146108.9,
            -62536.16
        ],
        "region": "EU",
        "companies": []
    },
    "barkhatovo": {
        "name": "Бархатово",
        "coords": [
            161285.0,
            -83289.68
        ],
        "region": "EU",
        "companies": []
    },
    "bavly": {
        "name": "Бавлы",
        "coords": [
            136625.2,
            -52968.19
        ],
        "region": "EU",
        "companies": []
    },
    "baymak": {
        "name": "Баймак",
        "coords": [
            156802.4,
            -51492.9
        ],
        "region": "EU",
        "companies": []
    },
    "beloretsk": {
        "name": "Белорецк",
        "coords": [
            153032.5,
            -58986.11
        ],
        "region": "EU",
        "companies": []
    },
    "beloyarskiy": {
        "name": "Белоярский",
        "coords": [
            152158.8,
            -81689.55
        ],
        "region": "EU",
        "companies": []
    },
    "berduzhie": {
        "name": "Бердюжье",
        "coords": [
            172495.1,
            -87615.45
        ],
        "region": "EU",
        "companies": []
    },
    "berezovsky": {
        "name": "Берёзовский",
        "coords": [
            148475.9,
            -81203.22
        ],
        "region": "EU",
        "companies": []
    },
    "bogandinsky": {
        "name": "Богандинский",
        "coords": [
            163830.9,
            -88368.33
        ],
        "region": "EU",
        "companies": []
    },
    "bogdanovich": {
        "name": "Богданович",
        "coords": [
            153539.5,
            -82210.44
        ],
        "region": "EU",
        "companies": []
    },
    "bugulma": {
        "name": "Бугульма",
        "coords": [
            135365.6,
            -54005.66
        ],
        "region": "EU",
        "companies": []
    },
    "chastoozerie": {
        "name": "Частоозерье",
        "coords": [
            171859.8,
            -85989.42
        ],
        "region": "EU",
        "companies": []
    },
    "chelyabinsk": {
        "name": "Челябинск",
        "coords": [
            157251.0,
            -71193.15
        ],
        "region": "EU",
        "companies": []
    },
    "chervishevo": {
        "name": "Червишево",
        "coords": [
            161671.5,
            -86189.27
        ],
        "region": "EU",
        "companies": []
    },
    "chistopol": {
        "name": "Чистополь",
        "coords": [
            126772.9,
            -54972.55
        ],
        "region": "EU",
        "companies": []
    },
    "ekat": {
        "name": "Екатеринбург",
        "coords": [
            147576.6,
            -78289.63
        ],
        "region": "EU",
        "companies": []
    },
    "formachevo": {
        "name": "Станция Формачёво",
        "coords": [
            158986.9,
            -68168.78
        ],
        "region": "EU",
        "companies": []
    },
    "gay": {
        "name": "Гай",
        "coords": [
            159621.4,
            -47751.18
        ],
        "region": "EU",
        "companies": []
    },
    "golishmanovo": {
        "name": "Голышманово",
        "coords": [
            170723.9,
            -89999.16
        ],
        "region": "EU",
        "companies": []
    },
    "inzer": {
        "name": "Инзер",
        "coords": [
            150536.9,
            -59500.18
        ],
        "region": "EU",
        "companies": []
    },
    "isetskoe": {
        "name": "Исетское",
        "coords": [
            162172.8,
            -84141.65
        ],
        "region": "EU",
        "companies": []
    },
    "ishim": {
        "name": "Ишим",
        "coords": [
            174555.0,
            -92069.98
        ],
        "region": "EU",
        "companies": []
    },
    "isilkul": {
        "name": "Исилькуль",
        "coords": [
            183385.4,
            -89899.18
        ],
        "region": "EU",
        "companies": []
    },
    "isyang": {
        "name": "Исянгулово",
        "coords": [
            152574.2,
            -48900.37
        ],
        "region": "EU",
        "companies": []
    },
    "kamenskur": {
        "name": "Каменск-Уральский",
        "coords": [
            155615.6,
            -77866.57
        ],
        "region": "EU",
        "companies": []
    },
    "kargapolie": {
        "name": "Каргаполье",
        "coords": [
            163799.6,
            -79661.42
        ],
        "region": "EU",
        "companies": []
    },
    "kazan": {
        "name": "Казань",
        "coords": [
            119299.2,
            -55874.78
        ],
        "region": "EU",
        "companies": []
    },
    "krutinka": {
        "name": "Крутинка",
        "coords": [
            179571.3,
            -96536.22
        ],
        "region": "EU",
        "companies": []
    },
    "kurgan": {
        "name": "Курган",
        "coords": [
            166905.6,
            -79791.63
        ],
        "region": "EU",
        "companies": []
    },
    "laishevo": {
        "name": "Лаишево",
        "coords": [
            122174.2,
            -53934.89
        ],
        "region": "EU",
        "companies": []
    },
    "magnitogorsk": {
        "name": "Магнитогорск",
        "coords": [
            156793.9,
            -57446.09
        ],
        "region": "EU",
        "companies": []
    },
    "makushino": {
        "name": "Макушино",
        "coords": [
            172832.4,
            -82470.03
        ],
        "region": "EU",
        "companies": []
    },
    "mamlut": {
        "name": "Mamlut",
        "coords": [
            176086.9,
            -82628.3
        ],
        "region": "EU",
        "companies": []
    },
    "miass": {
        "name": "Миасс",
        "coords": [
            155068.0,
            -66792.7
        ],
        "region": "EU",
        "companies": []
    },
    "miasskoe": {
        "name": "Миасское",
        "coords": [
            159478.0,
            -73159.08
        ],
        "region": "EU",
        "companies": []
    },
    "mishkino": {
        "name": "Мишкино",
        "coords": [
            163268.5,
            -75657.78
        ],
        "region": "EU",
        "companies": []
    },
    "moskalenky": {
        "name": "Москаленки",
        "coords": [
            184335.3,
            -91775.36
        ],
        "region": "EU",
        "companies": []
    },
    "novotroitsk": {
        "name": "Новотроицк",
        "coords": [
            161781.3,
            -46260.21
        ],
        "region": "EU",
        "companies": []
    },
    "oktyabrskiy": {
        "name": "Октябрьский",
        "coords": [
            137460.7,
            -53841.09
        ],
        "region": "EU",
        "companies": []
    },
    "omsk": {
        "name": "Омск",
        "coords": [
            186725.5,
            -95522.56
        ],
        "region": "EU",
        "companies": []
    },
    "orsk": {
        "name": "Орск",
        "coords": [
            162377.9,
            -47738.72
        ],
        "region": "EU",
        "companies": []
    },
    "petuhovo": {
        "name": "Петухово",
        "coords": [
            174796.9,
            -83071.53
        ],
        "region": "EU",
        "companies": []
    },
    "planoviy": {
        "name": "Плановый",
        "coords": [
            160107.6,
            -73737.91
        ],
        "region": "EU",
        "companies": []
    },
    "pyshma": {
        "name": "Пышма",
        "coords": [
            156212.8,
            -83396.94
        ],
        "region": "EU",
        "companies": []
    },
    "salavat": {
        "name": "Салават",
        "coords": [
            147404.9,
            -52098.19
        ],
        "region": "EU",
        "companies": []
    },
    "shadrinsk": {
        "name": "Шадринск",
        "coords": [
            160073.5,
            -78693.12
        ],
        "region": "EU",
        "companies": []
    },
    "shaksha": {
        "name": "Шакша",
        "coords": [
            142667.2,
            -60495.73
        ],
        "region": "EU",
        "companies": []
    },
    "shumikha": {
        "name": "Шумиха",
        "coords": [
            162968.7,
            -73687.41
        ],
        "region": "EU",
        "companies": []
    },
    "sibai": {
        "name": "Сибай",
        "coords": [
            158963.6,
            -52961.74
        ],
        "region": "EU",
        "companies": []
    },
    "sim": {
        "name": "Сим",
        "coords": [
            147591.3,
            -63131.84
        ],
        "region": "EU",
        "companies": []
    },
    "sterlitamak": {
        "name": "Стерлитамак",
        "coords": [
            147631.6,
            -54414.0
        ],
        "region": "EU",
        "companies": []
    },
    "sysert": {
        "name": "Сысерть",
        "coords": [
            150710.5,
            -75777.23
        ],
        "region": "EU",
        "companies": []
    },
    "troitsk": {
        "name": "Троицк",
        "coords": [
            161852.8,
            -66048.72
        ],
        "region": "EU",
        "companies": []
    },
    "tukalinsk": {
        "name": "Тюкалинск",
        "coords": [
            182451.4,
            -97651.61
        ],
        "region": "EU",
        "companies": []
    },
    "tulgan": {
        "name": "Тюльган",
        "coords": [
            150750.8,
            -49869.74
        ],
        "region": "EU",
        "companies": []
    },
    "tumen": {
        "name": "Тюмень",
        "coords": [
            160406.3,
            -89351.38
        ],
        "region": "EU",
        "companies": []
    },
    "ufa": {
        "name": "Уфа",
        "coords": [
            141292.5,
            -59044.03
        ],
        "region": "EU",
        "companies": []
    },
    "urgaza": {
        "name": "Ургаза",
        "coords": [
            159589.3,
            -51466.62
        ],
        "region": "EU",
        "companies": []
    },
    "uruzan": {
        "name": "Юрюзань",
        "coords": [
            153163.5,
            -64069.1
        ],
        "region": "EU",
        "companies": []
    },
    "ustkatav": {
        "name": "Усть-Катав",
        "coords": [
            150936.5,
            -63201.03
        ],
        "region": "EU",
        "companies": []
    },
    "uvelsky": {
        "name": "Увельский",
        "coords": [
            160676.5,
            -67778.08
        ],
        "region": "EU",
        "companies": []
    },
    "uzhnouralsk": {
        "name": "Южноуральск",
        "coords": [
            159205.5,
            -67193.48
        ],
        "region": "EU",
        "companies": []
    },
    "verhneuralsk": {
        "name": "Верхнеуральск",
        "coords": [
            156113.9,
            -61502.91
        ],
        "region": "EU",
        "companies": []
    },
    "yalutorovsk": {
        "name": "Ялуторовск",
        "coords": [
            165500.1,
            -88637.77
        ],
        "region": "EU",
        "companies": []
    },
    "zavodoukovsk": {
        "name": "Заводоуковск",
        "coords": [
            167599.0,
            -87324.98
        ],
        "region": "EU",
        "companies": []
    },
    "zlatoust": {
        "name": "Златоуст",
        "coords": [
            148862.5,
            -67286.98
        ],
        "region": "EU",
        "companies": []
    },
    "alekseevka": {
        "name": "Алексеевка",
        "coords": [
            137144.0,
            -43498.7
        ],
        "region": "EU",
        "companies": []
    },
    "buzuluk": {
        "name": "Бузулук",
        "coords": [
            139771.0,
            -42724.8
        ],
        "region": "EU",
        "companies": []
    },
    "kr": {
        "name": "Красный Яр",
        "coords": [
            135790.0,
            -46368.6
        ],
        "region": "EU",
        "companies": []
    },
    "kurumoch": {
        "name": "Курумоч",
        "coords": [
            132575.0,
            -45419.9
        ],
        "region": "EU",
        "companies": []
    },
    "novospasskoe": {
        "name": "Новоспасское",
        "coords": [
            124597.0,
            -39003.2
        ],
        "region": "EU",
        "companies": []
    },
    "nps": {
        "name": "НПС Самара",
        "coords": [
            137184.0,
            -41784.3
        ],
        "region": "EU",
        "companies": []
    },
    "samara": {
        "name": "Самара",
        "coords": [
            134744.0,
            -42478.2
        ],
        "region": "EU",
        "companies": []
    },
    "senn": {
        "name": "Сенной",
        "coords": [
            123714.0,
            -32870.7
        ],
        "region": "EU",
        "companies": []
    },
    "volsk": {
        "name": "Вольск",
        "coords": [
            126847.0,
            -33037.4
        ],
        "region": "EU",
        "companies": []
    },
    "volzskiy": {
        "name": "Волжский",
        "coords": [
            133209.0,
            -44746.2
        ],
        "region": "EU",
        "companies": []
    },
    "zhigulevsk": {
        "name": "Жигулёвск",
        "coords": [
            129968.0,
            -42613.1
        ],
        "region": "EU",
        "companies": []
    },
    "chepeck": {
        "name": "Кирово-Чепецк",
        "coords": [
            116784.3,
            -68377.08
        ],
        "region": "EU",
        "companies": []
    },
    "kotelnich": {
        "name": "Котельнич",
        "coords": [
            110529.1,
            -65145.06
        ],
        "region": "EU",
        "companies": []
    },
    "lebyajie": {
        "name": "Лебяжье",
        "coords": [
            117419.5,
            -61913.78
        ],
        "region": "EU",
        "companies": []
    },
    "manturovo": {
        "name": "Мантурово",
        "coords": [
            102176.3,
            -61323.47
        ],
        "region": "EU",
        "companies": []
    },
    "murashi": {
        "name": "Мураши",
        "coords": [
            109937.4,
            -73299.36
        ],
        "region": "EU",
        "companies": []
    },
    "nolinsk": {
        "name": "Нолинск",
        "coords": [
            117958.6,
            -63430.37
        ],
        "region": "EU",
        "companies": []
    },
    "obachevo": {
        "name": "Объячево",
        "coords": [
            109407.4,
            -77881.59
        ],
        "region": "EU",
        "companies": []
    },
    "orshanka": {
        "name": "Оршанка",
        "coords": [
            112434.8,
            -58580.4
        ],
        "region": "EU",
        "companies": []
    },
    "pijanka": {
        "name": "Пижанка",
        "coords": [
            113686.5,
            -60644.39
        ],
        "region": "EU",
        "companies": []
    },
    "shahunya": {
        "name": "Шахунья",
        "coords": [
            107395.2,
            -61918.89
        ],
        "region": "EU",
        "companies": []
    },
    "sharia": {
        "name": "Шарья",
        "coords": [
            102729.0,
            -64741.3
        ],
        "region": "EU",
        "companies": []
    },
    "siktivkar": {
        "name": "Сыктывкар",
        "coords": [
            109905.3,
            -86419.3
        ],
        "region": "EU",
        "companies": []
    },
    "slobodskoy": {
        "name": "Слободской",
        "coords": [
            116379.6,
            -72180.11
        ],
        "region": "EU",
        "companies": []
    },
    "sovetsk": {
        "name": "Советск",
        "coords": [
            114300.1,
            -62258.84
        ],
        "region": "EU",
        "companies": []
    },
    "suna": {
        "name": "Суна",
        "coords": [
            117536.4,
            -64598.95
        ],
        "region": "EU",
        "companies": []
    },
    "tuja": {
        "name": "Тужа",
        "coords": [
            110735.4,
            -62716.82
        ],
        "region": "EU",
        "companies": []
    },
    "urjum": {
        "name": "Уржум",
        "coords": [
            119790.8,
            -61414.46
        ],
        "region": "EU",
        "companies": []
    },
    "vahrushi": {
        "name": "Вахруши",
        "coords": [
            115521.2,
            -71115.72
        ],
        "region": "EU",
        "companies": []
    },
    "vizinga": {
        "name": "Визинга",
        "coords": [
            109460.8,
            -82837.14
        ],
        "region": "EU",
        "companies": []
    },
    "yaransk": {
        "name": "Яранск",
        "coords": [
            112569.4,
            -59719.65
        ],
        "region": "EU",
        "companies": []
    },
    "yoshkarola": {
        "name": "Йошкар-Ола",
        "coords": [
            112824.4,
            -57832.28
        ],
        "region": "EU",
        "companies": []
    },
    "arzamas": {
        "name": "Арзамас",
        "coords": [
            105475.5,
            -45342.63
        ],
        "region": "EU",
        "companies": []
    },
    "balakhna": {
        "name": "Балахна",
        "coords": [
            101451.1,
            -53164.02
        ],
        "region": "EU",
        "companies": []
    },
    "bogoyavlenie": {
        "name": "Богоявление",
        "coords": [
            105324.6,
            -48682.88
        ],
        "region": "EU",
        "companies": []
    },
    "chkalovsk": {
        "name": "Чкаловск",
        "coords": [
            100738.4,
            -54887.53
        ],
        "region": "EU",
        "companies": []
    },
    "dzerzhinsk": {
        "name": "Дзержинск",
        "coords": [
            100739.5,
            -51326.0
        ],
        "region": "EU",
        "companies": []
    },
    "kovrov": {
        "name": "Ковров",
        "coords": [
            97149.19,
            -49450.7
        ],
        "region": "EU",
        "companies": []
    },
    "kstovo": {
        "name": "Кстово",
        "coords": [
            106739.6,
            -51781.28
        ],
        "region": "EU",
        "companies": []
    },
    "lukoyanov": {
        "name": "Лукоянов",
        "coords": [
            110532.0,
            -45327.78
        ],
        "region": "EU",
        "companies": []
    },
    "nizhny": {
        "name": "Нижний Новгород",
        "coords": [
            104109.8,
            -52904.68
        ],
        "region": "EU",
        "companies": []
    },
    "saransk": {
        "name": "Саранск",
        "coords": [
            113243.8,
            -42269.25
        ],
        "region": "EU",
        "companies": []
    },
    "semenov": {
        "name": "Семёнов",
        "coords": [
            104802.1,
            -55448.84
        ],
        "region": "EU",
        "companies": []
    },
    "shuya": {
        "name": "Шуя",
        "coords": [
            96653.39,
            -52214.47
        ],
        "region": "EU",
        "companies": []
    },
    "vyazniki": {
        "name": "Вязники",
        "coords": [
            98547.19,
            -49037.93
        ],
        "region": "EU",
        "companies": []
    },
    "aleisk": {
        "name": "aleisk",
        "coords": [
            220272.0,
            -110442.0
        ],
        "region": "EU",
        "companies": []
    },
    "barnaul": {
        "name": "barnaul",
        "coords": [
            217189.0,
            -114517.0
        ],
        "region": "EU",
        "companies": []
    },
    "belokurikha": {
        "name": "belokurikha",
        "coords": [
            223802.0,
            -111649.0
        ],
        "region": "EU",
        "companies": []
    },
    "berdsk": {
        "name": "berdsk",
        "coords": [
            209003.0,
            -118297.0
        ],
        "region": "EU",
        "companies": []
    },
    "biysk": {
        "name": "biysk",
        "coords": [
            223696.0,
            -116684.0
        ],
        "region": "EU",
        "companies": []
    },
    "bochkaria": {
        "name": "bochkaria",
        "coords": [
            224020.0,
            -118853.0
        ],
        "region": "EU",
        "companies": []
    },
    "bolotnoe": {
        "name": "Bolotnoe",
        "coords": [
            206737.6,
            -123408.9
        ],
        "region": "EU",
        "companies": []
    },
    "bucanskoe": {
        "name": "bucanskoe",
        "coords": [
            215711.0,
            -110916.0
        ],
        "region": "EU",
        "companies": []
    },
    "cherepanovo": {
        "name": "cherepanovo",
        "coords": [
            211225.0,
            -117824.0
        ],
        "region": "EU",
        "companies": []
    },
    "chilinnoe": {
        "name": "chilinnoe",
        "coords": [
            221983.0,
            -119514.0
        ],
        "region": "EU",
        "companies": []
    },
    "elchovka": {
        "name": "Elchovka",
        "coords": [
            222743.3,
            -121773.9
        ],
        "region": "EU",
        "companies": []
    },
    "gornoaltaysk": {
        "name": "gornoaltaysk",
        "coords": [
            231492.0,
            -116588.0
        ],
        "region": "EU",
        "companies": []
    },
    "gramoteino": {
        "name": "Gramoteino",
        "coords": [
            218261.0,
            -124755.4
        ],
        "region": "EU",
        "companies": []
    },
    "kemerovo": {
        "name": "Kemerovo",
        "coords": [
            213471.2,
            -128838.5
        ],
        "region": "EU",
        "companies": []
    },
    "kislovka": {
        "name": "Kislovka",
        "coords": [
            203536.8,
            -127865.3
        ],
        "region": "EU",
        "companies": []
    },
    "kornilovo": {
        "name": "kornilovo",
        "coords": [
            208328.5,
            -124064.3
        ],
        "region": "EU",
        "companies": []
    },
    "kuibyshev": {
        "name": "kuibyshev",
        "coords": [
            219413.0,
            -102341.0
        ],
        "region": "EU",
        "companies": []
    },
    "kuzedeevo": {
        "name": "Kuzedeevo",
        "coords": [
            223623.9,
            -123251.6
        ],
        "region": "EU",
        "companies": []
    },
    "kytmanovo": {
        "name": "kytmanovo",
        "coords": [
            220024.0,
            -120062.0
        ],
        "region": "EU",
        "companies": []
    },
    "leninkuznec": {
        "name": "Leninkuznec",
        "coords": [
            215710.6,
            -124839.1
        ],
        "region": "EU",
        "companies": []
    },
    "linevo": {
        "name": "linevo",
        "coords": [
            210727.0,
            -118414.0
        ],
        "region": "EU",
        "companies": []
    },
    "mamontovo": {
        "name": "mamontovo",
        "coords": [
            216186.0,
            -107777.0
        ],
        "region": "EU",
        "companies": []
    },
    "martynovo": {
        "name": "martynovo",
        "coords": [
            221473.0,
            -120969.0
        ],
        "region": "EU",
        "companies": []
    },
    "moshkovo": {
        "name": "Moshkovo",
        "coords": [
            206910.5,
            -122099.8
        ],
        "region": "EU",
        "companies": []
    },
    "novoaltaysk": {
        "name": "novoaltaysk",
        "coords": [
            217119.0,
            -116469.0
        ],
        "region": "EU",
        "companies": []
    },
    "novobibeevo": {
        "name": "Novobibeevo",
        "coords": [
            205139.1,
            -123254.5
        ],
        "region": "EU",
        "companies": []
    },
    "novokuznetsk": {
        "name": "novokuznetsk",
        "coords": [
            222178.1,
            -124613.3
        ],
        "region": "EU",
        "companies": []
    },
    "oparino": {
        "name": "Oparino",
        "coords": [
            209061.6,
            -125529.4
        ],
        "region": "EU",
        "companies": []
    },
    "rubtsovsk": {
        "name": "Rubtsovsk",
        "coords": [
            221789.9,
            -100301.0
        ],
        "region": "EU",
        "companies": []
    },
    "smolenskoye": {
        "name": "smolenskoye",
        "coords": [
            223567.0,
            -114430.0
        ],
        "region": "EU",
        "companies": []
    },
    "talmenka": {
        "name": "talmenka",
        "coords": [
            212565.0,
            -117257.0
        ],
        "region": "EU",
        "companies": []
    },
    "tomsk": {
        "name": "Tomsk",
        "coords": [
            203107.7,
            -130838.2
        ],
        "region": "EU",
        "companies": []
    },
    "yurga": {
        "name": "Yurga",
        "coords": [
            207970.9,
            -126253.6
        ],
        "region": "EU",
        "companies": []
    },
    "zarinsk": {
        "name": "zarinsk",
        "coords": [
            217215.0,
            -120127.0
        ],
        "region": "EU",
        "companies": []
    },
    "arhangelsk": {
        "name": "Архангельск",
        "coords": [
            78768.36,
            -89503.66
        ],
        "region": "EU",
        "companies": []
    },
    "bereznik": {
        "name": "Березник",
        "coords": [
            83378.11,
            -84273.02
        ],
        "region": "EU",
        "companies": []
    },
    "cherepovets": {
        "name": "Череповец",
        "coords": [
            81352.36,
            -57683.59
        ],
        "region": "EU",
        "companies": []
    },
    "pogost": {
        "name": "Погост",
        "coords": [
            85703.58,
            -78027.78
        ],
        "region": "EU",
        "companies": []
    },
    "s": {
        "name": "Сергиев Посад",
        "coords": [
            89624.05,
            -46968.23
        ],
        "region": "EU",
        "companies": []
    },
    "severodvinsk": {
        "name": "Северодвинск",
        "coords": [
            74797.98,
            -87461.91
        ],
        "region": "EU",
        "companies": []
    },
    "velsk": {
        "name": "Вельск",
        "coords": [
            87816.64,
            -74173.44
        ],
        "region": "EU",
        "companies": []
    },
    "vologda": {
        "name": "Вологда",
        "coords": [
            87195.75,
            -61433.1
        ],
        "region": "EU",
        "companies": []
    },
    "yaroslavl": {
        "name": "Ярославль",
        "coords": [
            90258.98,
            -54546.04
        ],
        "region": "EU",
        "companies": []
    },
    "g": {
        "name": "Гусь Хрустальный",
        "coords": [
            97041.26,
            -42743.49
        ],
        "region": "EU",
        "companies": []
    },
    "kasimov": {
        "name": "Касимов",
        "coords": [
            99603.16,
            -41029.15
        ],
        "region": "EU",
        "companies": []
    },
    "kurlovo": {
        "name": "Курлово",
        "coords": [
            96645.23,
            -41160.68
        ],
        "region": "EU",
        "companies": []
    },
    "murom": {
        "name": "Муром",
        "coords": [
            100586.8,
            -43610.65
        ],
        "region": "EU",
        "companies": []
    },
    "sasovo": {
        "name": "Сасово",
        "coords": [
            101668.7,
            -38010.41
        ],
        "region": "EU",
        "companies": []
    },
    "shumerlya": {
        "name": "Шумерля",
        "coords": [
            112828.4,
            -49484.27
        ],
        "region": "EU",
        "companies": []
    },
    "tum": {
        "name": "Тума",
        "coords": [
            96807.55,
            -40280.75
        ],
        "region": "EU",
        "companies": []
    },
    "vladimir": {
        "name": "Владимир",
        "coords": [
            95146.88,
            -45077.95
        ],
        "region": "EU",
        "companies": []
    },
    "balabanovo": {
        "name": "Балабаново",
        "coords": [
            85499.8,
            -35196.2
        ],
        "region": "EU",
        "companies": []
    },
    "obninskcntrl": {
        "name": "Обнинск",
        "coords": [
            85434.1,
            -34413.6
        ],
        "region": "EU",
        "companies": []
    },
    "selyatino": {
        "name": "Селятино",
        "coords": [
            85641.6,
            -36741.6
        ],
        "region": "EU",
        "companies": []
    },
    "vorsino": {
        "name": "Ворсино",
        "coords": [
            86048.4,
            -35404.6
        ],
        "region": "EU",
        "companies": []
    },
    "zvenigorod": {
        "name": "Звенигород",
        "coords": [
            85489.4,
            -39235.2
        ],
        "region": "EU",
        "companies": []
    },
    "kiritsy": {
        "name": "Кирицы",
        "coords": [
            98861.55,
            -37418.59
        ],
        "region": "EU",
        "companies": []
    },
    "krslob": {
        "name": "Краснослободск",
        "coords": [
            106830.3,
            -42358.85
        ],
        "region": "EU",
        "companies": []
    },
    "n": {
        "name": "Нижний Ломов",
        "coords": [
            109894.3,
            -36469.02
        ],
        "region": "EU",
        "companies": []
    },
    "ryazan": {
        "name": "Рязань",
        "coords": [
            95838.21,
            -37864.16
        ],
        "region": "EU",
        "companies": []
    },
    "shilovo": {
        "name": "Шилово",
        "coords": [
            99617.0,
            -37068.18
        ],
        "region": "EU",
        "companies": []
    },
    "spassk": {
        "name": "Спасск",
        "coords": [
            107619.3,
            -37982.56
        ],
        "region": "EU",
        "companies": []
    },
    "torbeevo": {
        "name": "Торбеево",
        "coords": [
            106861.4,
            -39887.77
        ],
        "region": "EU",
        "companies": []
    },
    "umet": {
        "name": "Умёт",
        "coords": [
            104869.8,
            -38613.68
        ],
        "region": "EU",
        "companies": []
    },
    "z": {
        "name": "Зубова Поляна",
        "coords": [
            105713.8,
            -38184.91
        ],
        "region": "EU",
        "companies": []
    },
    "oshtrowrus": {
        "name": "Oshtrow Russkyia",
        "coords": [
            108637.5,
            -208953.7
        ],
        "region": "EU",
        "companies": []
    },
    "bokino": {
        "name": "Бокино",
        "coords": [
            108844.7,
            -26320.8
        ],
        "region": "EU",
        "companies": []
    },
    "kotovsk": {
        "name": "Котовск",
        "coords": [
            110292.4,
            -25825.74
        ],
        "region": "EU",
        "companies": []
    },
    "stroitell": {
        "name": "Строитель",
        "coords": [
            108420.0,
            -27367.56
        ],
        "region": "EU",
        "companies": []
    },
    "znamenka": {
        "name": "Знаменка",
        "coords": [
            112039.7,
            -24328.88
        ],
        "region": "EU",
        "companies": []
    },
    "anavgay": {
        "name": "Анавгай",
        "coords": [
            230313.1,
            -348577.7
        ],
        "region": "EU",
        "companies": []
    },
    "atka": {
        "name": "Атка",
        "coords": [
            211244.4,
            -320488.2
        ],
        "region": "EU",
        "companies": []
    },
    "debin": {
        "name": "Дебин",
        "coords": [
            205165.0,
            -315592.8
        ],
        "region": "EU",
        "companies": []
    },
    "dudinka": {
        "name": "Дудинка",
        "coords": [
            143265.4,
            -174617.7
        ],
        "region": "EU",
        "companies": []
    },
    "kliuchi": {
        "name": "Ключи",
        "coords": [
            224830.8,
            -355946.3
        ],
        "region": "EU",
        "companies": []
    },
    "kovran": {
        "name": "Ковран",
        "coords": [
            224427.3,
            -342073.0
        ],
        "region": "EU",
        "companies": []
    },
    "kozyrevsk": {
        "name": "Козыревск",
        "coords": [
            227486.8,
            -353885.5
        ],
        "region": "EU",
        "companies": []
    },
    "levinskie": {
        "name": "Левинские Пески",
        "coords": [
            142069.6,
            -174252.0
        ],
        "region": "EU",
        "companies": []
    },
    "magadan": {
        "name": "Магадан",
        "coords": [
            218752.6,
            -320147.2
        ],
        "region": "EU",
        "companies": []
    },
    "mayskoye": {
        "name": "Майское",
        "coords": [
            225589.6,
            -353693.5
        ],
        "region": "EU",
        "companies": []
    },
    "messoyakha": {
        "name": "Мессояха",
        "coords": [
            143398.9,
            -159926.0
        ],
        "region": "EU",
        "companies": []
    },
    "myaundzha": {
        "name": "Мяунджа",
        "coords": [
            203571.3,
            -305880.7
        ],
        "region": "EU",
        "companies": []
    },
    "norilsk": {
        "name": "Норильск",
        "coords": [
            146218.9,
            -176928.3
        ],
        "region": "EU",
        "companies": []
    },
    "novozapol": {
        "name": "Новозаполярний",
        "coords": [
            147650.0,
            -152906.6
        ],
        "region": "EU",
        "companies": []
    },
    "orotukan": {
        "name": "Оротукан",
        "coords": [
            203887.2,
            -317973.1
        ],
        "region": "EU",
        "companies": []
    },
    "palatka": {
        "name": "Палатка",
        "coords": [
            215554.5,
            -319670.4
        ],
        "region": "EU",
        "companies": []
    },
    "potapovo": {
        "name": "Потапово",
        "coords": [
            147649.2,
            -172353.9
        ],
        "region": "EU",
        "companies": []
    },
    "severo": {
        "name": "Се́веро-Кури́льск",
        "coords": [
            262175.3,
            -352685.5
        ],
        "region": "EU",
        "companies": []
    },
    "snezhnogorsk": {
        "name": "Снежногорск",
        "coords": [
            152825.4,
            -172539.9
        ],
        "region": "EU",
        "companies": []
    },
    "sokol": {
        "name": "Сокол",
        "coords": [
            216783.5,
            -319860.1
        ],
        "region": "EU",
        "companies": []
    },
    "susuman": {
        "name": "Сусуман",
        "coords": [
            204982.8,
            -307852.6
        ],
        "region": "EU",
        "companies": []
    },
    "talnakh": {
        "name": "Талнах",
        "coords": [
            146224.2,
            -178638.9
        ],
        "region": "EU",
        "companies": []
    },
    "tazovskiy": {
        "name": "Тазовский",
        "coords": [
            143164.7,
            -153619.9
        ],
        "region": "EU",
        "companies": []
    },
    "tukhard": {
        "name": "Тухард",
        "coords": [
            141913.0,
            -170523.2
        ],
        "region": "EU",
        "companies": []
    },
    "urengoy": {
        "name": "Уренгой",
        "coords": [
            149470.8,
            -147686.4
        ],
        "region": "EU",
        "companies": []
    },
    "yagodnoye": {
        "name": "Ягодное",
        "coords": [
            204873.0,
            -312143.9
        ],
        "region": "EU",
        "companies": []
    },
    "achinsk": {
        "name": "Ачинск",
        "coords": [
            214396.9,
            -143013.0
        ],
        "region": "EU",
        "companies": []
    },
    "aginskoe": {
        "name": "Агинское",
        "coords": [
            270450.8,
            -207193.5
        ],
        "region": "EU",
        "companies": []
    },
    "aldan": {
        "name": "Алдан",
        "coords": [
            233059.0,
            -247555.7
        ],
        "region": "EU",
        "companies": []
    },
    "artyk": {
        "name": "Артык",
        "coords": [
            197438.5,
            -299054.3
        ],
        "region": "EU",
        "companies": []
    },
    "baikalsk": {
        "name": "Байкальск",
        "coords": [
            258380.4,
            -172234.1
        ],
        "region": "EU",
        "companies": []
    },
    "barabinsk": {
        "name": "Барабинск",
        "coords": [
            194509.6,
            -107665.1
        ],
        "region": "EU",
        "companies": []
    },
    "belushiaguba": {
        "name": "belushiaguba",
        "coords": [
            84871.66,
            -137693.5
        ],
        "region": "EU",
        "companies": []
    },
    "birobizhan": {
        "name": "Биробиджан",
        "coords": [
            288821.0,
            -272647.6
        ],
        "region": "EU",
        "companies": []
    },
    "bolotnoye": {
        "name": "Болотное",
        "coords": [
            206661.1,
            -125286.4
        ],
        "region": "EU",
        "companies": []
    },
    "borzya": {
        "name": "Борзя",
        "coords": [
            276022.8,
            -212985.2
        ],
        "region": "EU",
        "companies": []
    },
    "bugrino": {
        "name": "bugrino",
        "coords": [
            87757.98,
            -119694.7
        ],
        "region": "EU",
        "companies": []
    },
    "byelgorsk": {
        "name": "Белогорск",
        "coords": [
            276347.0,
            -256326.6
        ],
        "region": "EU",
        "companies": []
    },
    "chernyshevsk": {
        "name": "Чернышевск",
        "coords": [
            265816.7,
            -214293.4
        ],
        "region": "EU",
        "companies": []
    },
    "chita": {
        "name": "Чита",
        "coords": [
            264140.0,
            -205094.0
        ],
        "region": "EU",
        "companies": []
    },
    "chulman": {
        "name": "Чульман",
        "coords": [
            243135.4,
            -245385.3
        ],
        "region": "EU",
        "companies": []
    },
    "churapcha": {
        "name": "Чурапча",
        "coords": [
            214006.2,
            -266762.7
        ],
        "region": "EU",
        "companies": []
    },
    "dalniechersk": {
        "name": "Дальнереченск",
        "coords": [
            306526.5,
            -275854.7
        ],
        "region": "EU",
        "companies": []
    },
    "drovyanoi": {
        "name": "drovyanoi",
        "coords": [
            112597.6,
            -165244.7
        ],
        "region": "EU",
        "companies": []
    },
    "erofeypav": {
        "name": "Ерофей Павлович",
        "coords": [
            258968.1,
            -235180.3
        ],
        "region": "EU",
        "companies": []
    },
    "irkutsk": {
        "name": "Иркутск",
        "coords": [
            254244.3,
            -174325.8
        ],
        "region": "EU",
        "companies": []
    },
    "kalachinsk": {
        "name": "Калачинск",
        "coords": [
            189989.8,
            -99502.5
        ],
        "region": "EU",
        "companies": []
    },
    "kansk": {
        "name": "Канск",
        "coords": [
            222785.5,
            -157156.4
        ],
        "region": "EU",
        "companies": []
    },
    "kargat": {
        "name": "Каргат",
        "coords": [
            200906.2,
            -113342.9
        ],
        "region": "EU",
        "companies": []
    },
    "khabarovsk": {
        "name": "Хабаровск",
        "coords": [
            290598.4,
            -280873.8
        ],
        "region": "EU",
        "companies": []
    },
    "khandyga": {
        "name": "Хандыга",
        "coords": [
            209505.4,
            -275661.7
        ],
        "region": "EU",
        "companies": []
    },
    "khilok": {
        "name": "Хилок",
        "coords": [
            265767.8,
            -193656.5
        ],
        "region": "EU",
        "companies": []
    },
    "kholmsk": {
        "name": "Холмск",
        "coords": [
            295264.4,
            -307938.4
        ],
        "region": "EU",
        "companies": []
    },
    "komsomolskru": {
        "name": "Комсомольск-на-Амуре",
        "coords": [
            273694.4,
            -285866.1
        ],
        "region": "EU",
        "companies": []
    },
    "korsakov": {
        "name": "Корсаков",
        "coords": [
            296302.3,
            -311405.2
        ],
        "region": "EU",
        "companies": []
    },
    "krasnoyarsk": {
        "name": "Красноярск",
        "coords": [
            219569.3,
            -149157.7
        ],
        "region": "EU",
        "companies": []
    },
    "kyemerovo": {
        "name": "Кемерово",
        "coords": [
            210973.7,
            -128960.7
        ],
        "region": "EU",
        "companies": []
    },
    "lidoga": {
        "name": "Лидога",
        "coords": [
            283487.6,
            -286105.8
        ],
        "region": "EU",
        "companies": []
    },
    "magadachi": {
        "name": "Магдагачи",
        "coords": [
            263127.6,
            -248384.4
        ],
        "region": "EU",
        "companies": []
    },
    "mariinsk": {
        "name": "Мариинск",
        "coords": [
            210328.4,
            -135648.9
        ],
        "region": "EU",
        "companies": []
    },
    "mogocha": {
        "name": "Могоча",
        "coords": [
            258369.3,
            -231307.4
        ],
        "region": "EU",
        "companies": []
    },
    "mudanjiang": {
        "name": "牡丹江",
        "coords": [
            313385.8,
            -259837.9
        ],
        "region": "EU",
        "companies": []
    },
    "nakhodka": {
        "name": "Нахо́дка",
        "coords": [
            322707.1,
            -273706.5
        ],
        "region": "EU",
        "companies": []
    },
    "never": {
        "name": "Невер",
        "coords": [
            259804.4,
            -241274.6
        ],
        "region": "EU",
        "companies": []
    },
    "nizhneudinsk": {
        "name": "Нижнеудинск",
        "coords": [
            233421.0,
            -163763.1
        ],
        "region": "EU",
        "companies": []
    },
    "nizhnii": {
        "name": "Нижний Бестях",
        "coords": [
            214771.1,
            -261319.5
        ],
        "region": "EU",
        "companies": []
    },
    "novobruetsky": {
        "name": "Новобурейский",
        "coords": [
            282902.7,
            -260303.9
        ],
        "region": "EU",
        "companies": []
    },
    "novosibirsk": {
        "name": "Новосибирск",
        "coords": [
            205928.5,
            -118147.8
        ],
        "region": "EU",
        "companies": []
    },
    "pzabai": {
        "name": "Петровск-Забайкальский",
        "coords": [
            264429.3,
            -187180.3
        ],
        "region": "EU",
        "companies": []
    },
    "rogachovo": {
        "name": "rogachovo",
        "coords": [
            84607.73,
            -140135.0
        ],
        "region": "EU",
        "companies": []
    },
    "selichino": {
        "name": "Селихино",
        "coords": [
            277463.2,
            -285631.7
        ],
        "region": "EU",
        "companies": []
    },
    "shimanovsk": {
        "name": "Шимановск",
        "coords": [
            268515.8,
            -252198.9
        ],
        "region": "EU",
        "companies": []
    },
    "skovorodino": {
        "name": "Сковородино",
        "coords": [
            258550.0,
            -240138.1
        ],
        "region": "EU",
        "companies": []
    },
    "spask": {
        "name": "Спасск-Дальний",
        "coords": [
            313821.8,
            -273629.0
        ],
        "region": "EU",
        "companies": []
    },
    "tayshet": {
        "name": "Тайшет",
        "coords": [
            227371.6,
            -163342.0
        ],
        "region": "EU",
        "companies": []
    },
    "tommot": {
        "name": "Томмот",
        "coords": [
            231155.0,
            -249977.8
        ],
        "region": "EU",
        "companies": []
    },
    "tonghua": {
        "name": "通化",
        "coords": [
            327364.5,
            -246332.5
        ],
        "region": "EU",
        "companies": []
    },
    "tynda": {
        "name": "Тында",
        "coords": [
            252632.7,
            -244151.4
        ],
        "region": "EU",
        "companies": []
    },
    "tyukalinsk": {
        "name": "Тюкалинск",
        "coords": [
            179782.8,
            -95046.19
        ],
        "region": "EU",
        "companies": []
    },
    "ulanude": {
        "name": "Улан-Удэ",
        "coords": [
            260190.8,
            -184257.9
        ],
        "region": "EU",
        "companies": []
    },
    "ulu": {
        "name": "Улу",
        "coords": [
            223121.0,
            -254246.3
        ],
        "region": "EU",
        "companies": []
    },
    "ulyoty": {
        "name": "Улеты",
        "coords": [
            267551.7,
            -200589.9
        ],
        "region": "EU",
        "companies": []
    },
    "ussuriysk": {
        "name": "Уссури́йск",
        "coords": [
            316683.5,
            -271637.5
        ],
        "region": "EU",
        "companies": []
    },
    "ustn": {
        "name": "Усть-Нера",
        "coords": [
            196049.1,
            -293363.9
        ],
        "region": "EU",
        "companies": []
    },
    "vakkanai": {
        "name": "稚内市",
        "coords": [
            304011.5,
            -308321.5
        ],
        "region": "EU",
        "companies": []
    },
    "vanino": {
        "name": "Ванино",
        "coords": [
            286491.3,
            -299202.0
        ],
        "region": "EU",
        "companies": []
    },
    "vladyvostok": {
        "name": "Владивосток",
        "coords": [
            320830.6,
            -269393.8
        ],
        "region": "EU",
        "companies": []
    },
    "yakutsk": {
        "name": "Якутск",
        "coords": [
            213407.0,
            -260164.3
        ],
        "region": "EU",
        "companies": []
    },
    "yuzhno": {
        "name": "Южно-Сахалинск",
        "coords": [
            294605.0,
            -309735.1
        ],
        "region": "EU",
        "companies": []
    },
    "zima": {
        "name": "Зима",
        "coords": [
            242509.0,
            -170989.7
        ],
        "region": "EU",
        "companies": []
    },
    "abbbad": {
        "name": "Abbottabad",
        "coords": [
            266257.5,
            -16830.57
        ],
        "region": "EU",
        "companies": []
    },
    "abdolhaqq": {
        "name": "'Abd ol Haqq",
        "coords": [
            232550.0,
            15858.3
        ],
        "region": "EU",
        "companies": []
    },
    "abeche": {
        "name": "Abéché",
        "coords": [
            56089.5,
            217868.0
        ],
        "region": "EU",
        "companies": []
    },
    "adre": {
        "name": "Adre",
        "coords": [
            62303.7,
            219326.0
        ],
        "region": "EU",
        "companies": []
    },
    "albad2": {
        "name": "Al Bad'",
        "coords": [
            117591.4,
            113034.4
        ],
        "region": "EU",
        "companies": []
    },
    "alkhuraybah": {
        "name": "Alkhuraybah",
        "coords": [
            119755.0,
            115484.0
        ],
        "region": "EU",
        "companies": []
    },
    "alqatrun": {
        "name": "Al Qatrun",
        "coords": [
            13184.2,
            149245.0
        ],
        "region": "EU",
        "companies": []
    },
    "alqusayr": {
        "name": "Al Qusayr",
        "coords": [
            121774.0,
            127982.3
        ],
        "region": "EU",
        "companies": []
    },
    "alsharaf": {
        "name": "Alsharaf",
        "coords": [
            118555.0,
            108585.0
        ],
        "region": "EU",
        "companies": []
    },
    "alubayyid": {
        "name": "Al-Ubayyid",
        "coords": [
            116464.0,
            215109.0
        ],
        "region": "EU",
        "companies": []
    },
    "alwajh": {
        "name": "Al Wajh",
        "coords": [
            132291.0,
            126265.0
        ],
        "region": "EU",
        "companies": []
    },
    "amol": {
        "name": "Amol",
        "coords": [
            184253.9,
            36974.75
        ],
        "region": "EU",
        "companies": []
    },
    "andkhoy": {
        "name": "Andkhoy",
        "coords": [
            232435.0,
            1158.32
        ],
        "region": "EU",
        "companies": []
    },
    "ashgabat": {
        "name": "Aşgabat",
        "coords": [
            205004.0,
            15339.9
        ],
        "region": "EU",
        "companies": []
    },
    "ashshwayrif": {
        "name": "Ash Shwayrif",
        "coords": [
            12083.1,
            118925.0
        ],
        "region": "EU",
        "companies": []
    },
    "astara": {
        "name": "Astara",
        "coords": [
            165103.7,
            35357.87
        ],
        "region": "EU",
        "companies": []
    },
    "atiabroki": {
        "name": "Ati",
        "coords": [
            39798.3,
            222563.0
        ],
        "region": "EU",
        "companies": []
    },
    "babol": {
        "name": "Babol",
        "coords": [
            184928.6,
            36120.24
        ],
        "region": "EU",
        "companies": []
    },
    "bagnotar": {
        "name": "Bagnotar",
        "coords": [
            269184.3,
            -15227.57
        ],
        "region": "EU",
        "companies": []
    },
    "baherden": {
        "name": "Bäherden",
        "coords": [
            198439.0,
            15567.3
        ],
        "region": "EU",
        "companies": []
    },
    "balkanabat": {
        "name": "Balkanabat",
        "coords": [
            183997.0,
            17283.6
        ],
        "region": "EU",
        "companies": []
    },
    "barakahu": {
        "name": "Barakahu",
        "coords": [
            273589.2,
            -12786.4
        ],
        "region": "EU",
        "companies": []
    },
    "baysun": {
        "name": "Boysun",
        "coords": [
            235627.0,
            -11428.6
        ],
        "region": "EU",
        "companies": []
    },
    "bhalwal": {
        "name": "Bhalwal",
        "coords": [
            278843.3,
            -3498.316
        ],
        "region": "EU",
        "companies": []
    },
    "bilasuvar": {
        "name": "Bilasuvar",
        "coords": [
            160822.1,
            29795.07
        ],
        "region": "EU",
        "companies": []
    },
    "bileomara": {
        "name": "Bile Omara",
        "coords": [
            33411.0,
            203404.0
        ],
        "region": "EU",
        "companies": []
    },
    "bishkek": {
        "name": "Бишкек",
        "coords": [
            239874.0,
            -51816.5
        ],
        "region": "EU",
        "companies": []
    },
    "bukhara": {
        "name": "Buxoro",
        "coords": [
            219550.0,
            -9897.66
        ],
        "region": "EU",
        "companies": []
    },
    "burush": {
        "name": "Burush",
        "coords": [
            94690.9,
            215965.0
        ],
        "region": "EU",
        "companies": []
    },
    "chakri": {
        "name": "Chakri",
        "coords": [
            274280.8,
            -7494.176
        ],
        "region": "EU",
        "companies": []
    },
    "chalus": {
        "name": "Chalus",
        "coords": [
            180013.1,
            37884.8
        ],
        "region": "EU",
        "companies": []
    },
    "chaman": {
        "name": "Chaman",
        "coords": [
            260714.0,
            24216.7
        ],
        "region": "EU",
        "companies": []
    },
    "chongju": {
        "name": "정주",
        "coords": [
            339880.0,
            -240720.0
        ],
        "region": "EU",
        "companies": []
    },
    "corfu": {
        "name": "Κέρκυρα",
        "coords": [
            38486.17,
            62311.61
        ],
        "region": "EU",
        "companies": []
    },
    "dahaban": {
        "name": "Dahaban",
        "coords": [
            113712.0,
            110822.0
        ],
        "region": "EU",
        "companies": []
    },
    "dalian": {
        "name": "大连",
        "coords": [
            343252.0,
            -224730.0
        ],
        "region": "EU",
        "companies": []
    },
    "dandong": {
        "name": "丹东",
        "coords": [
            337580.0,
            -236998.0
        ],
        "region": "EU",
        "companies": []
    },
    "darautkgn": {
        "name": "Дароот-Коргон",
        "coords": [
            247211.0,
            -32404.2
        ],
        "region": "EU",
        "companies": []
    },
    "darvaza": {
        "name": "Derweze",
        "coords": [
            195969.0,
            4422.67
        ],
        "region": "EU",
        "companies": []
    },
    "dasoguz": {
        "name": "Daşoguz",
        "coords": [
            196690.0,
            -7188.28
        ],
        "region": "EU",
        "companies": []
    },
    "delaram": {
        "name": "Delaram",
        "coords": [
            243394.0,
            28407.3
        ],
        "region": "EU",
        "companies": []
    },
    "denov": {
        "name": "Denov",
        "coords": [
            237256.0,
            -13199.6
        ],
        "region": "EU",
        "companies": []
    },
    "derbent": {
        "name": "Derbent",
        "coords": [
            234923.0,
            -10109.0
        ],
        "region": "EU",
        "companies": []
    },
    "dikhan": {
        "name": "Dera Ismail Khan",
        "coords": [
            273480.0,
            5442.84
        ],
        "region": "EU",
        "companies": []
    },
    "djermaya": {
        "name": "Djermaya",
        "coords": [
            18269.1,
            227162.0
        ],
        "region": "EU",
        "companies": []
    },
    "dorasan": {
        "name": "도라산",
        "coords": [
            351272.0,
            -247585.0
        ],
        "region": "EU",
        "companies": []
    },
    "doubagos": {
        "name": "Doubabé Gos",
        "coords": [
            14687.2,
            231708.0
        ],
        "region": "EU",
        "companies": []
    },
    "duba1": {
        "name": "Dubaa",
        "coords": [
            125716.9,
            121014.8
        ],
        "region": "EU",
        "companies": []
    },
    "dushanbe": {
        "name": "Душанбе",
        "coords": [
            239351.0,
            -16971.4
        ],
        "region": "EU",
        "companies": []
    },
    "dzhiland": {
        "name": "Ҷиланд",
        "coords": [
            255000.0,
            -24846.3
        ],
        "region": "EU",
        "companies": []
    },
    "eltor": {
        "name": "El Tor",
        "coords": [
            108952.0,
            113410.0
        ],
        "region": "EU",
        "companies": []
    },
    "esenguly": {
        "name": "Esenguly",
        "coords": [
            188098.0,
            27679.8
        ],
        "region": "EU",
        "companies": []
    },
    "fashir": {
        "name": "Al-Fashir",
        "coords": [
            84199.6,
            217198.0
        ],
        "region": "EU",
        "companies": []
    },
    "faya": {
        "name": "Faya-Largeau",
        "coords": [
            39661.2,
            180104.0
        ],
        "region": "EU",
        "companies": []
    },
    "fjang": {
        "name": "Fateh Jang",
        "coords": [
            271515.1,
            -5400.16
        ],
        "region": "EU",
        "companies": []
    },
    "fotokol": {
        "name": "Fotokol",
        "coords": [
            10992.1,
            230221.0
        ],
        "region": "EU",
        "companies": []
    },
    "gambaru": {
        "name": "Gambaru",
        "coords": [
            10216.6,
            230522.0
        ],
        "region": "EU",
        "companies": []
    },
    "garabogaz": {
        "name": "Garabogaz",
        "coords": [
            171006.0,
            11182.4
        ],
        "region": "EU",
        "companies": []
    },
    "garyan": {
        "name": "Garyan",
        "coords": [
            6635.18,
            104884.0
        ],
        "region": "EU",
        "companies": []
    },
    "geneina": {
        "name": "El Geneina",
        "coords": [
            67593.1,
            219762.0
        ],
        "region": "EU",
        "companies": []
    },
    "gorgan": {
        "name": "Gorgan",
        "coords": [
            191546.8,
            30292.8
        ],
        "region": "EU",
        "companies": []
    },
    "goyang": {
        "name": "고양",
        "coords": [
            352977.0,
            -247030.0
        ],
        "region": "EU",
        "companies": []
    },
    "guzar": {
        "name": "G'uzor",
        "coords": [
            230130.0,
            -9555.58
        ],
        "region": "EU",
        "companies": []
    },
    "gyzylgaya": {
        "name": "Gyzylgaya",
        "coords": [
            186396.0,
            8852.86
        ],
        "region": "EU",
        "companies": []
    },
    "hairatan": {
        "name": "Hairatan",
        "coords": [
            240484.0,
            -5723.45
        ],
        "region": "EU",
        "companies": []
    },
    "haiya": {
        "name": "Haiya",
        "coords": [
            147309.0,
            171712.0
        ],
        "region": "EU",
        "companies": []
    },
    "halaib": {
        "name": "Halaib",
        "coords": [
            142103.5,
            147045.5
        ],
        "region": "EU",
        "companies": []
    },
    "hashtpar": {
        "name": "Hashtpar",
        "coords": [
            166161.4,
            37340.69
        ],
        "region": "EU",
        "companies": []
    },
    "herat": {
        "name": "Herat",
        "coords": [
            230968.0,
            21861.7
        ],
        "region": "EU",
        "companies": []
    },
    "humeyra": {
        "name": "Humeyra",
        "coords": [
            14731.8,
            141611.0
        ],
        "region": "EU",
        "companies": []
    },
    "hurghada": {
        "name": "Hurghada",
        "coords": [
            117309.3,
            122156.3
        ],
        "region": "EU",
        "companies": []
    },
    "incheon": {
        "name": "인천",
        "coords": [
            353940.0,
            -245499.0
        ],
        "region": "EU",
        "companies": []
    },
    "islamabad": {
        "name": "Islamabad",
        "coords": [
            271716.6,
            -9842.945
        ],
        "region": "EU",
        "companies": []
    },
    "jigarband": {
        "name": "Jigarband",
        "coords": [
            207534.0,
            -7158.0
        ],
        "region": "EU",
        "companies": []
    },
    "kaechon": {
        "name": "개천",
        "coords": [
            340690.0,
            -243683.0
        ],
        "region": "EU",
        "companies": []
    },
    "kaesong": {
        "name": "개성",
        "coords": [
            350848.0,
            -246238.0
        ],
        "region": "EU",
        "companies": []
    },
    "kandahar": {
        "name": "Kandahar",
        "coords": [
            254908.0,
            23379.4
        ],
        "region": "EU",
        "companies": []
    },
    "karakul": {
        "name": "Қарокӯл",
        "coords": [
            253093.0,
            -34041.0
        ],
        "region": "EU",
        "companies": []
    },
    "kassala": {
        "name": "Kassala",
        "coords": [
            152834.0,
            189905.0
        ],
        "region": "EU",
        "companies": []
    },
    "kgjalalbd": {
        "name": "Жалалабат",
        "coords": [
            243214.0,
            -39637.0
        ],
        "region": "EU",
        "companies": []
    },
    "kgmanas": {
        "name": "Манас",
        "coords": [
            238140.0,
            -51688.7
        ],
        "region": "EU",
        "companies": []
    },
    "kgosh": {
        "name": "Ош",
        "coords": [
            244126.0,
            -37650.4
        ],
        "region": "EU",
        "companies": []
    },
    "kogon": {
        "name": "Kogon",
        "coords": [
            221471.0,
            -8519.93
        ],
        "region": "EU",
        "companies": []
    },
    "komsomolabad": {
        "name": "Комсомолобод",
        "coords": [
            242387.0,
            -22163.7
        ],
        "region": "EU",
        "companies": []
    },
    "koneurgenc": {
        "name": "Köneürgenç",
        "coords": [
            192250.0,
            -7675.14
        ],
        "region": "EU",
        "companies": []
    },
    "korday": {
        "name": "Қордай",
        "coords": [
            239291.0,
            -53482.9
        ],
        "region": "EU",
        "companies": []
    },
    "koson": {
        "name": "Koson",
        "coords": [
            224263.0,
            -8931.69
        ],
        "region": "EU",
        "companies": []
    },
    "kosti": {
        "name": "Kosti",
        "coords": [
            133515.0,
            210944.0
        ],
        "region": "EU",
        "companies": []
    },
    "kousseri": {
        "name": "Kousseri",
        "coords": [
            15870.5,
            232127.0
        ],
        "region": "EU",
        "companies": []
    },
    "koytendag": {
        "name": "Köýtendag",
        "coords": [
            233215.0,
            -3934.92
        ],
        "region": "EU",
        "companies": []
    },
    "kuchlak": {
        "name": "Kuchlak",
        "coords": [
            264581.0,
            25309.9
        ],
        "region": "EU",
        "companies": []
    },
    "marsa": {
        "name": "Marsa Alam",
        "coords": [
            126825.8,
            133088.7
        ],
        "region": "EU",
        "companies": []
    },
    "marytm": {
        "name": "Mary",
        "coords": [
            217498.0,
            7762.95
        ],
        "region": "EU",
        "companies": []
    },
    "massaguet": {
        "name": "Massaguet",
        "coords": [
            21019.9,
            227190.0
        ],
        "region": "EU",
        "companies": []
    },
    "massakory": {
        "name": "Massakory",
        "coords": [
            22076.8,
            221462.0
        ],
        "region": "EU",
        "companies": []
    },
    "medinah": {
        "name": "Medina",
        "coords": [
            153635.0,
            129098.0
        ],
        "region": "EU",
        "companies": []
    },
    "meymaneh": {
        "name": "Meymaneh",
        "coords": [
            235075.0,
            7018.21
        ],
        "region": "EU",
        "companies": []
    },
    "mohamqol": {
        "name": "Muhammad Qol",
        "coords": [
            147911.0,
            156616.0
        ],
        "region": "EU",
        "companies": []
    },
    "murghab": {
        "name": "Мурғоб",
        "coords": [
            257792.0,
            -31818.9
        ],
        "region": "EU",
        "companies": []
    },
    "murree": {
        "name": "Murree",
        "coords": [
            273012.3,
            -13275.93
        ],
        "region": "EU",
        "companies": []
    },
    "musbagh": {
        "name": "Muslim Bagh",
        "coords": [
            268317.0,
            18898.2
        ],
        "region": "EU",
        "companies": []
    },
    "muwaileh": {
        "name": "Al Muwaileh",
        "coords": [
            123074.0,
            118888.0
        ],
        "region": "EU",
        "companies": []
    },
    "nahud": {
        "name": "En Nahud",
        "coords": [
            106557.0,
            218449.0
        ],
        "region": "EU",
        "companies": []
    },
    "nampo": {
        "name": "남포",
        "coords": [
            345835.0,
            -240230.0
        ],
        "region": "EU",
        "companies": []
    },
    "nanga": {
        "name": "Nanga Parbat Base Camp",
        "coords": [
            272643.3,
            -17664.69
        ],
        "region": "EU",
        "companies": []
    },
    "ndjamena": {
        "name": "N'Djamena",
        "coords": [
            16930.4,
            230822.0
        ],
        "region": "EU",
        "companies": []
    },
    "ngoura": {
        "name": "Ngoura",
        "coords": [
            27054.7,
            224813.0
        ],
        "region": "EU",
        "companies": []
    },
    "olot": {
        "name": "Olot",
        "coords": [
            218745.0,
            -7017.96
        ],
        "region": "EU",
        "companies": []
    },
    "oumhadjer": {
        "name": "Oum Hadjer",
        "coords": [
            48705.9,
            221926.0
        ],
        "region": "EU",
        "companies": []
    },
    "paju": {
        "name": "파주",
        "coords": [
            352028.0,
            -246963.0
        ],
        "region": "EU",
        "companies": []
    },
    "portsudan": {
        "name": "Port Sudan",
        "coords": [
            149809.0,
            162137.0
        ],
        "region": "EU",
        "companies": []
    },
    "punel": {
        "name": "Punel",
        "coords": [
            167976.8,
            38541.19
        ],
        "region": "EU",
        "companies": []
    },
    "pyongyang": {
        "name": "평양",
        "coords": [
            344424.0,
            -243510.0
        ],
        "region": "EU",
        "companies": []
    },
    "qadarif": {
        "name": "Al Qadarif",
        "coords": [
            149006.0,
            200542.0
        ],
        "region": "EU",
        "companies": []
    },
    "qalenaslam": {
        "name": "Qal'en ye Mirza Aslam",
        "coords": [
            234037.0,
            25574.6
        ],
        "region": "EU",
        "companies": []
    },
    "qarshi": {
        "name": "Qarshi",
        "coords": [
            227780.0,
            -9188.7
        ],
        "region": "EU",
        "companies": []
    },
    "qaryat": {
        "name": "Qaryat",
        "coords": [
            9134.25,
            116034.0
        ],
        "region": "EU",
        "companies": []
    },
    "qorakol": {
        "name": "Qorako'l",
        "coords": [
            218723.0,
            -7776.93
        ],
        "region": "EU",
        "companies": []
    },
    "quetta": {
        "name": "Quetta",
        "coords": [
            265911.0,
            26418.6
        ],
        "region": "EU",
        "companies": []
    },
    "rabak": {
        "name": "Rabak",
        "coords": [
            133877.0,
            210586.0
        ],
        "region": "EU",
        "companies": []
    },
    "rasht": {
        "name": "Rasht",
        "coords": [
            171486.8,
            38430.41
        ],
        "region": "EU",
        "companies": []
    },
    "rawalpindi": {
        "name": "Rawalpindi",
        "coords": [
            274928.0,
            -9189.668
        ],
        "region": "EU",
        "companies": []
    },
    "rushon": {
        "name": "Рӯшон",
        "coords": [
            250399.0,
            -22221.0
        ],
        "region": "EU",
        "companies": []
    },
    "ruwaba": {
        "name": "Umm Ruwaba",
        "coords": [
            124070.0,
            214763.0
        ],
        "region": "EU",
        "companies": []
    },
    "sabha": {
        "name": "Sabha",
        "coords": [
            12619.6,
            135879.0
        ],
        "region": "EU",
        "companies": []
    },
    "safaga": {
        "name": "Safaga",
        "coords": [
            118961.9,
            125070.6
        ],
        "region": "EU",
        "companies": []
    },
    "saghirdasht": {
        "name": "Сағирдашт",
        "coords": [
            245524.0,
            -23133.2
        ],
        "region": "EU",
        "companies": []
    },
    "salyan": {
        "name": "Salyan",
        "coords": [
            162422.7,
            28642.28
        ],
        "region": "EU",
        "companies": []
    },
    "sari": {
        "name": "Sari",
        "coords": [
            187100.5,
            34315.65
        ],
        "region": "EU",
        "companies": []
    },
    "sarytash": {
        "name": "Сарыташ",
        "coords": [
            248967.0,
            -35481.4
        ],
        "region": "EU",
        "companies": []
    },
    "sennar": {
        "name": "Sennar",
        "coords": [
            138436.0,
            206822.0
        ],
        "region": "EU",
        "companies": []
    },
    "seoul": {
        "name": "서울",
        "coords": [
            353856.0,
            -249173.0
        ],
        "region": "EU",
        "companies": []
    },
    "serdartm": {
        "name": "Serdar",
        "coords": [
            192486.0,
            15518.8
        ],
        "region": "EU",
        "companies": []
    },
    "serhetabat": {
        "name": "Serhetabat",
        "coords": [
            228227.0,
            17010.9
        ],
        "region": "EU",
        "companies": []
    },
    "shalaten": {
        "name": "Shalaten",
        "coords": [
            134050.2,
            143825.8
        ],
        "region": "EU",
        "companies": []
    },
    "sharlavuk": {
        "name": "Sharlavuk",
        "coords": [
            191196.0,
            22676.1
        ],
        "region": "EU",
        "companies": []
    },
    "sherabad": {
        "name": "Sherobod",
        "coords": [
            236523.0,
            -7652.79
        ],
        "region": "EU",
        "companies": []
    },
    "sinkat": {
        "name": "Sinkat",
        "coords": [
            149136.0,
            167676.0
        ],
        "region": "EU",
        "companies": []
    },
    "sinuiju": {
        "name": "신의주",
        "coords": [
            338946.0,
            -237533.0
        ],
        "region": "EU",
        "companies": []
    },
    "songkhla": {
        "name": "Songkhla",
        "coords": [
            507648.0,
            -56160.0
        ],
        "region": "EU",
        "companies": []
    },
    "ssheikh": {
        "name": "Sharm El-Sheikh",
        "coords": [
            112672.0,
            115392.0
        ],
        "region": "EU",
        "companies": []
    },
    "stcath": {
        "name": "St. Catherine",
        "coords": [
            109747.0,
            110872.0
        ],
        "region": "EU",
        "companies": []
    },
    "suakin": {
        "name": "Suakin",
        "coords": [
            151714.0,
            165104.0
        ],
        "region": "EU",
        "companies": []
    },
    "suusamyr": {
        "name": "Суусамыр",
        "coords": [
            238739.0,
            -43650.3
        ],
        "region": "EU",
        "companies": []
    },
    "tehran": {
        "name": "Tehran",
        "coords": [
            182502.3,
            43419.62
        ],
        "region": "EU",
        "companies": []
    },
    "tejen": {
        "name": "Tejen",
        "coords": [
            213936.0,
            12279.3
        ],
        "region": "EU",
        "companies": []
    },
    "tendali": {
        "name": "Tendali",
        "coords": [
            128425.0,
            213037.0
        ],
        "region": "EU",
        "companies": []
    },
    "termez": {
        "name": "Termiz",
        "coords": [
            239069.0,
            -6910.43
        ],
        "region": "EU",
        "companies": []
    },
    "tojikobod": {
        "name": "Тоҷикобод",
        "coords": [
            243820.0,
            -25586.5
        ],
        "region": "EU",
        "companies": []
    },
    "tripoli": {
        "name": "Tripoli",
        "coords": [
            7031.74,
            101451.0
        ],
        "region": "EU",
        "companies": []
    },
    "turkmenabat": {
        "name": "Türkmenabat",
        "coords": [
            219245.0,
            -3547.8
        ],
        "region": "EU",
        "companies": []
    },
    "turkmenbashi": {
        "name": "Türkmenbaşy",
        "coords": [
            176385.0,
            17396.0
        ],
        "region": "EU",
        "companies": []
    },
    "ulugqat": {
        "name": "乌鲁克恰提乡",
        "coords": [
            252511.0,
            -40317.8
        ],
        "region": "EU",
        "companies": []
    },
    "wadibanda": {
        "name": "Wadi Banda",
        "coords": [
            101782.0,
            217432.0
        ],
        "region": "EU",
        "companies": []
    },
    "wadimadani": {
        "name": "Wadi Madani",
        "coords": [
            136948.0,
            201543.0
        ],
        "region": "EU",
        "companies": []
    },
    "wuqia": {
        "name": "乌恰镇",
        "coords": [
            255115.0,
            -42019.0
        ],
        "region": "EU",
        "companies": []
    },
    "xiuyanzhen": {
        "name": "岫岩镇",
        "coords": [
            335669.0,
            -232344.0
        ],
        "region": "EU",
        "companies": []
    },
    "yanbu": {
        "name": "Yanbu",
        "coords": [
            146416.0,
            135205.0
        ],
        "region": "EU",
        "companies": []
    },
    "yerbent": {
        "name": "Yerbent",
        "coords": [
            200277.0,
            7918.55
        ],
        "region": "EU",
        "companies": []
    },
    "zhob": {
        "name": "Zhob",
        "coords": [
            269753.0,
            11893.6
        ],
        "region": "EU",
        "companies": []
    },
    "zouar": {
        "name": "Zouar",
        "coords": [
            22514.6,
            167265.0
        ],
        "region": "EU",
        "companies": []
    },
    "alyabvck": {
        "name": "Алябьевский",
        "coords": [
            138858.6,
            -100993.2
        ],
        "region": "EU",
        "companies": []
    },
    "cerov": {
        "name": "Серов",
        "coords": [
            139469.4,
            -91600.13
        ],
        "region": "EU",
        "companies": []
    },
    "ceveroural": {
        "name": "Североуральск",
        "coords": [
            135116.0,
            -93394.48
        ],
        "region": "EU",
        "companies": []
    },
    "cocva": {
        "name": "Сосьва",
        "coords": [
            142978.3,
            -91991.03
        ],
        "region": "EU",
        "companies": []
    },
    "covetcky": {
        "name": "Советский",
        "coords": [
            142555.8,
            -104581.4
        ],
        "region": "EU",
        "companies": []
    },
    "cupra": {
        "name": "Супра",
        "coords": [
            145923.3,
            -102678.5
        ],
        "region": "EU",
        "companies": []
    },
    "dacny": {
        "name": "Дачный",
        "coords": [
            140691.3,
            -86415.93
        ],
        "region": "EU",
        "companies": []
    },
    "gornoural": {
        "name": "Горноуральский",
        "coords": [
            140706.2,
            -83327.9
        ],
        "region": "EU",
        "companies": []
    },
    "ivdel": {
        "name": "Ивдель",
        "coords": [
            134957.2,
            -96035.98
        ],
        "region": "EU",
        "companies": []
    },
    "karpinck": {
        "name": "Карпинск",
        "coords": [
            135385.6,
            -91953.53
        ],
        "region": "EU",
        "companies": []
    },
    "kosaj": {
        "name": "Кошай",
        "coords": [
            143194.9,
            -91184.8
        ],
        "region": "EU",
        "companies": []
    },
    "kracnogl": {
        "name": "Красноглинный",
        "coords": [
            140882.0,
            -92099.52
        ],
        "region": "EU",
        "companies": []
    },
    "kracnoturin": {
        "name": "Краснотурьинск",
        "coords": [
            137199.1,
            -93051.81
        ],
        "region": "EU",
        "companies": []
    },
    "kushva": {
        "name": "Кушва",
        "coords": [
            139456.9,
            -85248.31
        ],
        "region": "EU",
        "companies": []
    },
    "malayalya": {
        "name": "Малая Лая",
        "coords": [
            140516.0,
            -84538.63
        ],
        "region": "EU",
        "companies": []
    },
    "moctovaya": {
        "name": "Мостовая",
        "coords": [
            139474.1,
            -86903.39
        ],
        "region": "EU",
        "companies": []
    },
    "niznsalda": {
        "name": "Нижняя Салда",
        "coords": [
            144737.2,
            -84843.43
        ],
        "region": "EU",
        "companies": []
    },
    "nizntura": {
        "name": "Нижняя Тура",
        "coords": [
            139642.0,
            -87272.38
        ],
        "region": "EU",
        "companies": []
    },
    "niznytagil": {
        "name": "Нижний Тагил",
        "coords": [
            142504.8,
            -82070.38
        ],
        "region": "EU",
        "companies": []
    },
    "nlyalya": {
        "name": "Новая Ляля",
        "coords": [
            140806.4,
            -89656.88
        ],
        "region": "EU",
        "companies": []
    },
    "ouc": {
        "name": "Оус",
        "coords": [
            137172.7,
            -97253.59
        ],
        "region": "EU",
        "companies": []
    },
    "pelym": {
        "name": "Пелым",
        "coords": [
            138137.2,
            -98371.84
        ],
        "region": "EU",
        "companies": []
    },
    "pionercky": {
        "name": "Пионерский",
        "coords": [
            139685.8,
            -100980.5
        ],
        "region": "EU",
        "companies": []
    },
    "platinasv": {
        "name": "Платина",
        "coords": [
            140533.7,
            -88246.68
        ],
        "region": "EU",
        "companies": []
    },
    "privokzalny": {
        "name": "Привокзальный",
        "coords": [
            141316.5,
            -89019.5
        ],
        "region": "EU",
        "companies": []
    },
    "rudnichny": {
        "name": "Рудничный",
        "coords": [
            137419.3,
            -92099.84
        ],
        "region": "EU",
        "companies": []
    },
    "taezny": {
        "name": "Таежный",
        "coords": [
            139745.5,
            -100218.2
        ],
        "region": "EU",
        "companies": []
    },
    "teterevo": {
        "name": "Тетерево",
        "coords": [
            145830.4,
            -100876.6
        ],
        "region": "EU",
        "companies": []
    },
    "tretycever": {
        "name": "3-й Северный",
        "coords": [
            134399.1,
            -94212.06
        ],
        "region": "EU",
        "companies": []
    },
    "uray": {
        "name": "Урай",
        "coords": [
            147638.4,
            -99265.25
        ],
        "region": "EU",
        "companies": []
    },
    "vcevolodo": {
        "name": "Всеволодо-Благодатское",
        "coords": [
            133951.7,
            -95113.63
        ],
        "region": "EU",
        "companies": []
    },
    "verhoture": {
        "name": "Верхотурье",
        "coords": [
            141852.7,
            -89347.33
        ],
        "region": "EU",
        "companies": []
    },
    "verksalda": {
        "name": "Верхняя Салда",
        "coords": [
            144032.2,
            -84286.37
        ],
        "region": "EU",
        "companies": []
    },
    "verktura": {
        "name": "Верхняя Тура",
        "coords": [
            139388.3,
            -86224.23
        ],
        "region": "EU",
        "companies": []
    },
    "vorontsov": {
        "name": "Воронцовка",
        "coords": [
            136867.1,
            -91153.78
        ],
        "region": "EU",
        "companies": []
    },
    "yevctyun": {
        "name": "Евстюниха",
        "coords": [
            140355.3,
            -82615.53
        ],
        "region": "EU",
        "companies": []
    },
    "yugorck": {
        "name": "Югорск",
        "coords": [
            140923.9,
            -102441.0
        ],
        "region": "EU",
        "companies": []
    },
    "komso": {
        "name": "Комсомольск-на-Амуре",
        "coords": [
            276723.2,
            -285959.1
        ],
        "region": "EU",
        "companies": []
    },
    "selikhino": {
        "name": "Селихино",
        "coords": [
            279078.0,
            -288263.4
        ],
        "region": "EU",
        "companies": []
    },
    "achikulak": {
        "name": "Ачикулак",
        "coords": [
            134759.6,
            10356.82
        ],
        "region": "EU",
        "companies": []
    },
    "achtubinsk": {
        "name": "Ахтубинск",
        "coords": [
            133163.2,
            -10214.14
        ],
        "region": "EU",
        "companies": []
    },
    "akkystau": {
        "name": "Аккыстау",
        "coords": [
            150438.2,
            -12712.05
        ],
        "region": "EU",
        "companies": []
    },
    "artezian": {
        "name": "Артезиан",
        "coords": [
            139247.6,
            5720.188
        ],
        "region": "EU",
        "companies": []
    },
    "astrachan": {
        "name": "Астрахань",
        "coords": [
            140727.9,
            -3928.035
        ],
        "region": "EU",
        "companies": []
    },
    "babayurt": {
        "name": "Бабаюрт",
        "coords": [
            145378.2,
            12931.13
        ],
        "region": "EU",
        "companies": []
    },
    "baksan": {
        "name": "Баксан",
        "coords": [
            131935.1,
            17103.25
        ],
        "region": "EU",
        "companies": []
    },
    "beslan": {
        "name": "Беслан",
        "coords": [
            136335.0,
            17901.61
        ],
        "region": "EU",
        "companies": []
    },
    "budennovsk": {
        "name": "Будённовск",
        "coords": [
            132692.4,
            9283.316
        ],
        "region": "EU",
        "companies": []
    },
    "chervlennaya": {
        "name": "Червленная",
        "coords": [
            142215.6,
            13454.23
        ],
        "region": "EU",
        "companies": []
    },
    "derbentus": {
        "name": "Дербент",
        "coords": [
            154618.2,
            17839.03
        ],
        "region": "EU",
        "companies": []
    },
    "grozniy": {
        "name": "Грозный",
        "coords": [
            141174.5,
            15578.23
        ],
        "region": "EU",
        "companies": []
    },
    "harabali": {
        "name": "Харабали",
        "coords": [
            136190.5,
            -8263.641
        ],
        "region": "EU",
        "companies": []
    },
    "hasavjurt": {
        "name": "Хасавюрт",
        "coords": [
            145090.8,
            15401.91
        ],
        "region": "EU",
        "companies": []
    },
    "hosheutovo": {
        "name": "Хошеутово",
        "coords": [
            139166.5,
            -6633.34
        ],
        "region": "EU",
        "companies": []
    },
    "ganyushkino": {
        "name": "Ганюшкин",
        "coords": [
            147705.0,
            -8359.859
        ],
        "region": "EU",
        "companies": []
    },
    "isberbasch": {
        "name": "Избербаш",
        "coords": [
            153511.2,
            16635.89
        ],
        "region": "EU",
        "companies": []
    },
    "kaspijsk": {
        "name": "Каспийск",
        "coords": [
            151484.9,
            15231.43
        ],
        "region": "EU",
        "companies": []
    },
    "kisljar": {
        "name": "Кизляр",
        "coords": [
            143273.2,
            10918.15
        ],
        "region": "EU",
        "companies": []
    },
    "kochubey": {
        "name": "Кочубей",
        "coords": [
            140904.9,
            9113.016
        ],
        "region": "EU",
        "companies": []
    },
    "komsomolskiy": {
        "name": "Комсомольский",
        "coords": [
            136270.2,
            3562.879
        ],
        "region": "EU",
        "companies": []
    },
    "kotyaevka": {
        "name": "Котяевка",
        "coords": [
            143721.5,
            -5320.992
        ],
        "region": "EU",
        "companies": []
    },
    "krasnyiyar": {
        "name": "Красный Яр",
        "coords": [
            141566.4,
            -5196.574
        ],
        "region": "EU",
        "companies": []
    },
    "kurskaya": {
        "name": "Курская",
        "coords": [
            135765.9,
            13291.52
        ],
        "region": "EU",
        "companies": []
    },
    "kyslovodsk": {
        "name": "Кисловодск",
        "coords": [
            130250.1,
            17101.89
        ],
        "region": "EU",
        "companies": []
    },
    "lagan": {
        "name": "Лагань",
        "coords": [
            140084.2,
            2373.566
        ],
        "region": "EU",
        "companies": []
    },
    "lenino": {
        "name": "Ленино",
        "coords": [
            136605.5,
            -5782.777
        ],
        "region": "EU",
        "companies": []
    },
    "magas": {
        "name": "Магас",
        "coords": [
            139204.3,
            18246.11
        ],
        "region": "EU",
        "companies": []
    },
    "mahachkala": {
        "name": "Махачкала",
        "coords": [
            150222.9,
            14984.72
        ],
        "region": "EU",
        "companies": []
    },
    "mozdok": {
        "name": "Моздок",
        "coords": [
            137748.9,
            14120.87
        ],
        "region": "EU",
        "companies": []
    },
    "nalchik": {
        "name": "Нальчик",
        "coords": [
            132483.6,
            18065.41
        ],
        "region": "EU",
        "companies": []
    },
    "neftekumsk": {
        "name": "Нефтекумск",
        "coords": [
            134807.4,
            8653.039
        ],
        "region": "EU",
        "companies": []
    },
    "prohladnyi": {
        "name": "Прохладный",
        "coords": [
            133884.1,
            15362.22
        ],
        "region": "EU",
        "companies": []
    },
    "pyatigorsk": {
        "name": "Пятигорск",
        "coords": [
            129809.9,
            16173.83
        ],
        "region": "EU",
        "companies": []
    },
    "suhokumsk": {
        "name": "Южно-Сухокумск",
        "coords": [
            137425.1,
            9018.516
        ],
        "region": "EU",
        "companies": []
    },
    "svetlograd": {
        "name": "Светлоград",
        "coords": [
            132703.5,
            6252.75
        ],
        "region": "EU",
        "companies": []
    },
    "tmekteb": {
        "name": "Терекли-Мектеб",
        "coords": [
            139256.9,
            10986.24
        ],
        "region": "EU",
        "companies": []
    },
    "tukuymekteb": {
        "name": "Тукуй-Мектеб",
        "coords": [
            136925.2,
            10720.23
        ],
        "region": "EU",
        "companies": []
    },
    "vladikavkaz": {
        "name": "Владикавказ",
        "coords": [
            137140.5,
            19331.27
        ],
        "region": "EU",
        "companies": []
    },
    "xacmaz": {
        "name": "Xaçmaz",
        "coords": [
            157240.9,
            18887.04
        ],
        "region": "EU",
        "companies": []
    },
    "zaganaman": {
        "name": "Цаган Аман",
        "coords": [
            132137.2,
            -7422.48
        ],
        "region": "EU",
        "companies": []
    },
    "zelenokumsk": {
        "name": "Зеленокумск",
        "coords": [
            132952.7,
            12711.14
        ],
        "region": "EU",
        "companies": []
    },
    "zubovka": {
        "name": "Зубовка",
        "coords": [
            126162.4,
            -7692.734
        ],
        "region": "EU",
        "companies": []
    },
    "bekasi": {
        "name": "Bekasi",
        "coords": [
            635990.1,
            -68515.49
        ],
        "region": "EU",
        "companies": []
    },
    "bogor": {
        "name": "Bogor",
        "coords": [
            639141.9,
            -64426.58
        ],
        "region": "EU",
        "companies": []
    },
    "cilegon": {
        "name": "Cilegon",
        "coords": [
            631357.3,
            -58920.03
        ],
        "region": "EU",
        "companies": []
    },
    "depok": {
        "name": "Depok",
        "coords": [
            638134.5,
            -65534.2
        ],
        "region": "EU",
        "companies": []
    },
    "jakarta": {
        "name": "Jakarta",
        "coords": [
            635294.6,
            -66100.04
        ],
        "region": "EU",
        "companies": []
    },
    "merak": {
        "name": "Merak",
        "coords": [
            630153.9,
            -60392.44
        ],
        "region": "EU",
        "companies": []
    },
    "serpong": {
        "name": "Ciputat",
        "coords": [
            637152.4,
            -64629.94
        ],
        "region": "EU",
        "companies": []
    },
    "tangerang": {
        "name": "Tangerang",
        "coords": [
            635075.6,
            -63838.31
        ],
        "region": "EU",
        "companies": []
    },
    "apex": {
        "name": "Apex",
        "coords": [
            -157954.0,
            -183007.9
        ],
        "region": "EU",
        "companies": []
    },
    "brae": {
        "name": "Brae",
        "coords": [
            -30136.8,
            -77157.3
        ],
        "region": "EU",
        "companies": []
    },
    "frodsba": {
        "name": "Froðba",
        "coords": [
            -50025.15,
            -74024.72
        ],
        "region": "EU",
        "companies": []
    },
    "gloup": {
        "name": "Gloup",
        "coords": [
            -28456.94,
            -79166.83
        ],
        "region": "EU",
        "companies": []
    },
    "grutness": {
        "name": "Grutness",
        "coords": [
            -30594.54,
            -74078.02
        ],
        "region": "EU",
        "companies": []
    },
    "gutcher": {
        "name": "Gutcher",
        "coords": [
            -28301.31,
            -78776.45
        ],
        "region": "EU",
        "companies": []
    },
    "husavik": {
        "name": "Húsavík",
        "coords": [
            -50301.42,
            -77400.74
        ],
        "region": "EU",
        "companies": []
    },
    "hvalba": {
        "name": "Hvalba",
        "coords": [
            -51358.65,
            -74536.58
        ],
        "region": "EU",
        "companies": []
    },
    "iqaluit": {
        "name": "Iqaluit",
        "coords": [
            -158031.1,
            -183283.1
        ],
        "region": "EU",
        "companies": []
    },
    "itorqomt": {
        "name": "Ittoqqortoormiit",
        "coords": [
            -56779.94,
            -132616.1
        ],
        "region": "EU",
        "companies": []
    },
    "kulusuk": {
        "name": "Kulusuk",
        "coords": [
            -98579.69,
            -128887.4
        ],
        "region": "EU",
        "companies": []
    },
    "kuummiit": {
        "name": "Kuummiit",
        "coords": [
            -97560.98,
            -130557.9
        ],
        "region": "EU",
        "companies": []
    },
    "lopra": {
        "name": "Lopra",
        "coords": [
            -50005.41,
            -73123.83
        ],
        "region": "EU",
        "companies": []
    },
    "mid": {
        "name": "Mid Yell",
        "coords": [
            -28979.2,
            -78551.72
        ],
        "region": "EU",
        "companies": []
    },
    "nanortalik": {
        "name": "Nanortalik",
        "coords": [
            -138771.5,
            -119644.9
        ],
        "region": "EU",
        "companies": []
    },
    "porkeri": {
        "name": "Porkeri",
        "coords": [
            -50233.16,
            -73678.75
        ],
        "region": "EU",
        "companies": []
    },
    "sandness": {
        "name": "Sandness",
        "coords": [
            -31367.48,
            -76735.47
        ],
        "region": "EU",
        "companies": []
    },
    "sandvik": {
        "name": "Sandvík",
        "coords": [
            -51513.36,
            -74831.03
        ],
        "region": "EU",
        "companies": []
    },
    "skopun": {
        "name": "Skopun",
        "coords": [
            -50842.39,
            -77919.39
        ],
        "region": "EU",
        "companies": []
    },
    "sumba": {
        "name": "Sumba",
        "coords": [
            -49945.78,
            -72735.58
        ],
        "region": "EU",
        "companies": []
    },
    "tasiilaq": {
        "name": "Tasiilaq",
        "coords": [
            -99809.9,
            -129688.4
        ],
        "region": "EU",
        "companies": []
    },
    "tasiusaq": {
        "name": "Tasiusaq",
        "coords": [
            -136746.4,
            -119556.0
        ],
        "region": "EU",
        "companies": []
    },
    "toft": {
        "name": "Toft",
        "coords": [
            -29770.07,
            -77601.41
        ],
        "region": "EU",
        "companies": []
    },
    "trongisva": {
        "name": "Trongisvágur",
        "coords": [
            -50607.59,
            -74109.84
        ],
        "region": "EU",
        "companies": []
    },
    "ulsta": {
        "name": "Ulsta",
        "coords": [
            -29320.07,
            -77726.69
        ],
        "region": "EU",
        "companies": []
    },
    "vagur": {
        "name": "Vágur",
        "coords": [
            -50285.31,
            -73262.34
        ],
        "region": "EU",
        "companies": []
    },
    "ajanm": {
        "name": "Puppebu",
        "coords": [
            -29742.95,
            -125097.9
        ],
        "region": "EU",
        "companies": []
    },
    "bjornoya": {
        "name": "bjornoya",
        "coords": [
            22664.41,
            -137575.1
        ],
        "region": "EU",
        "companies": []
    },
    "sj": {
        "name": "Ny-Ålesund",
        "coords": [
            12489.13,
            -166475.6
        ],
        "region": "EU",
        "companies": []
    },
    "aj": {
        "name": "al_bajda",
        "coords": [
            50002.23,
            101363.0
        ],
        "region": "EU",
        "companies": []
    },
    "ajdabiya": {
        "name": "ajdabiya",
        "coords": [
            44010.16,
            112893.5
        ],
        "region": "EU",
        "companies": []
    },
    "alexandria": {
        "name": "alexandria",
        "coords": [
            89421.84,
            100451.2
        ],
        "region": "EU",
        "companies": []
    },
    "as": {
        "name": "as_sallum",
        "coords": [
            72358.02,
            105524.1
        ],
        "region": "EU",
        "companies": []
    },
    "bengazi": {
        "name": "bengazi",
        "coords": [
            42442.27,
            105100.4
        ],
        "region": "EU",
        "companies": []
    },
    "matruh": {
        "name": "matruh",
        "coords": [
            79165.84,
            105630.9
        ],
        "region": "EU",
        "companies": []
    },
    "misrata": {
        "name": "misrata",
        "coords": [
            16198.79,
            104963.4
        ],
        "region": "EU",
        "companies": []
    },
    "syrta": {
        "name": "syrta",
        "coords": [
            23208.94,
            111002.7
        ],
        "region": "EU",
        "companies": []
    },
    "tobruk": {
        "name": "tobruk",
        "coords": [
            60897.84,
            103445.7
        ],
        "region": "EU",
        "companies": []
    },
    "cala": {
        "name": "Cala en Bosc",
        "coords": [
            -31822.98,
            57702.31
        ],
        "region": "EU",
        "companies": []
    },
    "capdepera": {
        "name": "Capdepera",
        "coords": [
            -34362.89,
            58619.27
        ],
        "region": "EU",
        "companies": []
    },
    "ceuta": {
        "name": "Ceuta",
        "coords": [
            -78468.68,
            72909.74
        ],
        "region": "EU",
        "companies": []
    },
    "ibiza": {
        "name": "Eivissa",
        "coords": [
            -43658.84,
            61456.93
        ],
        "region": "EU",
        "companies": []
    },
    "mahon": {
        "name": "Maó",
        "coords": [
            -30134.22,
            58104.07
        ],
        "region": "EU",
        "companies": []
    },
    "melilla": {
        "name": "Melila",
        "coords": [
            -68710.47,
            78293.62
        ],
        "region": "EU",
        "companies": []
    },
    "menorca": {
        "name": "Ciutadella de Menorca",
        "coords": [
            -32384.86,
            57535.07
        ],
        "region": "EU",
        "companies": []
    },
    "palma": {
        "name": "Palma",
        "coords": [
            -37875.28,
            58873.59
        ],
        "region": "EU",
        "companies": []
    },
    "pollenca": {
        "name": "Pollença",
        "coords": [
            -37107.28,
            58204.95
        ],
        "region": "EU",
        "companies": []
    },
    "santa": {
        "name": "Santa Marina",
        "coords": [
            -30610.58,
            57179.7
        ],
        "region": "EU",
        "companies": []
    },
    "santanyi": {
        "name": "Santanyi",
        "coords": [
            -36022.73,
            60711.39
        ],
        "region": "EU",
        "companies": []
    }
}


def get_city_coords(city_id):
    cid = city_id.replace("city.", "")
    return CITY_DATA.get(cid, {}).get("coords", (0, 0))

def get_city_companies(city_id):
    cid = city_id.replace("city.", "")
    # Se a cidade existe no banco, retorna as empresas dela. Caso contrário, retorna um padrão.
    return CITY_DATA.get(cid, {}).get("companies", ["eurogoodies", "stokes", "lkwlog"])

def calculate_distance(city1_id, city2_id):
    c1 = get_city_coords(city1_id)
    c2 = get_city_coords(city2_id)
    # Distância Euclidiana baseada em coordenadas reais (escala 1:19)
    dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return int(dist / 19 / 10) # Ajuste de escala para KM

BRAZIL_CITIES_IDS = [cid for cid, data in CITY_DATA.items() if data["region"] == "BR"]
