import json
import os
from database import SessionLocal
from models import Agricultor

def insertar_agricultores_desde_json(ruta_json):
    """Inserta los agricultores listados en un archivo JSON."""
    with open(ruta_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Si el JSON tiene una lista directa o un objeto con clave 'agricultores'
    if isinstance(data, list):
        agricultores = data
    elif isinstance(data, dict) and 'agricultores' in data:
        agricultores = data['agricultores']
    else:
        raise ValueError("El JSON debe ser una lista de objetos o tener una clave 'agricultores'")
    
    db = SessionLocal()
    try:
        for item in agricultores:
            # Validar campos mínimos
            if 'cedula' not in item or 'nombre' not in item:
                print(f"⚠️  Saltando registro sin cédula o nombre: {item}")
                continue
            agricultor = Agricultor(
                cedula=item['cedula'],
                nombre=item['nombre'],
                area=item.get('area'),
                cultivo=item.get('cultivo'),
                inversion=item.get('inversion'),
                fecha=item.get('fecha'),
                ubicacion_cultivo=item.get('ubicacion_cultivo')
            )
            db.add(agricultor)
        db.commit()
        print(f"✅ {len(agricultores)} agricultores insertados correctamente.")
    except Exception as e:
        db.rollback()
        print(f"❌ Error al insertar: {e}")
    finally:
        db.close()

def insertar_datos_ejemplo():
    """Inserta datos de muestra si no se encuentra un archivo JSON."""
    ejemplo = [
        {
            "cedula": "1002345678",
            "nombre": "Pedro López",
            "area": "8 ha",
            "cultivo": "Papa Suprema",
            "inversion": 7500.0,
            "fecha": "2024-03-10",
            "ubicacion_cultivo": "POLYGON((-74.1 4.6, -74.0 4.6, -74.0 4.7, -74.1 4.7, -74.1 4.6))"
        },
        {
            "cedula": "1009876543",
            "nombre": "Luisa Fernández",
            "area": "4.2 ha",
            "cultivo": "Papa R12",
            "inversion": 4800.0,
            "fecha": "2024-02-05",
            "ubicacion_cultivo": "POLYGON((-74.2 4.55, -74.1 4.55, -74.1 4.65, -74.2 4.65, -74.2 4.55))"
        }
    ]
    db = SessionLocal()
    try:
        for data in ejemplo:
            agricultor = Agricultor(**data)
            db.add(agricultor)
        db.commit()
        print("✅ Datos de ejemplo insertados correctamente.")
    except Exception as e:
        db.rollback()
        print(f"❌ Error al insertar ejemplo: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    json_file = "../backend/demo.json"   # Cambia por tu archivo si es otro nombre
    if os.path.exists(json_file):
        insertar_agricultores_desde_json(json_file)
    else:
        print(f"No se encontró '{json_file}'. Insertando datos de ejemplo.")
        insertar_datos_ejemplo()