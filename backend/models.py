from sqlalchemy import Column, Integer, String, Float
from database import Base

# Tabla: agricultores (exactamente según demo.json)
class Agricultor(Base):
    __tablename__ = "agricultores"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    area = Column(String, nullable=True)               # Área de papa lista para cosechar
    cultivo = Column(String, nullable=True)            # Variedad de papa cultivada
    inversion = Column(Float, nullable=True)           # Dinero invertido en dólares
    fecha = Column(String, nullable=True)              # Fecha inicial de siembra
    ubicacion_cultivo = Column(String, nullable=True)  # Polígono georeferenciado

# El resto de actores (mantenemos los mismos campos que antes)
class Recolector(Base):
    __tablename__ = "recolectores"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    zona_asignada = Column(String, nullable=True)
    jornada = Column(String, nullable=True)

class Cotero(Base):
    __tablename__ = "coteros"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    medio_transporte = Column(String, nullable=True)
    capacidad = Column(String, nullable=True)

class Transportador(Base):
    __tablename__ = "transportadores"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    vehiculo_placa = Column(String, nullable=True)
    ruta_asignada = Column(String, nullable=True)

class Bodeguero(Base):
    __tablename__ = "bodegueros"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    nombre_bodega = Column(String, nullable=True)
    capacidad_almacenamiento = Column(Float, nullable=True)

class Comerciante(Base):
    __tablename__ = "comerciantes"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    volumen_compra = Column(String, nullable=True)
    direccion_comercial = Column(String, nullable=True)

class CompradorFinal(Base):
    __tablename__ = "compradores_finales"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    cantidad_comprada = Column(String, nullable=True)
    punto_venta = Column(String, nullable=True)

class ConsumidorFinal(Base):
    __tablename__ = "consumidores_finales"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    preferencias = Column(String, nullable=True)
    frecuencia_compra = Column(String, nullable=True)

class MinisterioAgricultura(Base):
    __tablename__ = "ministerio_agricultura"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    region_regulada = Column(String, nullable=True)
    precio_referencia = Column(Float, nullable=True)

class Superintendencia(Base):
    __tablename__ = "superintendencias"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    sector_regulado = Column(String, nullable=True)
    ultima_inspeccion = Column(String, nullable=True)