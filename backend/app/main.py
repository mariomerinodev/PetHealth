from fastapi import FastAPI

app = FastAPI(
    title="PetHealth API",
    description="API de PetHealth",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "PetHealth API funcionando correctamente"}