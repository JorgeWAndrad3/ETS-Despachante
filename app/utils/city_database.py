# Banco de Dados Mestre de Cidades com Coordenadas e Empresas
# Coordenadas (x, z) servem para calcular a distância em KM

CITY_DATA = {
    "paris": {"name": "Paris", "coords": (0, 0), "companies": ["itcc", "stokes", "lkwlog", "tradeaux"]},
    "berlin": {"name": "Berlin", "coords": (1000, -200), "companies": ["stokes", "euroacres", "posped"]},
    "london": {"name": "Londres", "coords": (-800, -500), "companies": ["stokes", "trameri", "posped"]},
    "roma": {"name": "Roma", "coords": (500, 1200), "companies": ["itcc", "marmo", "fcp"]},
    "madrid": {"name": "Madrid", "coords": (-1500, 1500), "companies": ["itcc", "stokes", "tradeaux"]},
    "lisboa": {"name": "Lisboa", "coords": (-2200, 1800), "companies": ["itcc", "stokes"]},
    "praga": {"name": "Praga", "coords": (800, 200), "companies": ["itcc", "posped", "euroacres"]},
    "brussel": {"name": "Bruxelas", "coords": (-200, -300), "companies": ["stokes", "lkwlog", "tradeaux"]},
    "lyon": {"name": "Lyon", "coords": (-100, 500), "companies": ["itcc", "stokes", "boisserie"]},
    "amsterdam": {"name": "Amsterdã", "coords": (0, -400), "companies": ["itcc", "stokes", "lkwlog"]},
    # Brasil (Exemplo)
    "sao_paulo": {"name": "São Paulo", "coords": (5000, 5000), "companies": ["rrb_log", "agronorte"]},
    "curitiba": {"name": "Curitiba", "coords": (4800, 5500), "companies": ["rrb_log", "stokes"]},
}

# Funções auxiliares
def get_city_coords(city_id):
    city_id = city_id.replace("city.", "")
    return CITY_DATA.get(city_id, {}).get("coords", (0, 0))

def get_city_companies(city_id):
    city_id = city_id.replace("city.", "")
    return CITY_DATA.get(city_id, {}).get("companies", ["itcc", "stokes", "lkwlog"]) # Fallback

def calculate_distance(city1_id, city2_id):
    import math
    c1 = get_city_coords(city1_id)
    c2 = get_city_coords(city2_id)
    # Distância Euclidiana simplificada (ajustada para escala ETS2 ~1:19)
    dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return int(dist * 0.8) # Fator de ajuste para KM
