# Banco de Dados Mestre de Cargas do ETS2 com Classificação
# Tipos: 'danger' (Perigosa), 'fragile' (Frágil), 'heavy' (Pesada), 'normal'

CARGO_MASTER_LIST = {
    # Perigosas (ADR)
    "adr_explosiv": {"name": "Explosivos", "type": "danger"},
    "adr_toxic": {"name": "Substâncias Tóxicas", "type": "danger"},
    "adr_flamm": {"name": "Líquidos Inflamáveis", "type": "danger"},
    "oil": {"name": "Óleo Combustível", "type": "danger"},
    "chemicals": {"name": "Produtos Químicos", "type": "danger"},
    
    # Frágeis
    "electronics": {"name": "Eletrônicos", "type": "fragile"},
    "computers": {"name": "Computadores", "type": "fragile"},
    "glass": {"name": "Vidros", "type": "fragile"},
    "wine": {"name": "Vinhos Finos", "type": "fragile"},
    "yogurt": {"name": "Iogurte", "type": "fragile"},
    "medical_sup": {"name": "Suprimentos Médicos", "type": "fragile"},
    
    # Pesadas
    "machinery": {"name": "Maquinário Industrial", "type": "heavy"},
    "diggers": {"name": "Escavadeiras", "type": "heavy"},
    "tractors": {"name": "Tratores", "type": "heavy"},
    "iron_pipes": {"name": "Tubos de Ferro", "type": "heavy"},
    "cement": {"name": "Blocos de Cimento", "type": "heavy"},
    "coal": {"name": "Carvão", "type": "heavy"},
    "logs": {"name": "Troncos de Árvore", "type": "heavy"},

    # Normais
    "apples": {"name": "Maçãs", "type": "normal"},
    "potatoes": {"name": "Batatas", "type": "normal"},
    "vegetables": {"name": "Vegetais", "type": "normal"},
    "milk": {"name": "Leite", "type": "normal"},
    "flour": {"name": "Farinha", "type": "normal"},
    "sugar": {"name": "Açúcar", "type": "normal"},
    "toys": {"name": "Brinquedos", "type": "normal"},
}

# Cargas do Mapa RRB / Brasil
RRB_CARGOS = {
    "cerveja": {"name": "Cerveja Gelada", "type": "fragile"},
    "carne_sol": {"name": "Carne de Sol", "type": "normal"},
    "soja": {"name": "Soja", "type": "normal"},
    "milho": {"name": "Milho", "type": "normal"},
    "cafe": {"name": "Café em Grãos", "type": "normal"},
}

CARGO_MASTER_LIST.update(RRB_CARGOS)

def get_cargo_icon(cargo_type):
    icons = {
        "danger": "☢️",
        "fragile": "📦",
        "heavy": "🏋️",
        "normal": "🚛"
    }
    return icons.get(cargo_type, "🚛")
