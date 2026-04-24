import math

# Banco de Dados Mestre com Regiões e Coordenadas
CITY_DATA = {
    # EUROPA (EU)
    "paris": {"name": "Paris", "coords": (0, 0), "region": "EU", "companies": ["itcc", "stokes", "lkwlog", "tradeaux"]},
    "berlin": {"name": "Berlin", "coords": (1000, -200), "region": "EU", "companies": ["stokes", "euroacres", "posped"]},
    "london": {"name": "Londres", "coords": (-800, -500), "region": "EU", "companies": ["stokes", "trameri", "posped"]},
    "praga": {"name": "Praga", "coords": (800, 200), "region": "EU", "companies": ["itcc", "posped", "euroacres"]},
    "brussel": {"name": "Bruxelas", "coords": (-200, -300), "region": "EU", "companies": ["stokes", "lkwlog", "tradeaux"]},
    "lyon": {"name": "Lyon", "coords": (-100, 500), "region": "EU", "companies": ["itcc", "stokes", "boisserie"]},
    "amsterdam": {"name": "Amsterdã", "coords": (0, -400), "region": "EU", "companies": ["itcc", "stokes", "lkwlog"]},
    "roma": {"name": "Roma", "coords": (500, 1200), "region": "EU", "companies": ["itcc", "marmo", "fcp"]},
    "madrid": {"name": "Madrid", "coords": (-1500, 1500), "region": "EU", "companies": ["itcc", "stokes", "tradeaux"]},
    "lisboa": {"name": "Lisboa", "coords": (-2200, 1800), "region": "EU", "companies": ["itcc", "stokes"]},
    "warszawa": {"name": "Varsóvia", "coords": (1500, -100), "region": "EU", "companies": ["posped", "lkwlog"]},
    "vienna": {"name": "Viena", "coords": (1200, 400), "region": "EU", "companies": ["itcc", "stokes"]},
    "stockholm": {"name": "Estocolmo", "coords": (1100, -1200), "region": "EU", "companies": ["ika_bohag", "gnt"]},
    "oslo": {"name": "Oslo", "coords": (600, -1300), "region": "EU", "companies": ["ika_bohag", "gnt"]},
    "munchen": {"name": "Munique", "coords": (800, 300), "region": "EU", "companies": ["itcc", "stokes"]},
    "milano": {"name": "Milão", "coords": (400, 700), "region": "EU", "companies": ["itcc", "fcp"]},
    "barcelona": {"name": "Barcelona", "coords": (-900, 1300), "region": "EU", "companies": ["itcc", "stokes"]},
    "hamburg": {"name": "Hamburgo", "coords": (700, -400), "region": "EU", "companies": ["lkwlog", "stokes"]},
    "frankfurt": {"name": "Frankfurt", "coords": (600, 0), "region": "EU", "companies": ["itcc", "lkwlog"]},

    # BRASIL (BR)
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

# Lista de IDs para detecção rápida de mapa
BRAZIL_CITIES_IDS = [cid for cid, data in CITY_DATA.items() if data["region"] == "BR"]
