from fastapi import FastAPI
from .modules.users.router import router as users_router

app = FastAPI(
    title="PetHealth API",
    description="API de PetHealth",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "PetHealth API funcionando correctamente"}