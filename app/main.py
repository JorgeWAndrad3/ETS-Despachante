import flet as ft
import random
from app.services.cargo_service import CargoService
from app.services.save_manager import SaveManagerService
from app.services.sii_native import SiiNativeService
from app.models.cargo import City, Company, Cargo
from app.utils.city_database import GLOBAL_CITY_LIST, EUROPE_CITIES, BRAZIL_CITIES
from app.utils.cargo_database import CARGO_MASTER_LIST

def load_initial_data(service):
    """Carrega o banco de dados mestre inicial."""
    for city_id, city_name in GLOBAL_CITY_LIST.items():
        service.add_city(City(f"city.{city_id}", city_name, ["comp.itcc", "comp.stokes", "comp.rrb_log"]))
    
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

    # --- Funções de Lógica ---
    def update_city_dropdowns():
        # Filtra as cidades baseadas na região detectada
        if is_brazil_map:
            base_list = GLOBAL_CITY_LIST
        else:
            base_list = EUROPE_CITIES

        all_cities_objs = []
        for cid, cname in base_list.items():
            all_cities_objs.append(City(f"city.{cid}", cname, []))
            
        all_cities_sorted = sorted(all_cities_objs, key=lambda x: x.name)
        
        if show_all_cities_sw.value:
            options = [ft.dropdown.Option(c.id, c.name) for c in all_cities_sorted if c.id in discovered_cities_ids]
        else:
            options = [ft.dropdown.Option(c.id, c.name) for c in all_cities_sorted]
        
        if not options:
            options = [ft.dropdown.Option("none", "Nenhuma cidade disponível")]
            
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
        nonlocal discovered_cities_ids, is_brazil_map
        try:
            save_path = save_manager.base_path / "profiles" / profile_dd.value / "save" / save_dd.value / "game.sii"
            content = sii_native.decrypt_save(save_path)
            
            # 1. Extração de Cidades
            known_ids = [f"city.{cid}" for cid in GLOBAL_CITY_LIST.keys()]
            discovered_cities_ids = sii_native.extract_cities(content, known_city_ids=known_ids)
            
            # 2. Detecção de Região (Brasil)
            # Se encontrar qualquer cidade que pertence ao banco BR, ativa o modo BR
            is_brazil_map = any(cid.replace("city.", "") in BRAZIL_CITIES for cid in discovered_cities_ids)
            
            # 3. Extração de Cargas
            discovered_cargos_ids = sii_native.extract_cargos(content)
            for cargo_id in discovered_cargos_ids:
                if cargo_id not in service.cargos:
                    display_name = cargo_id.replace("cargo.", "").replace("_", " ").title()
                    service.add_cargo(Cargo(cargo_id, display_name, 10))
            
            # 4. Atualizar UI
            update_city_dropdowns()
            all_cargos = sorted(service.cargos.values(), key=lambda x: x.name)
            cargo_dd.options = [ft.dropdown.Option(c.id, c.name) for c in all_cargos]
            
            profile_card.visible = False
            main_ui.visible = True
            
            status_msg = f"Mapa {'Brasileiro' if is_brazil_map else 'Europeu'} detectado! "
            status_msg += f"{len(discovered_cities_ids)} cidades carregadas."
            
            page.snack_bar = ft.SnackBar(ft.Text(f"✅ {status_msg}"), bgcolor=SUCCESS_COLOR)
            page.snack_bar.open = True
            page.update()
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {err}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()

    # --- UI Components ---
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

    show_all_cities_sw = ft.Switch(label="Somente descobertas", value=False, on_change=lambda _: update_city_dropdowns())
    source_city_dd = ft.Dropdown(label="Cidade de Origem", width=400, on_change=lambda e: update_comp_dd(e.data, source_comp_dd))
    source_comp_dd = ft.Dropdown(label="Empresa de Origem", width=400)
    dest_city_dd = ft.Dropdown(label="Cidade de Destino", width=400, on_change=lambda e: update_comp_dd(e.data, dest_comp_dd))
    dest_comp_dd = ft.Dropdown(label="Empresa de Destino", width=400)
    cargo_dd = ft.Dropdown(label="Carga", width=400)
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
        ft.ElevatedButton("GERAR E INJETAR CARGA NO SAVE", icon=ft.icons.ADD_TASK, bgcolor=SUCCESS_COLOR, color="white", height=70, width=940)
    ], visible=False, alignment=ft.MainAxisAlignment.CENTER)

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

    profiles = save_manager.list_profiles()
    profile_dd.options = [ft.dropdown.Option(p.id, p.name) for p in profiles]
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
