from app.services.cargo_service import CargoService
from app.models.cargo import City, Company, Cargo, Trailer, TrailerModel


def load_initial_data(service: CargoService):
    """Popula o serviço com dados iniciais do ETS2."""
    
    # Cidades e Empresas
    cities_data = [
        ("berlin", "Berlin", ["lkwlog", "itcc", "stokes"]),
        ("paris", "Paris", ["posped", "batisse", "euroacres"]),
        ("london", "London", ["itcc", "posped", "stokes"]),
        ("madrid", "Madrid", ["exol", "cortes", "transinet"]),
        ("warsaw", "Warsaw", ["posped", "lkwlog", "itcc"])
    ]
    
    companies_data = [
        ("lkwlog", "LKW Log"),
        ("itcc", "ITCC"),
        ("stokes", "Stokes"),
        ("posped", "Posped"),
        ("batisse", "Batisse"),
        ("euroacres", "EuroAcres"),
        ("exol", "Exol"),
        ("cortes", "Cortes"),
        ("transinet", "Transinet")
    ]
    
    cargos_data = [
        ("machinery", "Machinery", 15.0),
        ("electronics", "Electronics", 5.2),
        ("food", "Food & Beverages", 18.0),
        ("vehicles", "High-End Vehicles", 8.0),
        ("chemicals", "Chemicals", 22.0)
    ]

    trailers_data = [
        ("flatbed", "Flatbed"),
        ("curtainside", "Curtain Sider"),
        ("refrigerated", "Refrigerated"),
        ("lowboy", "Lowboy"),
        ("tanker", "Fuel Tanker")
    ]

    models_data = [
        ("scs_flatbed", "SCS Standard Flatbed"),
        ("scs_curtain", "SCS Standard Curtain"),
        ("kogel_cool", "Kögel Cool Expert"),
        ("schmitz_cargo", "Schmitz Cargobull"),
        ("krone_dry", "Krone Dry Liner")
    ]
    
    for c_id, name in companies_data:
        service.add_company(Company(id=c_id, name=name, city_id=""))

    for city_id, name, comps in cities_data:
        service.add_city(City(id=city_id, name=name, companies=comps))
        
    for cargo_id, name, weight in cargos_data:
        service.add_cargo(Cargo(id=cargo_id, name=name, weight=weight))

    for t_id, name in trailers_data:
        service.add_trailer(Trailer(id=t_id, name=name))

    for m_id, name in models_data:
        service.add_trailer_model(TrailerModel(id=m_id, name=name))
