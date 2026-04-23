from typing import List, Dict
from app.models.cargo import Cargo, City, Company, CargoJob, Trailer, TrailerModel
from app.utils.helpers import generate_unique_job_code
import random

class CargoService:
    def __init__(self):
        self.cities: Dict[str, City] = {}
        self.companies: Dict[str, Company] = {}
        self.cargos: Dict[str, Cargo] = {}
        self.trailers: Dict[str, Trailer] = {}
        self.trailer_models: Dict[str, TrailerModel] = {}

    def add_city(self, city: City) -> None:
        self.cities[city.id] = city

    def add_company(self, company: Company) -> None:
        self.companies[company.id] = company

    def add_cargo(self, cargo: Cargo) -> None:
        self.cargos[cargo.id] = cargo
    
    def add_trailer(self, trailer: Trailer) -> None:
        self.trailers[trailer.id] = trailer
    
    def add_trailer_model(self, model: TrailerModel) -> None:
        self.trailer_models[model.id] = model

    def get_random_city_id(self) -> str:
        return random.choice(list(self.cities.keys())) if self.cities else ""

    def get_companies_by_city(self, city_id: str) -> List[Company]:
        """Retorna as empresas presentes em uma determinada cidade."""
        if city_id not in self.cities:
            return []
        
        city_companies_ids = self.cities[city_id].companies
        return [self.companies[cid] for cid in city_companies_ids if cid in self.companies]

    def create_job(
        self, 
        source_city_id: str, 
        source_company_id: str, 
        dest_city_id: str, 
        dest_company_id: str, 
        cargo_id: str,
        trailer_id: str,
        trailer_model_id: str,
        urgency: int
    ) -> CargoJob:
        """Valida e cria uma nova carga com código único."""
        if not all([
            source_city_id in self.cities,
            dest_city_id in self.cities,
            cargo_id in self.cargos,
            trailer_id in self.trailers,
            trailer_model_id in self.trailer_models
        ]):
            raise ValueError("Dados incompletos ou inválidos.")

        if source_city_id == dest_city_id:
            raise ValueError("Origem e destino não podem ser iguais.")

        return CargoJob(
            source_city=self.cities[source_city_id].name,
            source_company=source_company_id,
            dest_city=self.cities[dest_city_id].name,
            dest_company=dest_company_id,
            cargo=self.cargos[cargo_id].name,
            trailer=self.trailers[trailer_id].name,
            trailer_model=self.trailer_models[trailer_model_id].name,
            urgency=urgency,
            unique_code=generate_unique_job_code()
        )
