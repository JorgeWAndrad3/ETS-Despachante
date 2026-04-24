# Banco de Dados de Regras Logísticas (Exportação/Importação)

COMPANY_RULES = {
    "itcc": {
        "name": "ITCC",
        "exports": ["cargo.apples", "cargo.potatoes", "cargo.vegetables"],
        "imports": ["cargo.machinery", "cargo.electronics"]
    },
    "stokes": {
        "name": "Stokes",
        "exports": ["cargo.electronics", "cargo.computers"],
        "imports": ["cargo.apples", "cargo.food"]
    },
    "lkwlog": {
        "name": "LKW Logistik",
        "exports": ["cargo.iron_pipes", "cargo.cement"],
        "imports": ["cargo.machinery"]
    },
    "sanbuilders": {
        "name": "Sanbuilders",
        "exports": ["cargo.machinery"],
        "imports": ["cargo.cement", "cargo.iron_pipes"]
    },
    "rrb_log": {
        "name": "RRB Logistica",
        "exports": ["cargo.cafe", "cargo.soja", "cargo.milho"],
        "imports": ["cargo.cerveja", "cargo.carne_sol"]
    }
}
