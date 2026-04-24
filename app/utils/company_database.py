# Banco de Dados de Regras Logísticas (Exportação/Importação)
# Mapeamento estendido das empresas SCS (Base + DLCs)

COMPANY_RULES = {
    # Base Game & Common
    "itcc": {"name": "ITCC", "exports": ["cargo.apples", "cargo.potatoes"], "imports": ["cargo.machinery"]},
    "stokes": {"name": "Stokes", "exports": ["cargo.electronics"], "imports": ["cargo.apples"]},
    "lkwlog": {"name": "LKW Logistik", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    "sanbuilders": {"name": "Sanbuilders", "exports": ["cargo.machinery"], "imports": ["cargo.cement"]},
    "euroacres": {"name": "EuroAcres", "exports": ["cargo.apples", "cargo.milk"], "imports": ["cargo.machinery"]},
    "posped": {"name": "Posped", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "tradeaux": {"name": "Tradeaux", "exports": ["cargo.electronics"], "imports": ["cargo.food"]},
    "trameri": {"name": "Trameri", "exports": ["cargo.machinery"], "imports": ["cargo.iron_pipes"]},
    "transinet": {"name": "Transinet", "exports": ["cargo.electronics"], "imports": ["cargo.machinery"]},
    "fcp": {"name": "FCP", "exports": ["cargo.cars"], "imports": ["cargo.machinery"]},
    "wgcc": {"name": "WGCC", "exports": ["cargo.oil"], "imports": ["cargo.machinery"]},
    "quarry": {"name": "Quarry", "exports": ["cargo.coal"], "imports": ["cargo.machinery"]},
    "kaarfor": {"name": "Kaarfor", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "sellplan": {"name": "SellPlan", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    
    # Scandinavia
    "gnt": {"name": "GNT", "exports": ["cargo.milk"], "imports": ["cargo.food"]},
    "ika_bohag": {"name": "Ika Bohag", "exports": ["cargo.furniture"], "imports": ["cargo.electronics"]},
    "nordic_ste": {"name": "Nordic Stenbrott", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    
    # France
    "boisserie": {"name": "Boisserie", "exports": ["cargo.wine"], "imports": ["cargo.glass"]},
    "batisse": {"name": "Batisse", "exports": ["cargo.cement"], "imports": ["cargo.machinery"]},
    
    # Italy
    "marmo": {"name": "Marmo SpA", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    
    # Brasil (RRB / EAA)
    "rrb_log": {"name": "RRB Logística", "exports": ["cargo.cafe", "cargo.soja"], "imports": ["cargo.cerveja"]},
    "agronorte": {"name": "Agro Norte", "exports": ["cargo.soja", "cargo.milho"], "imports": ["cargo.machinery"]},
}

# IDs Genéricos (Para preenchimento do modo livre)
GENERIC_COMPANIES = [
    "bhv", "bcl", "tree_et", "vitas_power", "stefan_p", "scania", "volvo", "renault", 
    "man", "daf", "mercedes", "iveco", "norrsken", "nordic_cr", "konstnorr", "vpk",
    "drekkar", "marina", "polar_fish", "sag_tre", "scania_fac", "volvo_fac",
    "chimi", "fle", "globeur", "huilant", "subse", "voitureux", "wilnet", 
    "cargotras", "e_leclerc", "nuclon", "cesta", "exomar", "f_gas", "spinelli",
    "tesoro", "unite_d", "baltrak", "blt", "domdepo", "evro_pk", "ladoga",
    "lativia", "radus", "rosmark", "ukr_p_l", "vl_f"
]
