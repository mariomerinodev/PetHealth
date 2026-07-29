from fastapi import FastAPI
from .modules.users.router import router as users_router
from .modules.pets.router import router as pets_router

from app.modules.users.model import User
from app.modules.pets.model import Pet

app = FastAPI(
    title="PetHealth API",
    description="API de PetHealth",
    version="1.0.0"
)

# Routers
app.include_router(users_router)
app.include_router(pets_router)

@app.get("/")
def root():
    return {"message": "PetHealth API funcionando correctamente"}