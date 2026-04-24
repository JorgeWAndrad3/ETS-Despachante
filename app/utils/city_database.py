import math

# Banco de Dados DEFINITIVO de Cidades (EU/BR)
CITY_DATA = {
    # EUROPA
    "paris": {"name": "Paris", "coords": (0, 0), "region": "EU", "companies": ["itcc", "stokes", "lkwlog"]},
    "berlin": {"name": "Berlin", "coords": (1000, -200), "region": "EU", "companies": ["stokes", "euroacres"]},
    "london": {"name": "Londres", "coords": (-800, -500), "region": "EU", "companies": ["stokes", "trameri"]},
    "praga": {"name": "Praga", "coords": (800, 200), "region": "EU", "companies": ["itcc", "posped"]},
    "brussel": {"name": "Bruxelas", "coords": (-200, -300), "region": "EU", "companies": ["stokes", "lkwlog"]},
    "lyon": {"name": "Lyon", "coords": (-100, 500), "region": "EU", "companies": ["itcc", "boisserie"]},
    "amsterdam": {"name": "Amsterdã", "coords": (0, -400), "region": "EU", "companies": ["itcc", "lkwlog"]},
    "roma": {"name": "Roma", "coords": (500, 1200), "region": "EU", "companies": ["marmo", "fcp"]},
    "madrid": {"name": "Madrid", "coords": (-1500, 1500), "region": "EU", "companies": ["itcc", "stokes"]},
    "lisboa": {"name": "Lisboa", "coords": (-2200, 1800), "region": "EU", "companies": ["itcc", "stokes"]},
    "warszawa": {"name": "Varsóvia", "coords": (1500, -100), "region": "EU", "companies": ["posped", "lkwlog"]},
    "vienna": {"name": "Viena", "coords": (1200, 400), "region": "EU", "companies": ["itcc", "stokes"]},
    "munchen": {"name": "Munique", "coords": (800, 300), "region": "EU", "companies": ["itcc", "stokes"]},
    "hamburg": {"name": "Hamburgo", "coords": (700, -400), "region": "EU", "companies": ["lkwlog", "stokes"]},
    "frankfurt": {"name": "Frankfurt", "coords": (600, 0), "region": "EU", "companies": ["itcc", "lkwlog"]},
    "zurich": {"name": "Zurique", "coords": (300, 500), "region": "EU", "companies": ["itcc", "stokes"]},
    "geneve": {"name": "Genebra", "coords": (200, 600), "region": "EU", "companies": ["itcc", "stokes"]},
    "milano": {"name": "Milão", "coords": (400, 700), "region": "EU", "companies": ["itcc", "fcp"]},
    "venezia": {"name": "Veneza", "coords": (700, 750), "region": "EU", "companies": ["itcc", "stokes"]},
    "marseille": {"name": "Marselha", "coords": (0, 1000), "region": "EU", "companies": ["itcc", "stokes"]},
    "nice": {"name": "Nice", "coords": (200, 1050), "region": "EU", "companies": ["itcc", "stokes"]},
    "toulouse": {"name": "Toulouse", "coords": (-400, 1100), "region": "EU", "companies": ["itcc", "stokes"]},
    "bordeaux": {"name": "Bordéus", "coords": (-600, 900), "region": "EU", "companies": ["itcc", "stokes"]},
    "nantes": {"name": "Nantes", "coords": (-800, 600), "region": "EU", "companies": ["itcc", "stokes"]},
    "lille": {"name": "Lille", "coords": (-100, -100), "region": "EU", "companies": ["itcc", "stokes"]},
    "calais": {"name": "Calais", "coords": (-200, -200), "region": "EU", "companies": ["itcc", "stokes"]},
    "dover": {"name": "Dover", "coords": (-300, -300), "region": "EU", "companies": ["itcc", "stokes"]},
    "cambridge": {"name": "Cambridge", "coords": (-700, -600), "region": "EU", "companies": ["itcc", "stokes"]},
    "birmingham": {"name": "Birmingham", "coords": (-900, -700), "region": "EU", "companies": ["itcc", "stokes"]},
    "liverpool": {"name": "Liverpool", "coords": (-1000, -800), "region": "EU", "companies": ["itcc", "stokes"]},
    "manchester": {"name": "Manchester", "coords": (-950, -850), "region": "EU", "companies": ["itcc", "stokes"]},
    "glasgow": {"name": "Glasgow", "coords": (-1100, -1200), "region": "EU", "companies": ["itcc", "stokes"]},
    "edinburgh": {"name": "Edimburgo", "coords": (-1050, -1250), "region": "EU", "companies": ["itcc", "stokes"]},
    "aberdeen": {"name": "Aberdeen", "coords": (-1100, -1400), "region": "EU", "companies": ["itcc", "stokes"]},
    "bergen": {"name": "Bergen", "coords": (200, -1500), "region": "EU", "companies": ["itcc", "stokes"]},
    "stavanger": {"name": "Stavanger", "coords": (300, -1600), "region": "EU", "companies": ["itcc", "stokes"]},
    "kristiansand": {"name": "Kristiansand", "coords": (500, -1700), "region": "EU", "companies": ["itcc", "stokes"]},
    "goteborg": {"name": "Gotemburgo", "coords": (800, -1300), "region": "EU", "companies": ["itcc", "stokes"]},
    "malmo": {"name": "Malmö", "coords": (900, -1100), "region": "EU", "companies": ["itcc", "stokes"]},
    "kobenhavn": {"name": "Copenhague", "coords": (850, -1000), "region": "EU", "companies": ["itcc", "stokes"]},
    "odense": {"name": "Odense", "coords": (750, -950), "region": "EU", "companies": ["itcc", "stokes"]},
    "aalborg": {"name": "Aalborg", "coords": (800, -1200), "region": "EU", "companies": ["itcc", "stokes"]},
    "uppsala": {"name": "Uppsala", "coords": (1200, -1300), "region": "EU", "companies": ["itcc", "stokes"]},
    "vasteras": {"name": "Västerås", "coords": (1150, -1250), "region": "EU", "companies": ["itcc", "stokes"]},
    "linkoping": {"name": "Linköping", "coords": (1050, -1150), "region": "EU", "companies": ["itcc", "stokes"]},
    "orebro": {"name": "Örebro", "coords": (1100, -1200), "region": "EU", "companies": ["itcc", "stokes"]},
    "jonkoping": {"name": "Jönköping", "coords": (1000, -1100), "region": "EU", "companies": ["itcc", "stokes"]},
    "helsinki": {"name": "Helsinque", "coords": (2000, -1500), "region": "EU", "companies": ["itcc", "stokes"]},
    "turku": {"name": "Turku", "coords": (1900, -1450), "region": "EU", "companies": ["itcc", "stokes"]},
    "tampere": {"name": "Tampere", "coords": (2000, -1600), "region": "EU", "companies": ["itcc", "stokes"]},
    "lahti": {"name": "Lahti", "coords": (2100, -1550), "region": "EU", "companies": ["itcc", "stokes"]},
    "kouvola": {"name": "Kouvola", "coords": (2200, -1500), "region": "EU", "companies": ["itcc", "stokes"]},
    "kotka": {"name": "Kotka", "coords": (2250, -1450), "region": "EU", "companies": ["itcc", "stokes"]},
    "pori": {"name": "Pori", "coords": (1850, -1550), "region": "EU", "companies": ["itcc", "stokes"]},
    "riga": {"name": "Riga", "coords": (2000, -800), "region": "EU", "companies": ["itcc", "stokes"]},
    "tallinn": {"name": "Tallinn", "coords": (2100, -1100), "region": "EU", "companies": ["itcc", "stokes"]},
    "vilnius": {"name": "Vilnius", "coords": (2100, -500), "region": "EU", "companies": ["itcc", "stokes"]},
    "kaunas": {"name": "Kaunas", "coords": (2000, -450), "region": "EU", "companies": ["itcc", "stokes"]},
    "klaipeda": {"name": "Klaipėda", "coords": (1800, -600), "region": "EU", "companies": ["itcc", "stokes"]},

    # BRASIL
    "sao_paulo": {"name": "São Paulo", "coords": (5000, 5000), "region": "BR", "companies": ["rrb_log", "agronorte"]},
    "rio_janeiro": {"name": "Rio de Janeiro", "coords": (5300, 4800), "region": "BR", "companies": ["rrb_log", "stokes"]},
    "curitiba": {"name": "Curitiba", "coords": (4800, 5500), "region": "BR", "companies": ["rrb_log", "agronorte"]},
    "belo_horizonte": {"name": "Belo Horizonte", "coords": (5100, 4500), "region": "BR", "companies": ["rrb_log"]},
    "porto_alegre": {"name": "Porto Alegre", "coords": (4500, 6000), "region": "BR", "companies": ["rrb_log"]},
    "brasilia": {"name": "Brasília", "coords": (4800, 4000), "region": "BR", "companies": ["rrb_log", "agronorte"]},
}

def get_city_coords(city_id):
    cid = city_id.replace("city.", "")
    return CITY_DATA.get(cid, {}).get("coords", (0, 0))

def get_city_companies(city_id):
    cid = city_id.replace("city.", "")
    return CITY_DATA.get(cid, {}).get("companies", ["itcc", "stokes", "lkwlog"])

def calculate_distance(city1_id, city2_id):
    c1 = get_city_coords(city1_id)
    c2 = get_city_coords(city2_id)
    dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return int(dist * 0.8)

BRAZIL_CITIES_IDS = [cid for cid, data in CITY_DATA.items() if data["region"] == "BR"]
