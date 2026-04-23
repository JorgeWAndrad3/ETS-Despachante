import flet as ft
import random
from app.services.cargo_service import CargoService
from app.services.save_manager import SaveManagerService
from app.services.sii_native import SiiNativeService
from app.models.cargo import City, Company, Cargo
from app.utils.city_database import CITY_MASTER_LIST

def load_initial_data(service):
    """Carrega o banco de dados mestre de cidades e empresas."""
    # Adiciona cidades em ordem alfabética pelo nome
    sorted_cities = sorted(CITY_MASTER_LIST.items(), key=lambda x: x[1])
    for city_id, city_name in sorted_cities:
        c_id = f"city.{city_id}"
        service.add_city(City(c_id, city_name, ["comp.itcc", "comp.stokes", "comp.rrb_log"]))
    
    # Empresas e Cargas
    service.add_company(Company("comp.itcc", "ITCC", "city.paris"))
    service.add_company(Company("comp.stokes", "Stokes", "city.berlin"))
    service.add_company(Company("comp.rrb_log", "RRB Logística", "city.sao_paulo"))
    service.add_cargo(Cargo("cargo.apple", "Maçãs", 15))
    service.add_cargo(Cargo("cargo.electronics", "Eletrônicos", 5))
    service.add_cargo(Cargo("cargo.machinery", "Maquinário Pesado", 25))

