import flet as ft
import random
from app.services.cargo_service import CargoService
from app.services.save_manager import SaveManagerService
from app.services.sii_native import SiiNativeService
from app.models.cargo import City, Company, Cargo
from app.utils.city_database import GLOBAL_CITY_LIST, EUROPE_CITIES, BRAZIL_CITIES
from app.utils.cargo_database import CARGO_MASTER_LIST
from app.utils.company_database import COMPANY_RULES

def load_initial_data(service):
    """Carrega o banco de dados mestre inicial."""
    # 1. Cidades
    for city_id, city_name in GLOBAL_CITY_LIST.items():
        # Associamos empresas genéricas a cada cidade para teste
        service.add_city(City(f"city.{city_id}", city_name, ["itcc", "stokes", "lkwlog", "rrb_log"]))
    
    # 2. Empresas com Regras
    for comp_id, rules in COMPANY_RULES.items():
        # Criamos instâncias da empresa para as cidades (exemplo simplificado)
        service.add_company(Company(comp_id, rules["name"], "city.paris", exports=rules["exports"], imports=rules["imports"]))

    # 3. Cargas
    for cargo_id, cargo_name in CARGO_MASTER_LIST.items():
        service.add_cargo(Cargo(f"cargo.{cargo_id}", cargo_name, 10))

