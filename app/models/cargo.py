from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Cargo:
    id: str
    name: str
    weight: float  # em toneladas


@dataclass
class Company:
    id: str
    name: str
    city_id: str
    exports: List[str] = None  # IDs das cargas que a empresa ENVIA
    imports: List[str] = None  # IDs das cargas que a empresa RECEBE


@dataclass
class City:
    id: str
    name: str
    companies: List[str]  # Lista de IDs de empresas


@dataclass
class Trailer:
    id: str
    name: str

@dataclass
class TrailerModel:
    id: str
    name: str

@dataclass
class CargoJob:
    source_city: str
    source_company: str
    dest_city: str
    dest_company: str
    cargo: str
    trailer: str
    trailer_model: str
    urgency: int  # 0, 1, 2
    unique_code: str  # 8 letras aleatórias
    distance_km: Optional[int] = None
