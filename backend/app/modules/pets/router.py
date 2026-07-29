from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from sqlalchemy.orm import Session

from ...config.database import get_db
from ...config.config import settings
from ..users.model import User
from . import crud
from .schema import PetCreate, PetUpdate, PetResponse

router = APIRouter(prefix="/pets", tags=["Pets"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        print(f"DEBUG - Email extraído del token: {email}")
        if email is None:
            print("DEBUG - El token no contiene 'sub' (email)")
            raise credentials_exception
    except ExpiredSignatureError:
        print("DEBUG - El token ha expirado.")
        raise credentials_exception
    except JWTError as e:
        print(f"DEBUG - Error de JWT (firma inválida, malformado, etc.): {e}")
        raise credentials_exception
    except Exception as e:
        print(f"DEBUG - Error inesperado: {e}")
        raise credentials_exception
    
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        print(f"DEBUG - No se encontró ningún usuario en la BD con el email: {email}")
        raise credentials_exception
        
    return user


@router.post("/", response_model=PetResponse, status_code=status.HTTP_201_CREATED)
def create_pet(
    pet_data: PetCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_pet(db=db, pet_data=pet_data, user_id=current_user.id)


@router.get("/", response_model=List[PetResponse])
def list_pets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_pets_by_user(db=db, user_id=current_user.id)


@router.get("/{pet_id}", response_model=PetResponse)
def get_pet(
    pet_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pet = crud.get_pet_by_id(db=db, pet_id=pet_id, user_id=current_user.id)
    if not pet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mascota no encontrada"
        )
    return pet


@router.put("/{pet_id}", response_model=PetResponse)
def update_pet(
    pet_id: UUID,
    pet_data: PetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_pet = crud.update_pet(db=db, pet_id=pet_id, user_id=current_user.id, pet_data=pet_data)
    if not updated_pet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mascota no encontrada para actualizar"
        )
    return updated_pet


@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet(
    pet_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted_pet = crud.delete_pet(db=db, pet_id=pet_id, user_id=current_user.id)
    if not deleted_pet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mascota no encontrada para eliminar"
        )
    return None