def main(page: ft.Page):
    page.title = "ETS2 Cargo Dispatcher PRO"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 950
    page.bgcolor = "#0b0e14"
    page.scroll = ft.ScrollMode.AUTO

    PRIMARY_COLOR = "#e91e63"
    SUCCESS_COLOR = "#00c853"
    
    # Serviços
    service = CargoService()
    save_manager = SaveManagerService()
    sii_native = SiiNativeService()
    load_initial_data(service)
    
    discovered_cities_ids = set()

    # --- Funções de Lógica ---
    def update_city_dropdowns():
        all_cities = sorted(service.cities.values(), key=lambda x: x.name)
        if show_all_cities_sw.value:
            options = [ft.dropdown.Option(c.id, c.name) for c in all_cities if c.id in discovered_cities_ids]
        else:
            options = [ft.dropdown.Option(c.id, c.name) for c in all_cities]
        
        source_city_dd.options = options
        dest_city_dd.options = options
        page.update()

    def update_comp_dd(city_id, dropdown):
        companies = service.get_companies_by_city(city_id)
        dropdown.options = [ft.dropdown.Option(c.id, c.name) for c in companies]
        dropdown.value = companies[0].id if companies else None
        page.update()

    def randomize_cities(e):
        valid_options = source_city_dd.options
        if len(valid_options) > 1:
            source_city_dd.value = random.choice(valid_options).key
            dest_city_dd.value = random.choice(valid_options).key
            update_comp_dd(source_city_dd.value, source_comp_dd)
            update_comp_dd(dest_city_dd.value, dest_comp_dd)
            page.update()

    def randomize_cargo(e):
        if cargo_dd.options:
            cargo_dd.value = random.choice(cargo_dd.options).key
            urgency_dd.value = random.choice(["0", "1", "2"])
            page.update()

    def load_save_data(e):
        nonlocal discovered_cities_ids
        try:
            save_path = save_manager.base_path / "profiles" / profile_dd.value / "save" / save_dd.value / "game.sii"
            content = sii_native.decrypt_save(save_path)
            
            # 1. Extração de Cidades
            known_ids = list(service.cities.keys())
            discovered_cities_ids = sii_native.extract_cities(content, known_city_ids=known_ids)
            
            # 2. Extração de Cargas
            discovered_cargos_ids = sii_native.extract_cargos(content)
            
            # Adiciona cargas novas ao banco de dados dinamicamente
            for cargo_id in discovered_cargos_ids:
                if cargo_id not in service.cargos:
                    # Gera um nome amigável (ex: cargo.apple -> Apple)
                    display_name = cargo_id.replace("cargo.", "").replace("_", " ").title()
                    service.add_cargo(Cargo(cargo_id, display_name, 10))
            
            # Atualiza Dropdowns
            update_city_dropdowns()
            
            # Atualiza Dropdown de Cargas (Ordem Alfabética)
            all_cargos = sorted(service.cargos.values(), key=lambda x: x.name)
            cargo_dd.options = [ft.dropdown.Option(c.id, c.name) for c in all_cargos]
            
            # Transição de tela
            profile_card.visible = False
            main_ui.visible = True
            
            page.snack_bar = ft.SnackBar(
                ft.Text(f"✅ {len(discovered_cities_ids)} cidades e {len(discovered_cargos_ids)} cargas carregadas!"), 
                bgcolor=SUCCESS_COLOR
            )
            page.snack_bar.open = True
            page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {err}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # --- UI Components ---
    # Card de Seleção de Perfil
    profile_dd = ft.Dropdown(label="Perfil", width=350, on_change=lambda _: on_profile_change())
    save_dd = ft.Dropdown(label="Save", width=250, disabled=True)
    load_btn = ft.ElevatedButton("CARREGAR SAVE", icon=ft.icons.PLAY_ARROW, bgcolor=PRIMARY_COLOR, color="white", on_click=load_save_data, height=50)
    
    profile_card = ft.Container(
        content=ft.Column([
            ft.Text("CONFIGURAÇÃO DO PERFIL", size=14, weight="bold", color=PRIMARY_COLOR),
            ft.Row([profile_dd, save_dd, load_btn], spacing=20, alignment=ft.MainAxisAlignment.CENTER)
        ]),
        padding=20, bgcolor="#161b22", border_radius=12, border=ft.border.all(1, "#30363d")
    )

    def on_profile_change():
        saves = save_manager.list_saves(profile_dd.value)
        save_dd.options = [ft.dropdown.Option(s.id, s.display_name) for s in saves]
        save_dd.disabled = False
        if saves: save_dd.value = saves[0].id
        load_btn.disabled = False
        page.update()

    # Painel de Despacho
    show_all_cities_sw = ft.Switch(label="Somente descobertas", value=False, on_change=lambda _: update_city_dropdowns())
    source_city_dd = ft.Dropdown(label="Cidade de Origem", width=400, on_change=lambda e: update_comp_dd(e.data, source_comp_dd))
    source_comp_dd = ft.Dropdown(label="Empresa de Origem", width=400)
    
    dest_city_dd = ft.Dropdown(label="Cidade de Destino", width=400, on_change=lambda e: update_comp_dd(e.data, dest_comp_dd))
    dest_comp_dd = ft.Dropdown(label="Empresa de Destino", width=400)
    
    cargo_dd = ft.Dropdown(label="Carga", width=400, options=[ft.dropdown.Option(c.id, c.name) for c in sorted(service.cargos.values(), key=lambda x: x.name)])
    urgency_dd = ft.Dropdown(label="Urgência", width=200, value="0", options=[ft.dropdown.Option("0", "Normal"), ft.dropdown.Option("1", "Urgente"), ft.dropdown.Option("2", "Crítica")])
    trailer_dd = ft.Dropdown(label="Tipo de Reboque", width=400, value="curtain", options=[ft.dropdown.Option("curtain", "Sider (Lonado)"), ft.dropdown.Option("refrigerated", "Frigorífico"), ft.dropdown.Option("flatbed", "Prancha")])

    main_ui = ft.Column([
        ft.Row([
            ft.Column([
                ft.Text("📦 ORIGEM E DESTINO", weight="bold", color=PRIMARY_COLOR),
                source_city_dd, source_comp_dd,
                ft.Divider(height=10, color="transparent"),
                dest_city_dd, dest_comp_dd,
                ft.ElevatedButton("RANDOMIZAR ROTA", icon=ft.icons.SHUFFLE, on_click=randomize_cities),
                show_all_cities_sw
            ], width=450),
            ft.VerticalDivider(width=40),
            ft.Column([
                ft.Text("🚛 ESPECIFICAÇÕES", weight="bold", color=PRIMARY_COLOR),
                cargo_dd,
                urgency_dd,
                trailer_dd,
                ft.ElevatedButton("RANDOMIZAR CARGA", icon=ft.icons.SHUFFLE, on_click=randomize_cargo)
            ], width=450)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=40),
        ft.ElevatedButton(
            "GERAR E INJETAR CARGA NO SAVE", 
            icon=ft.icons.ADD_TASK, 
            bgcolor=SUCCESS_COLOR, 
            color="white", 
            height=70, 
            width=940,
            on_click=lambda _: print("Injetando...")
        )
    ], visible=False, alignment=ft.MainAxisAlignment.CENTER)

    # Montagem Final
    page.add(
        ft.Column([
            ft.Row([
                ft.Icon(ft.icons.LOCAL_SHIPPING, color=PRIMARY_COLOR, size=40),
                ft.Text("ETS2 CARGO DISPATCHER PRO", size=32, weight="bold")
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=20),
            profile_card,
            ft.Divider(height=40, color="#30363d"),
            main_ui
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    # Inicialização
    profiles = save_manager.list_profiles()
    profile_dd.options = [ft.dropdown.Option(p.id, p.name) for p in profiles]
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
