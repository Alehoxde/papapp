import json
import os
import sys

# Asegurar que la carpeta padre (backend) esté en sys.path para poder importar módulos locales
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '..')))

from database import SessionLocal
from models import (
    Agricultor, Recolector, Cotero, Transportador, Bodeguero,
    Comerciante, CompradorFinal, ConsumidorFinal,
    MinisterioAgricultura, Superintendencia
)

MODEL_MAP = {
    'agricultores': Agricultor,
    'recolectores': Recolector,
    'coteros': Cotero,
    'transportadores': Transportador,
    'bodegueros': Bodeguero,
    'comerciantes': Comerciante,
    'compradores_finales': CompradorFinal,
    'consumidores_finales': ConsumidorFinal,
    'ministerio_agricultura': MinisterioAgricultura,
    'superintendencias': Superintendencia,
}


def cargar_seed(ruta_json=None):
    if ruta_json is None:
        ruta_json = os.path.join(os.path.dirname(__file__), '..', 'seed_data.json')
        ruta_json = os.path.normpath(ruta_json)

    with open(ruta_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    db = SessionLocal()
    inserted = {k: 0 for k in MODEL_MAP.keys()}
    try:
        for key, items in data.items():
            Model = MODEL_MAP.get(key)
            if not Model:
                print(f"⚠️  Clave no reconocida en seed: {key}")
                continue
            for item in items:
                # Evitar duplicados por cedula si existe
                cedula = item.get('cedula')
                if cedula and db.query(Model).filter_by(cedula=cedula).first():
                    print(f"⚠️  Ya existe {key} con cédula {cedula}, se salta.")
                    continue
                obj = Model(**item)
                db.add(obj)
                inserted[key] += 1
        db.commit()
        print("✅ Seed cargado correctamente. Resumen:")
        for k, v in inserted.items():
            print(f"  - {k}: {v} registrados")
    except Exception as e:
        db.rollback()
        print(f"❌ Error al insertar seed: {e}")
    finally:
        db.close()


if __name__ == '__main__':
    ruta = os.path.join(os.path.dirname(__file__), '..', 'seed_data.json')
    ruta = os.path.normpath(ruta)
    if os.path.exists(ruta):
        cargar_seed(ruta)
    else:
        print(f"No se encontró el archivo seed en {ruta}")