def main(page: ft.Page):
    page.title = "ETS2 Cargo Dispatcher PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 950
    page.bgcolor = "#0b0e14"
    page.scroll = ft.ScrollMode.AUTO

    PRIMARY_COLOR = "#e91e63"
    SUCCESS_COLOR = "#00c853"
    
    service = CargoService()
    save_manager = SaveManagerService()
    sii_native = SiiNativeService()
    load_initial_data(service)
    
    discovered_cities_ids = set()
    is_brazil_map = False

    # --- Funções de Lógica de Filtragem ---
    def update_city_dropdowns():
        base_list = GLOBAL_CITY_LIST if is_brazil_map else EUROPE_CITIES
        all_cities_objs = [City(f"city.{cid}", cname, []) for cid, cname in base_list.items()]
        all_cities_sorted = sorted(all_cities_objs, key=lambda x: x.name)
        
        options = [ft.dropdown.Option(c.id, c.name) for c in all_cities_sorted]
        if show_all_cities_sw.value:
            options = [o for o in options if o.key in discovered_cities_ids]
        
        for dd in [source_city_dd, dest_city_dd, own_source_city_dd, own_dest_city_dd]:
            dd.options = options
        page.update()

    def on_source_comp_change(e, cargo_dd_ref, dest_city_dd_ref):
        if not realistic_mode_sw.value:
            return
        
        comp_id = e.data
        company = service.companies.get(comp_id)
        if company and company.exports:
            # Filtra cargas que a empresa EXPORTA
            cargo_dd_ref.options = [ft.dropdown.Option(c_id, service.cargos[c_id].name) 
                                   for c_id in company.exports if c_id in service.cargos]
            if cargo_dd_ref.options: cargo_dd_ref.value = cargo_dd_ref.options[0].key
        page.update()

    def on_cargo_change(e, dest_city_dd_ref):
        if not realistic_mode_sw.value:
            return
        
        cargo_id = e.data
        # Encontra cidades que tenham empresas que IMPORTAM essa carga
        valid_cities = set()
        for comp in service.companies.values():
            if comp.imports and cargo_id in comp.imports:
                valid_cities.add(comp.city_id)
        
        if valid_cities:
            all_cities = [service.cities[cid] for cid in valid_cities if cid in service.cities]
            dest_city_dd_ref.options = [ft.dropdown.Option(c.id, c.name) for c in sorted(all_cities, key=lambda x: x.name)]
            if dest_city_dd_ref.options: dest_city_dd_ref.value = dest_city_dd_ref.options[0].key
        page.update()

    # --- UI Components ---
    realistic_mode_sw = ft.Switch(label="Respeitar mercado logístico", value=False, active_color=PRIMARY_COLOR)
    show_all_cities_sw = ft.Switch(label="Somente descobertas", value=False, on_change=lambda _: update_city_dropdowns())
    
    # Dropdowns Mercado Fretes
    source_city_dd = ft.Dropdown(label="Origem", width=300, on_change=lambda e: update_comp_dd(e.data, source_comp_dd))
    source_comp_dd = ft.Dropdown(label="Empresa", width=300, on_change=lambda e: on_source_comp_change(e, cargo_dd, dest_city_dd))
    dest_city_dd = ft.Dropdown(label="Destino", width=300, on_change=lambda e: update_comp_dd(e.data, dest_comp_dd))
    dest_comp_dd = ft.Dropdown(label="Empresa", width=300)
    cargo_dd = ft.Dropdown(label="Carga", width=400, on_change=lambda e: on_cargo_change(e, dest_city_dd))
    trailer_dd = ft.Dropdown(label="Reboque do Jogo", width=300, value="curtain", options=[ft.dropdown.Option("curtain", "Sider"), ft.dropdown.Option("flatbed", "Prancha")])

    # Dropdowns Reboque Próprio
    own_source_city_dd = ft.Dropdown(label="Origem", width=300, on_change=lambda e: update_comp_dd(e.data, own_source_comp_dd))
    own_source_comp_dd = ft.Dropdown(label="Empresa", width=300, on_change=lambda e: on_source_comp_change(e, own_cargo_dd, own_dest_city_dd))
    own_dest_city_dd = ft.Dropdown(label="Destino", width=300, on_change=lambda e: update_comp_dd(e.data, own_dest_comp_dd))
    own_dest_comp_dd = ft.Dropdown(label="Empresa", width=300)
    own_cargo_dd = ft.Dropdown(label="Carga", width=620, on_change=lambda e: on_cargo_change(e, own_dest_city_dd))

    def update_comp_dd(city_id, dropdown):
        # Aqui, como é um protótipo, vamos mostrar as mesmas 4 empresas para todas as cidades
        companies = [service.companies[cid] for cid in ["itcc", "stokes", "lkwlog", "rrb_log"]]
        dropdown.options = [ft.dropdown.Option(c.id, c.name) for c in companies]
        dropdown.value = companies[0].id
        page.update()

    def load_save_data(e):
        nonlocal discovered_cities_ids, is_brazil_map
        try:
            save_path = save_manager.base_path / "profiles" / profile_dd.value / "save" / save_dd.value / "game.sii"
            content = sii_native.decrypt_save(save_path)
            known_ids = [f"city.{cid}" for cid in GLOBAL_CITY_LIST.keys()]
            discovered_cities_ids = sii_native.extract_cities(content, known_city_ids=known_ids)
            is_brazil_map = any(cid.replace("city.", "") in BRAZIL_CITIES for cid in discovered_cities_ids)
            
            discovered_cargos_ids = sii_native.extract_cargos(content)
            for cargo_id in discovered_cargos_ids:
                if cargo_id not in service.cargos:
                    service.add_cargo(Cargo(cargo_id, cargo_id.replace("cargo.", "").title(), 10))
            
            update_city_dropdowns()
            all_cargos = [ft.dropdown.Option(c.id, c.name) for c in sorted(service.cargos.values(), key=lambda x: x.name)]
            cargo_dd.options = all_cargos
            own_cargo_dd.options = all_cargos
            
            profile_card.visible = False
            main_tabs.visible = True
            page.snack_bar = ft.SnackBar(ft.Text(f"✅ Save carregado! Mapa: {'Brasil' if is_brazil_map else 'Europa'}"), bgcolor=SUCCESS_COLOR)
            page.snack_bar.open = True
            page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {err}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # --- UI Helpers ---
    def create_section(title, content):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=16, weight="bold", color=PRIMARY_COLOR),
                ft.Divider(height=10, color="transparent"),
                content
            ]),
            padding=20, bgcolor="#161b22", border_radius=12, border=ft.border.all(1, "#30363d")
        )

    # --- Seleção Perfil ---
    profile_dd = ft.Dropdown(label="Perfil", width=350, on_change=lambda _: on_profile_change())
    save_dd = ft.Dropdown(label="Save", width=250, disabled=True)
    load_btn = ft.ElevatedButton("CARREGAR SAVE", bgcolor=PRIMARY_COLOR, color="white", on_click=load_save_data, height=50)
    profile_card = ft.Container(content=ft.Row([profile_dd, save_dd, load_btn], alignment=ft.MainAxisAlignment.CENTER), padding=20)

    def on_profile_change():
        saves = save_manager.list_saves(profile_dd.value)
        save_dd.options = [ft.dropdown.Option(s.id, s.display_name) for s in saves]
        save_dd.disabled = False
        if saves: save_dd.value = saves[0].id
        load_btn.disabled = False
        page.update()

    # --- Views ---
    mercado_fretes_view = ft.Column([
        ft.Row([
            create_section("📍 ORIGEM", ft.Column([source_city_dd, source_comp_dd])),
            create_section("🏁 DESTINO", ft.Column([dest_city_dd, dest_comp_dd])),
        ], spacing=20),
        create_section("📦 CARGA E REBOQUE", ft.Row([cargo_dd, trailer_dd], spacing=20)),
        ft.ElevatedButton("GERAR NO MERCADO DE FRETES", icon=ft.icons.ADD_TASK, bgcolor=SUCCESS_COLOR, color="white", height=60, width=940)
    ], spacing=20)

    mercado_cargas_view = ft.Column([
        ft.Row([
            create_section("📍 ONDE VOCÊ ESTÁ", ft.Column([own_source_city_dd, own_source_comp_dd])),
            create_section("🏁 PARA ONDE VAI", ft.Column([own_dest_city_dd, own_dest_comp_dd])),
        ], spacing=20),
        create_section("📦 SELECIONE A CARGA", ft.Row([own_cargo_dd], spacing=20)),
        ft.ElevatedButton("GERAR PARA MEU REBOQUE", icon=ft.icons.LOCAL_SHIPPING, bgcolor="#2196F3", color="white", height=60, width=940)
    ], spacing=20)

    main_tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="MERCADO DE FRETES", icon=ft.icons.ASSIGNMENT, content=ft.Container(mercado_fretes_view, padding=20)),
            ft.Tab(text="REBOQUE PRÓPRIO", icon=ft.icons.LOCAL_SHIPPING, content=ft.Container(mercado_cargas_view, padding=20)),
        ],
        visible=False,
        expand=1
    )

    page.add(
        ft.Column([
            ft.Row([ft.Icon(ft.icons.LOCAL_SHIPPING, color=PRIMARY_COLOR, size=40), ft.Text("ETS2 CARGO DISPATCHER PRO", size=32, weight="bold")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=10),
            profile_card,
            ft.Row([realistic_mode_sw, show_all_cities_sw], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
            ft.Divider(height=20, color="#30363d"),
            main_tabs
        ])
    )
    
    profiles = save_manager.list_profiles()
    if profiles: profile_dd.options = [ft.dropdown.Option(p.id, p.name) for p in profiles]
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
