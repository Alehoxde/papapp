from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from database import engine, get_db, Base
from models import (
    Agricultor, Recolector, Cotero, Transportador, Bodeguero,
    Comerciante, CompradorFinal, ConsumidorFinal,
    MinisterioAgricultura, Superintendencia
)

# Crear todas las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cadena de Papa API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ESQUEMAS PYDANTIC (validación) ----------
# Agricultor (basado en JSON)
class AgricultorBase(BaseModel):
    cedula: str
    nombre: str
    area: Optional[str] = None
    cultivo: Optional[str] = None
    inversion: Optional[float] = None
    fecha: Optional[str] = None
    ubicacion_cultivo: Optional[str] = None

class AgricultorOut(AgricultorBase):
    id: int
    class Config: from_attributes = True

# Recolector
class RecolectorBase(BaseModel):
    cedula: str; nombre: str
    zona_asignada: Optional[str] = None
    jornada: Optional[str] = None
class RecolectorOut(RecolectorBase):
    id: int
    class Config: from_attributes = True

# Cotero
class CoteroBase(BaseModel):
    cedula: str; nombre: str
    medio_transporte: Optional[str] = None
    capacidad: Optional[str] = None
class CoteroOut(CoteroBase):
    id: int
    class Config: from_attributes = True

# Transportador
class TransportadorBase(BaseModel):
    cedula: str; nombre: str
    vehiculo_placa: Optional[str] = None
    ruta_asignada: Optional[str] = None
class TransportadorOut(TransportadorBase):
    id: int
    class Config: from_attributes = True

# Bodeguero
class BodegueroBase(BaseModel):
    cedula: str; nombre: str
    nombre_bodega: Optional[str] = None
    capacidad_almacenamiento: Optional[float] = None
class BodegueroOut(BodegueroBase):
    id: int
    class Config: from_attributes = True

# Comerciante
class ComercianteBase(BaseModel):
    cedula: str; nombre: str
    volumen_compra: Optional[str] = None
    direccion_comercial: Optional[str] = None
class ComercianteOut(ComercianteBase):
    id: int
    class Config: from_attributes = True

# CompradorFinal
class CompradorFinalBase(BaseModel):
    cedula: str; nombre: str
    cantidad_comprada: Optional[str] = None
    punto_venta: Optional[str] = None
class CompradorFinalOut(CompradorFinalBase):
    id: int
    class Config: from_attributes = True

# ConsumidorFinal
class ConsumidorFinalBase(BaseModel):
    cedula: str; nombre: str
    preferencias: Optional[str] = None
    frecuencia_compra: Optional[str] = None
class ConsumidorFinalOut(ConsumidorFinalBase):
    id: int
    class Config: from_attributes = True

# MinisterioAgricultura
class MinisterioBase(BaseModel):
    cedula: str; nombre: str
    region_regulada: Optional[str] = None
    precio_referencia: Optional[float] = None
class MinisterioOut(MinisterioBase):
    id: int
    class Config: from_attributes = True

# Superintendencia
class SuperintendenciaBase(BaseModel):
    cedula: str; nombre: str
    sector_regulado: Optional[str] = None
    ultima_inspeccion: Optional[str] = None
class SuperintendenciaOut(SuperintendenciaBase):
    id: int
    class Config: from_attributes = True

# ---------- CRUD ENDPOINTS PARA CADA ACTOR ----------
# AGRICULTOR
@app.post("/agricultores", response_model=AgricultorOut, status_code=201)
def crear_agricultor(agri: AgricultorBase, db: Session = Depends(get_db)):
    db_agri = Agricultor(**agri.dict())
    db.add(db_agri)
    db.commit()
    db.refresh(db_agri)
    return db_agri

@app.get("/agricultores", response_model=List[AgricultorOut])
def listar_agricultores(db: Session = Depends(get_db)):
    return db.query(Agricultor).all()

# RECOLECTOR
@app.post("/recolectores", response_model=RecolectorOut, status_code=201)
def crear_recolector(data: RecolectorBase, db: Session = Depends(get_db)):
    obj = Recolector(**data.dict())
    db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/recolectores", response_model=List[RecolectorOut])
def listar_recolectores(db: Session = Depends(get_db)):
    return db.query(Recolector).all()

