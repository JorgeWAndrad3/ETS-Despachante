# Banco de Dados de Regras Logísticas (Exportação/Importação)
# Atualizado com empresas reais do Base Game + DLCs (França, Itália, etc.)

COMPANY_RULES = {
    # Ajaccio & França
    "bhv": {"name": "BHV", "exports": ["cargo.iron_pipes"], "imports": ["cargo.machinery"]},
    "huilant": {"name": "Huilant", "exports": ["cargo.oil"], "imports": ["cargo.machinery"]},
    "kaarfor": {"name": "Kaarfor", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "lisette_log": {"name": "Lisette Logistics", "exports": ["cargo.electronics"], "imports": ["cargo.food"]},
    "marina": {"name": "Marina", "exports": ["cargo.yacht"], "imports": ["cargo.food"]},
    "mvm_carriere": {"name": "MVM Carrière", "exports": ["cargo.cement"], "imports": ["cargo.machinery"]},
    "tradeaux": {"name": "Tradeaux", "exports": ["cargo.electronics"], "imports": ["cargo.food"]},
    "batisse": {"name": "Bâtisse", "exports": ["cargo.cement"], "imports": ["cargo.iron_pipes"]},
    
    # Itália & Outros
    "eurogoodies": {"name": "EuroGoodies", "exports": ["cargo.apples", "cargo.potatoes"], "imports": ["cargo.electronics"]},
    "sellplan": {"name": "SellPlan", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "lkwlog": {"name": "LkwLog GmbH", "exports": ["cargo.iron_pipes"], "imports": ["cargo.cement"]},
    "stokes": {"name": "Stokes", "exports": ["cargo.electronics"], "imports": ["cargo.apples"]},
    "nbfc": {"name": "NBFC", "exports": ["cargo.oil"], "imports": ["cargo.machinery"]},
    "sanbuilders": {"name": "Sanbuilders", "exports": ["cargo.machinery"], "imports": ["cargo.cement"]},
    "tree_et": {"name": "Tree-ET", "exports": ["cargo.logs"], "imports": ["cargo.machinery"]},
    "wgcc": {"name": "WGCC", "exports": ["cargo.chemicals"], "imports": ["cargo.machinery"]},
    "posped": {"name": "Posped", "exports": ["cargo.food"], "imports": ["cargo.electronics"]},
    "trameri": {"name": "Trameri", "exports": ["cargo.machinery"], "imports": ["cargo.iron_pipes"]},
    "itcc": {"name": "ITCC", "exports": ["cargo.chemicals"], "imports": ["cargo.machinery"]},
    "fcp": {"name": "FCP", "exports": ["cargo.cars"], "imports": ["cargo.machinery"]},
    "ika_bohag": {"name": "Ika Bohag", "exports": ["cargo.furniture"], "imports": ["cargo.electronics"]},
    "fle": {"name": "FLE", "exports": ["cargo.milk"], "imports": ["cargo.food"]},
    "voitureux": {"name": "Voitureux", "exports": ["cargo.cars"], "imports": ["cargo.machinery"]},
    "bcp": {"name": "BCP", "exports": ["cargo.electronics"], "imports": ["cargo.machinery"]},
    "scania_dealer": {"name": "Scania Dealer", "exports": ["cargo.trucks"], "imports": ["cargo.trucks"]},
    "volvo_dealer": {"name": "Volvo Dealer", "exports": ["cargo.trucks"], "imports": ["cargo.trucks"]},
    
    # Brasil (Exemplos)
    "rrb_log": {"name": "RRB Logística", "exports": ["cargo.cafe"], "imports": ["cargo.cerveja"]},
}

GENERIC_COMPANIES = list(COMPANY_RULES.keys())
