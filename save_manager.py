import json
import os
from city import Ciudad

SAVE_FOLDER = "saves"

def generar_nombre_archivo(nombre_ciudad):
    base = nombre_ciudad.strip().replace(" ", "_")
    nombre = base + ".json"
    contador = 1
    while os.path.exists(os.path.join(SAVE_FOLDER, nombre)):
        nombre = f"{base}_{contador}.json"
        contador += 1
    return nombre

def save_game(city, advisor):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    filename = generar_nombre_archivo(city.nombre)

    data = {
        "nombre": city.nombre,
        "clase": city.clase,
        "poblacion": city.poblacion,
        "dinero": city.dinero,
        "felicidad": city.felicidad,
        "salud": city.salud,
        "empleo": city.empleo,
        "reservas": city.reservas,
        "dia": city.dia,
        "historial": city.historial,
        "advisor_last_used": advisor.last_used_turn
    }

    with open(os.path.join(SAVE_FOLDER, filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"\n✔ Partida guardada como {filename}")

def load_game(_, advisor):
    if not os.path.exists(SAVE_FOLDER):
        print("No hay partidas guardadas.")
        return None

    archivos = [f for f in os.listdir(SAVE_FOLDER) if f.endswith(".json")]

    if not archivos:
        print("No hay archivos de guardado disponibles.")
        return None

    print("\n📂 Partidas disponibles:")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")

    while True:
        try:
            eleccion = int(input("Elegí una partida para cargar (número): "))
            if 1 <= eleccion <= len(archivos):
                break
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingresá un número.")

    filename = archivos[eleccion - 1]
    filepath = os.path.join(SAVE_FOLDER, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        ciudad = Ciudad(nombre=data["nombre"], clase=data["clase"])
        ciudad.poblacion = data["poblacion"]
        ciudad.dinero = data["dinero"]
        ciudad.felicidad = data["felicidad"]
        ciudad.salud = data["salud"]
        ciudad.empleo = data["empleo"]
        ciudad.reservas = data["reservas"]
        ciudad.dia = data["dia"]
        ciudad.historial = data["historial"]
        advisor.last_used_turn = data["advisor_last_used"]

        print(f"\n✔ Partida cargada desde {filename}")
        return ciudad

    except Exception as e:
        print(f"Error al cargar la partida: {e}")
        return None
