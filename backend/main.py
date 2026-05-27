from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/crear_agricultor")  # ✅ debe ser así

@app.get("/")
def saludar():
    return {"mensaje": "Hola API"}

@app.get ("/crear_agricultor")
def crear_agricultor():
    return "Cambiar esto por la funcionalidad" 
