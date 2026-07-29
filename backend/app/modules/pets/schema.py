from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class PetSpecies(str, Enum):
    dog = "dog"
    cat = "cat"
    bird = "bird"
    reptile = "reptile"
    other = "other"


class PetBase(BaseModel):
    name: str
    species: PetSpecies
    breed: Optional[str] = None
    birth_date: Optional[date] = None
    weight_kg: Optional[float] = None
    microchip_number: Optional[str] = None
    photo_url: Optional[str] = None


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[PetSpecies] = None
    breed: Optional[str] = None
    birth_date: Optional[date] = None
    weight_kg: Optional[float] = None
    microchip_number: Optional[str] = None
    photo_url: Optional[str] = None


class PetResponse(PetBase):
    id: UUID
    user_id: UUID
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)