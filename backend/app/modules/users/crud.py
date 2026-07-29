from sqlalchemy.orm import Session
from .security import create_access_token, hash_password, verify_password
from .model import User
from .schema import UserCreate, UserLogin


def register(db: Session, user_data: UserCreate):
    # 1. Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return "USER_ALREADY_EXISTS"
    
    # Hashear la contraseña
    hashed_pwd = hash_password(user_data.password)

    # Crear al nuevo usuario
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_pwd,
        role=user_data.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(db: Session, credentials: UserLogin):
    # Buscar el usuario por el email
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        return "UNAUTHORIZED"
    
    # Generar el token JWT con el email como identificador (sub)
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}