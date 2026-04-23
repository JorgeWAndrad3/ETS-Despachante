import pytest
from app.services.cargo_service import CargoService
from app.models.cargo import City, Company, Cargo


@pytest.fixture
def service():
    s = CargoService()
    # Setup de dados iniciais
    s.add_city(City(id="berlin", name="Berlin", companies=["lkwlog", "itcc"]))
    s.add_city(City(id="paris", name="Paris", companies=["posped", "batisse"]))
    
    s.add_company(Company(id="lkwlog", name="LKW Log", city_id="berlin"))
    s.add_company(Company(id="itcc", name="ITCC", city_id="berlin"))
    s.add_company(Company(id="posped", name="Posped", city_id="paris"))
    
    s.add_cargo(Cargo(id="machinery", name="Machinery", weight=12.5))
    return s


def test_get_companies_by_city(service):
    companies = service.get_companies_by_city("berlin")
    assert len(companies) == 2
    assert any(c.id == "lkwlog" for c in companies)


def test_create_job_success(service):
    job = service.create_job(
        source_city_id="berlin",
        source_company_id="lkwlog",
        dest_city_id="paris",
        dest_company_id="posped",
        cargo_id="machinery"
    )
    assert job.source_city == "Berlin"
    assert job.dest_city == "Paris"
    assert job.cargo == "Machinery"


def test_create_job_same_city_error(service):
    with pytest.raises(ValueError, match="Origem e destino não podem ser iguais."):
        service.create_job(
            source_city_id="berlin",
            source_company_id="lkwlog",
            dest_city_id="berlin",
            dest_company_id="itcc",
            cargo_id="machinery"
        )


def test_create_job_invalid_data_error(service):
    with pytest.raises(ValueError, match="Cidade ou carga inválida."):
        service.create_job(
            source_city_id="london", # Inexistente
            source_company_id="lkwlog",
            dest_city_id="paris",
            dest_company_id="posped",
            cargo_id="machinery"
        )


def test_add_entities(service):
    service.add_city(City(id="lisbon", name="Lisbon", companies=[]))
    assert "lisbon" in service.cities
    
    service.add_company(Company(id="og", name="OG", city_id="lisbon"))
    assert "og" in service.companies
    
    service.add_cargo(Cargo(id="wood", name="Wood", weight=10.0))
    assert "wood" in service.cargos
