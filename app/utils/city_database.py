import math

# Banco de Dados OFICIAL de Cidades e Empresas (Fonte: Wiki/Game Data)
CITY_DATA = {
    # EUROPA
    "paris": {
        "name": "Paris", "coords": (0, 0), "region": "EU", 
        "companies": ["batisse", "bhv", "fle", "ika_bohag", "lisette_log", "tradeaux", "voitureux"]
    },
    "berlin": {
        "name": "Berlin", "coords": (1000, -200), "region": "EU", 
        "companies": ["eurogoodies", "lkwlog", "posped", "stokes", "trameri"]
    },
    "london": {
        "name": "Londres", "coords": (-800, -500), "region": "EU", 
        "companies": ["eurogoodies", "stokes", "trameri", "posped"]
    },
    "venezia": {
        "name": "Veneza", "coords": (700, 750), "region": "EU", 
        "companies": ["eurogoodies", "lkwlog", "sellplan"]
    },
    "praga": {
        "name": "Praga", "coords": (800, 200), "region": "EU", 
        "companies": ["eurogoodies", "posped", "stokes", "itcc"]
    },
    "brussel": {
        "name": "Bruxelas", "coords": (-200, -300), "region": "EU", 
        "companies": ["eurogoodies", "lkwlog", "stokes", "tradeaux"]
    },
    "lyon": {
        "name": "Lyon", "coords": (-100, 500), "region": "EU", 
        "companies": ["batisse", "kaarfor", "tradeaux", "trameri", "steinbruch"]
    },
    "amsterdam": {
        "name": "Amsterdã", "coords": (0, -400), "region": "EU", 
        "companies": ["eurogoodies", "lkwlog", "stokes", "itcc"]
    },
    "roma": {
        "name": "Roma", "coords": (500, 1200), "region": "EU", 
        "companies": ["cesta", "exomar", "f_gas", "marmo", "tesoro"]
    },
    "madrid": {
        "name": "Madrid", "coords": (-1500, 1500), "region": "EU", 
        "companies": ["agregados", "casas", "corteva", "logistica"]
    },
    "lisboa": {
        "name": "Lisboa", "coords": (-2200, 1800), "region": "EU", 
        "companies": ["corteva", "eurogoodies", "stokes"]
    },
    "warszawa": {
        "name": "Varsóvia", "coords": (1500, -100), "region": "EU", 
        "companies": ["eurogoodies", "lkwlog", "posped"]
    },
    "vienna": {
        "name": "Viena", "coords": (1200, 400), "region": "EU", 
        "companies": ["eurogoodies", "stokes", "itcc"]
    },
    "munchen": {
        "name": "Munique", "coords": (800, 300), "region": "EU", 
        "companies": ["eurogoodies", "stokes", "trameri"]
    },

    # BRASIL (Exemplos reais EAA/RRB)
    "sao_paulo": {"name": "São Paulo", "coords": (5000, 5000), "region": "BR", "companies": ["rrb_log", "agronorte", "braspress"]},
    "rio_janeiro": {"name": "Rio de Janeiro", "coords": (5300, 4800), "region": "BR", "companies": ["rrb_log", "stokes", "sedex"]},
    "curitiba": {"name": "Curitiba", "coords": (4800, 5500), "region": "BR", "companies": ["rrb_log", "agronorte", "volvo_fac"]},
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
    dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return int(dist * 0.8)

BRAZIL_CITIES_IDS = [cid for cid, data in CITY_DATA.items() if data["region"] == "BR"]
