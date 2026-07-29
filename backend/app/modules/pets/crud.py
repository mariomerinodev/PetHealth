from sqlalchemy.orm import Session
from uuid import UUID
from .model import Pet
from .schema import PetCreate, PetUpdate


def create_pet(db: Session, pet_data: PetCreate, user_id: UUID):
    db_pet = Pet(
        **pet_data.model_dump(),
        user_id=user_id
    )
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def get_pets_by_user(db: Session, user_id: UUID):
    return db.query(Pet).filter(Pet.user_id == user_id).all()


def get_pet_by_id(db: Session, pet_id: UUID, user_id: UUID):
    return db.query(Pet).filter(Pet.id == pet_id, Pet.user_id == user_id).first()


def update_pet(db: Session, pet_id: UUID, user_id: UUID, pet_data: PetUpdate):
    db_pet = get_pet_by_id(db, pet_id=pet_id, user_id=user_id)
    if not db_pet:
        return None
    
    update_data = pet_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pet, key, value)
        
    db.commit()
    db.refresh(db_pet)
    return db_pet


def delete_pet(db: Session, pet_id: UUID, user_id: UUID):
    db_pet = get_pet_by_id(db, pet_id=pet_id, user_id=user_id)
    if not db_pet:
        return None
        
    db.delete(db_pet)
    db.commit()
    return db_pet