# COTERO
@app.post("/coteros", response_model=CoteroOut, status_code=201)
def crear_cotero(data: CoteroBase, db: Session = Depends(get_db)):
    obj = Cotero(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/coteros", response_model=List[CoteroOut])
def listar_coteros(db: Session = Depends(get_db)):
    return db.query(Cotero).all()

# TRANSPORTADOR
@app.post("/transportadores", response_model=TransportadorOut, status_code=201)
def crear_transportador(data: TransportadorBase, db: Session = Depends(get_db)):
    obj = Transportador(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/transportadores", response_model=List[TransportadorOut])
def listar_transportadores(db: Session = Depends(get_db)):
    return db.query(Transportador).all()

# BODEGUERO
@app.post("/bodegueros", response_model=BodegueroOut, status_code=201)
def crear_bodeguero(data: BodegueroBase, db: Session = Depends(get_db)):
    obj = Bodeguero(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/bodegueros", response_model=List[BodegueroOut])
def listar_bodegueros(db: Session = Depends(get_db)):
    return db.query(Bodeguero).all()

# COMERCIANTE
@app.post("/comerciantes", response_model=ComercianteOut, status_code=201)
def crear_comerciante(data: ComercianteBase, db: Session = Depends(get_db)):
    obj = Comerciante(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/comerciantes", response_model=List[ComercianteOut])
def listar_comerciantes(db: Session = Depends(get_db)):
    return db.query(Comerciante).all()

# COMPRADOR FINAL
@app.post("/compradores_finales", response_model=CompradorFinalOut, status_code=201)
def crear_comprador_final(data: CompradorFinalBase, db: Session = Depends(get_db)):
    obj = CompradorFinal(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/compradores_finales", response_model=List[CompradorFinalOut])
def listar_compradores_finales(db: Session = Depends(get_db)):
    return db.query(CompradorFinal).all()

# CONSUMIDOR FINAL
@app.post("/consumidores_finales", response_model=ConsumidorFinalOut, status_code=201)
def crear_consumidor_final(data: ConsumidorFinalBase, db: Session = Depends(get_db)):
    obj = ConsumidorFinal(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/consumidores_finales", response_model=List[ConsumidorFinalOut])
def listar_consumidores_finales(db: Session = Depends(get_db)):
    return db.query(ConsumidorFinal).all()

# MINISTERIO DE AGRICULTURA
@app.post("/ministerio_agricultura", response_model=MinisterioOut, status_code=201)
def crear_ministerio(data: MinisterioBase, db: Session = Depends(get_db)):
    obj = MinisterioAgricultura(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/ministerio_agricultura", response_model=List[MinisterioOut])
def listar_ministerio(db: Session = Depends(get_db)):
    return db.query(MinisterioAgricultura).all()

# SUPERINTENDENCIA
@app.post("/superintendencias", response_model=SuperintendenciaOut, status_code=201)
def crear_superintendencia(data: SuperintendenciaBase, db: Session = Depends(get_db)):
    obj = Superintendencia(**data.dict()); db.add(obj); db.commit(); db.refresh(obj); return obj
@app.get("/superintendencias", response_model=List[SuperintendenciaOut])
def listar_superintendencias(db: Session = Depends(get_db)):
    return db.query(Superintendencia).all()

#---------- FRONTEND HTML ----------
@app.get("/", response_class=HTMLResponse)
def frontend():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cadena de Papa - Gestión de Actores</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #2c3e50; }
            select, button { padding: 8px; margin: 5px; font-size: 1em; }
            table { border-collapse: collapse; width: 100%; margin-top: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .form-container { margin-top: 30px; background: #f9f9f9; padding: 15px; border-radius: 8px; }
            input { display: block; margin: 8px 0; padding: 6px; width: 300px; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>🌱 Gestión de la Cadena de Papa</h1>
        <label>Seleccionar actor: </label>
        <select id="rolSelect">
            <option value="agricultores">Agricultor</option>
            <option value="recolectores">Recolector</option>
            <option value="coteros">Cotero</option>
            <option value="transportadores">Transportador</option>
            <option value="bodegueros">Bodeguero</option>
            <option value="comerciantes">Comerciante</option>
            <option value="compradores_finales">Comprador Final</option>
            <option value="consumidores_finales">Consumidor Final</option>
            <option value="ministerio_agricultura">Ministerio de Agricultura</option>
            <option value="superintendencias">Superintendencia</option>
        </select>
        <button onclick="cargarLista()">Mostrar registros</button>
        <div id="lista"></div>

        <div class="form-container">
            <h3>Crear nuevo registro</h3>
            <div id="formulario"></div>
            <button onclick="crearRegistro()">Guardar</button>
            <div id="mensaje" class="error"></div>
        </div>

        <script>
            let endpointActual = "agricultores";
            const camposPorRol = {
                agricultores: ["cedula", "nombre", "area", "cultivo", "inversion", "fecha", "ubicacion_cultivo"],
                recolectores: ["cedula", "nombre", "zona_asignada", "jornada"],
                coteros: ["cedula", "nombre", "medio_transporte", "capacidad"],
                transportadores: ["cedula", "nombre", "vehiculo_placa", "ruta_asignada"],
                bodegueros: ["cedula", "nombre", "nombre_bodega", "capacidad_almacenamiento"],
                comerciantes: ["cedula", "nombre", "volumen_compra", "direccion_comercial"],
                compradores_finales: ["cedula", "nombre", "cantidad_comprada", "punto_venta"],
                consumidores_finales: ["cedula", "nombre", "preferencias", "frecuencia_compra"],
                ministerio_agricultura: ["cedula", "nombre", "region_regulada", "precio_referencia"],
                superintendencias: ["cedula", "nombre", "sector_regulado", "ultima_inspeccion"]
            };

            document.getElementById("rolSelect").addEventListener("change", (e) => {
                endpointActual = e.target.value;
                generarFormulario(endpointActual);
                cargarLista();
            });

            function generarFormulario(rol) {
                const campos = camposPorRol[rol];
                let html = "";
                campos.forEach(campo => {
                    let tipo = "text";
                    if (campo === "inversion" || campo === "precio_referencia" || campo === "capacidad_almacenamiento") tipo = "number";
                    html += `<label>${campo.replace("_"," ")}: </label><input type="${tipo}" id="${campo}" placeholder="${campo}"><br>`;
                });
                document.getElementById("formulario").innerHTML = html;
            }

            async function cargarLista() {
                try {
                    const res = await fetch(`/${endpointActual}`);
                    if (!res.ok) throw new Error("Error al cargar");
                    const data = await res.json();
                    const campos = camposPorRol[endpointActual];
                    let tabla = "<table><tr>" + campos.map(c => `<th>${c}</th>`).join("") + "</tr>";
                    data.forEach(item => {
                        tabla += "<tr>";
                        campos.forEach(campo => {
                            let valor = item[campo] !== undefined ? item[campo] : "";
                            tabla += `<td>${valor}</td>`;
                        });
                        tabla += "</tr>";
                    });
                    tabla += "</table>";
                    document.getElementById("lista").innerHTML = tabla || "<p>No hay registros</p>";
                } catch (err) {
                    document.getElementById("lista").innerHTML = `<p class="error">Error: ${err.message}</p>`;
                }
            }

            async function crearRegistro() {
                const campos = camposPorRol[endpointActual];
                const nuevo = {};
                for (let campo of campos) {
                    let val = document.getElementById(campo).value;
                    if (campo === "inversion" || campo === "precio_referencia" || campo === "capacidad_almacenamiento") {
                        val = val === "" ? null : parseFloat(val);
                    } else {
                        val = val === "" ? null : val;
                    }
                    nuevo[campo] = val;
                }
                try {
                    const res = await fetch(`/${endpointActual}`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(nuevo)
                    });
                    if (!res.ok) {
                        const error = await res.json();
                        throw new Error(error.detail || "Error al crear");
                    }
                    document.getElementById("mensaje").innerHTML = "✅ Creado exitosamente";
                    setTimeout(() => document.getElementById("mensaje").innerHTML = "", 3000);
                    cargarLista();
                    campos.forEach(campo => document.getElementById(campo).value = "");
                } catch (err) {
                    document.getElementById("mensaje").innerHTML = `❌ ${err.message}`;
                }
            }

            generarFormulario("agricultores");
            cargarLista();
        </script>
    </body>
    </html>
    """