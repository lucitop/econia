import json
import os
from city import Ciudad

SAVE_FILE = "saved_city.json"

def guardar_ciudad(ciudad):
    data = {
        "nombre": ciudad.nombre,
        "poblacion": ciudad.poblacion,
        "felicidad": ciudad.felicidad,
        "economia": ciudad.economia,
        "clase": ciudad.clase,
        "dia": ciudad.dia,
        "reservas": ciudad.reservas
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("\n✅ Ciudad guardada correctamente.\n")

def cargar_ciudad():
    if not os.path.exists(SAVE_FILE):
        print("❌ No hay partida guardada. Se iniciará una nueva.")
        return None
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    ciudad = Ciudad(nombre=data["nombre"], clase=data["clase"])
    ciudad.poblacion = data["poblacion"]
    ciudad.felicidad = data["felicidad"]
    ciudad.economia = data["economia"]
    ciudad.dia = data["dia"]
    ciudad.reservas = data["reservas"]
    print(f"\n✅ Ciudad cargada: {ciudad.nombre} (día {ciudad.dia})\n")
    return ciudad
