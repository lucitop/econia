import json
import os

SAVE_FOLDER = "saves"

def save_game(city, advisor, filename="partida_1.json"):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    data = {
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

    with open(f"{SAVE_FOLDER}/{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"\n✔ Partida guardada como {filename}")

def load_game(city, advisor, filename="partida_1.json"):
    try:
        with open(f"{SAVE_FOLDER}/{filename}", "r", encoding="utf-8") as f:
            data = json.load(f)

        city.poblacion = data["poblacion"]
        city.dinero = data["dinero"]
        city.felicidad = data["felicidad"]
        city.salud = data["salud"]
        city.empleo = data["empleo"]
        city.reservas = data["reservas"]
        city.dia = data["dia"]
        city.historial = data["historial"]
        advisor.last_used_turn = data["advisor_last_used"]

        print(f"\n✔ Partida cargada correctamente desde {filename}")
    except FileNotFoundError:
        print(f"\n✘ No se encontró el archivo {filename}. Asegurate de haber guardado una partida antes.")
