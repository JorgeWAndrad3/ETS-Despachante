# Banco de Dados de Regras Logísticas (Exportação/Importação)

COMPANY_RULES = {
    # Novas Empresas Mapeadas
    "eurogoodies": {"name": "EuroGoodies", "exports": ["cargo.apples", "cargo.potatoes", "cargo.food"], "imports": ["cargo.electronics"]},
    "sellplan": {"name": "SellPlan", "exports": ["cargo.food", "cargo.vegetables"], "imports": ["cargo.electronics", "cargo.computers"]},
    "batisse": {"name": "Bâtisse", "exports": ["cargo.cement", "cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    "bhv": {"name": "BHV", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    "fle": {"name": "FLE", "exports": ["cargo.milk", "cargo.yogurt"], "imports": ["cargo.food"]},
    "lisette_log": {"name": "Lisette Logistics", "exports": ["cargo.electronics"], "imports": ["cargo.food"]},
    "voitureux": {"name": "Voitureux", "exports": ["cargo.cars"], "imports": ["cargo.machinery"]},
    "steinbruch": {"name": "Steinbruch", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    
    # Base Game & Common
    "itcc": {"name": "ITCC", "exports": ["cargo.apples", "cargo.potatoes"], "imports": ["cargo.machinery"]},
    "stokes": {"name": "Stokes", "exports": ["cargo.electronics"], "imports": ["cargo.apples"]},
    "lkwlog": {"name": "LkwLog GmbH", "exports": ["cargo.iron_pipes", "cargo.machinery"], "imports": ["cargo.cement"]},
    "sanbuilders": {"name": "Sanbuilders", "exports": ["cargo.machinery"], "imports": ["cargo.cement"]},
    "euroacres": {"name": "EuroAcres", "exports": ["cargo.apples", "cargo.milk"], "imports": ["cargo.machinery"]},
    "posped": {"name": "Posped", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "tradeaux": {"name": "Tradeaux", "exports": ["cargo.electronics"], "imports": ["cargo.food"]},
    "trameri": {"name": "Trameri", "exports": ["cargo.machinery"], "imports": ["cargo.iron_pipes"]},
    "transinet": {"name": "Transinet", "exports": ["cargo.electronics"], "imports": ["cargo.machinery"]},
    "fcp": {"name": "FCP", "exports": ["cargo.cars"], "imports": ["cargo.machinery"]},
    "wgcc": {"name": "WGCC", "exports": ["cargo.oil"], "imports": ["cargo.machinery"]},
    "kaarfor": {"name": "Kaarfor", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "ika_bohag": {"name": "Ika Bohag", "exports": ["cargo.furniture"], "imports": ["cargo.electronics"]},
    "rrb_log": {"name": "RRB Logística", "exports": ["cargo.cafe", "cargo.soja"], "imports": ["cargo.cerveja"]},
}

GENERIC_COMPANIES = list(COMPANY_RULES.keys())
