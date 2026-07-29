from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...config.database import get_db
from . import crud
from .schema import UserCreate, UserLogin, UserResponse, Token

router = APIRouter(tags=["Users"])

# 1. Endpoint de registro
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    user = crud.register(db=db, user_data=user_data)

    if user == "USER_ALREADY_EXISTS":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado"
        )
    return user

# 2. Endpoint de login
@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    # Verificar si las credenciales son válidas
    user = crud.login(db=db, credentials=credentials)
    if user == "UNAUTHORIZED":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas (email o contraseña inválidos).",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user