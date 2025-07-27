import random
from colorama import Fore, Style


class Event:
    def __init__(self, name, description, effects):
        self.name = name
        self.description = description
        self.effects = effects  # dict: {'variable': valor}

    def apply(self, city):
        city.aplicar_efectos(self.effects, f"Evento: {self.name}")

        texto = (
            f"{Fore.RED + Style.BRIGHT}╔══════════════════════════════╗\n"
            f"║     ¡EVENTO ALEATORIO!      ║\n"
            f"╚══════════════════════════════╝\n"
            f"{Fore.YELLOW + Style.BRIGHT}{self.name}: {Style.NORMAL}{self.description}\n"
            f"{Fore.CYAN}Impacto en la ciudad:"
        )
        for var, val in self.effects.items():
            signo = "+" if val >= 0 else ""
            texto += f"\n - {var}: {signo}{val}"

        return texto

def get_random_event():
    eventos = [
        Event(
            "Pandemia",
            "Un brote infeccioso afecta a la población.",
            {"salud": -15, "empleo": -10, "felicidad": -5}
        ),
        Event(
            "Bonanza exportadora",
            "El país logra vender productos a gran escala en el exterior.",
            {"dinero": +30, "reservas": +20, "felicidad": +5}
        ),
        Event(
            "Crisis financiera",
            "El sistema bancario entra en pánico.",
            {"dinero": -25, "empleo": -15, "felicidad": -10}
        ),
        Event(
            "Inflación creciente",
            "Los precios aumentan rápidamente, erosionando el poder de compra.",
            {"dinero": -20, "felicidad": -5, "reservas": -10}
        ),
        Event(
            "Ayuda internacional",
            "Organismos multilaterales otorgan financiamiento de emergencia.",
            {"dinero": +40, "reservas": +30}
        )
    ]

    probabilidad_evento = 0.25
    if random.random() < probabilidad_evento:
        return random.choice(eventos)
    else:
        return None

class EventoInteractivo:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones

    def mostrar_y_resolver(self, ciudad):
        print("\n🌐 Evento interactivo:")
        print(Fore.YELLOW + Style.BRIGHT + self.descripcion + Style.RESET_ALL)
        print()

        opciones_validas = []

        for i, opcion in enumerate(self.opciones, 1):
            clases_restringidas = opcion.get("clases_restringidas", [])
            if ciudad.clase in clases_restringidas:
                continue
            print(f"{Fore.CYAN}{i}. {Fore.WHITE}{opcion['texto']}")
            opciones_validas.append(opcion)

        if not opciones_validas:
            print("Tu ciudad no tiene opciones viables para este evento.")
            return "Sin acción posible."

        while True:
            try:
                eleccion = int(input(Fore.GREEN + "Elegí una opción: "))
                if 1 <= eleccion <= len(opciones_validas):
                    break
            except ValueError:
                pass
            print("Opción inválida.")

        seleccion = opciones_validas[eleccion - 1]
        efectos = seleccion["efectos"]
        ciudad.aplicar_efectos(efectos, seleccion.get("etiqueta", "Evento interactivo"))
        return f"✔ Decisión tomada: {seleccion['texto']}"

def get_random_interactive_event():
    eventos = [
        EventoInteractivo(
            descripcion="Un grupo minoritario protesta por la falta de representación política.",
            opciones=[
                {
                    "texto": "Reprimir la protesta con fuerza.",
                    "efectos": {"felicidad": -10, "dinero": +5},
                    "clases_restringidas": ["Diplomática", "Colectivista"],
                    "etiqueta": "Represión"
                },
                {
                    "texto": "Abrir diálogo con los líderes.",
                    "efectos": {"felicidad": +8, "dinero": -5},
                    "etiqueta": "Negociación"
                },
                {
                    "texto": "Ignorar el conflicto.",
                    "efectos": {},
                    "etiqueta": "Inacción"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Una sequía ha reducido la producción de alimentos.",
            opciones=[
                {
                    "texto": "Importar alimentos urgentemente.",
                    "efectos": {"dinero": -20, "felicidad": +5},
                    "etiqueta": "Importación de emergencia"
                },
                {
                    "texto": "Distribuir las reservas internas.",
                    "efectos": {"reservas": -15, "felicidad": +3},
                    "clases_restringidas": ["Liberal"],
                    "etiqueta": "Distribución estatal"
                },
                {
                    "texto": "No intervenir. El mercado se ajustará solo.",
                    "efectos": {"salud": -10},
                    "clases_restringidas": ["Colectivista"],
                    "etiqueta": "Dejar actuar al mercado"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Se descubre un escándalo de corrupción en altos funcionarios.",
            opciones=[
                {
                    "texto": "Investigar públicamente y castigar.",
                    "efectos": {"dinero": -10, "felicidad": +7},
                    "etiqueta": "Justicia ejemplar"
                },
                {
                    "texto": "Encubrir para evitar escándalo.",
                    "efectos": {"felicidad": -5},
                    "clases_restringidas": ["Tradicionalista", "Diplomática"],
                    "etiqueta": "Encubrimiento"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Se descubre una nueva tecnología agrícola muy eficiente.",
            opciones=[
                {
                    "texto": "Invertir y adoptarla masivamente.",
                    "efectos": {"dinero": -30, "empleo": +10},
                    "clases_restringidas": ["Tradicionalista"],
                    "etiqueta": "Adopción tecnológica"
                },
                {
                    "texto": "Esperar a ver resultados en otras ciudades.",
                    "efectos": {},
                    "etiqueta": "Cautela"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Una ciudad vecina moviliza tropas cerca de tu frontera.",
            opciones=[
                {
                    "texto": "Responder con despliegue militar.",
                    "efectos": {"dinero": -15, "felicidad": +2},
                    "clases_restringidas": ["Diplomática", "Colectivista"],
                    "etiqueta": "Respuesta militar"
                },
                {
                    "texto": "Iniciar negociaciones inmediatas.",
                    "efectos": {"dinero": -10},
                    "etiqueta": "Negociación diplomática"
                },
                {
                    "texto": "Ignorar y esperar.",
                    "efectos": {"felicidad": -3},
                    "etiqueta": "Pasividad"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Una huelga paraliza sectores clave de la ciudad.",
            opciones=[
                {
                    "texto": "Reprimir y forzar el regreso al trabajo.",
                    "efectos": {"empleo": +5, "felicidad": -10},
                    "clases_restringidas": ["Colectivista", "Diplomática"],
                    "etiqueta": "Fuerza contra huelga"
                },
                {
                    "texto": "Negociar con los sindicatos.",
                    "efectos": {"dinero": -10, "felicidad": +5},
                    "etiqueta": "Acuerdo laboral"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Una ola turística repentina genera oportunidades económicas.",
            opciones=[
                {
                    "texto": "Promover el turismo y flexibilizar regulaciones.",
                    "efectos": {"dinero": +25, "empleo": +5},
                    "etiqueta": "Apertura turística"
                },
                {
                    "texto": "Limitar el acceso para proteger la cultura local.",
                    "efectos": {"felicidad": +3, "dinero": +5},
                    "clases_restringidas": ["Liberal"],
                    "etiqueta": "Turismo regulado"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="El crimen organizado empieza a ganar influencia en barrios periféricos.",
            opciones=[
                {
                    "texto": "Invertir en seguridad y cámaras.",
                    "efectos": {"dinero": -20, "felicidad": +3},
                    "etiqueta": "Política de seguridad"
                },
                {
                    "texto": "Negociar con líderes barriales.",
                    "efectos": {"felicidad": +5},
                    "clases_restringidas": ["Tecno-Productivista", "Guerrera"],
                    "etiqueta": "Abordaje social"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Un río cercano se contamina por una empresa local.",
            opciones=[
                {
                    "texto": "Cerrar la empresa y sancionar.",
                    "efectos": {"empleo": -5, "salud": +10},
                    "etiqueta": "Protección ambiental"
                },
                {
                    "texto": "Exigir mejoras, pero mantener la empresa abierta.",
                    "efectos": {"salud": +5, "dinero": -5},
                    "etiqueta": "Compromiso ambiental"
                },
                {
                    "texto": "No intervenir. Evitar regulación.",
                    "efectos": {"salud": -10, "dinero": +10},
                    "clases_restringidas": ["Colectivista", "Tradicionalista"],
                    "etiqueta": "No regulación"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Una oleada de migrantes llega a tu ciudad en busca de refugio.",
            opciones=[
                {
                    "texto": "Integrarlos en programas sociales.",
                    "efectos": {"dinero": -15, "empleo": +5, "felicidad": +3},
                    "clases_restringidas": ["Aislacionista"],
                    "etiqueta": "Inclusión migratoria"
                },
                {
                    "texto": "Negarles entrada y reforzar fronteras.",
                    "efectos": {"dinero": -5, "felicidad": -2},
                    "etiqueta": "Cierre de fronteras"
                }
            ]
        ),
        EventoInteractivo(
            descripcion="Presión cambiaria.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 1, "felicidad": 5, "reservas": 8, "empleo": 8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -5, "felicidad": -7, "reservas": 8, "empleo": 7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -19, "felicidad": -6, "reservas": 16, "empleo": -2},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -27, "felicidad": -2, "reservas": 20, "empleo": 10},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 25, "felicidad": 3, "reservas": -17, "empleo": 9},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Tasa internacional sube.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -21, "felicidad": -10, "reservas": 5, "empleo": -3},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -6, "felicidad": 1, "reservas": -3, "empleo": 7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -29, "felicidad": -5, "reservas": -14, "empleo": -9},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -29, "felicidad": 7, "reservas": 16, "empleo": 0},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Colapso bancario.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 5, "felicidad": -3, "reservas": -15, "empleo": -1},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 24, "felicidad": 1, "reservas": 19, "empleo": 5},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -23, "felicidad": 8, "reservas": 19, "empleo": 8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 28, "felicidad": 4, "reservas": -14, "empleo": 5},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 16, "felicidad": -1, "reservas": -14, "empleo": 6},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Crisis energética.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -8, "felicidad": -1, "reservas": 9, "empleo": 7},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 2, "felicidad": 8, "reservas": 3, "empleo": -3},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -20, "felicidad": -7, "reservas": 5, "empleo": 0},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 13, "felicidad": 5, "reservas": -12, "empleo": -6},
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 15, "felicidad": -9, "reservas": 8, "empleo": 1},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Boom exportador.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 16, "felicidad": 1, "reservas": 18, "empleo": 1},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -1, "felicidad": 3, "reservas": 19, "empleo": -7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -12, "felicidad": -4, "reservas": 8, "empleo": 5},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -29, "felicidad": -10, "reservas": 20, "empleo": 7},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Déficit fiscal extremo.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 9, "felicidad": 0, "reservas": 5, "empleo": -3},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 21, "felicidad": -4, "reservas": 3, "empleo": -2},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 18, "felicidad": 8, "reservas": -1, "empleo": -1},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -2, "felicidad": -10, "reservas": 9, "empleo": 5},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Reforma previsional.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -15, "felicidad": 1, "reservas": -8, "empleo": -7},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 25, "felicidad": 4, "reservas": 20, "empleo": 6},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -9, "felicidad": 9, "reservas": 16, "empleo": -9},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -20, "felicidad": -5, "reservas": 4, "empleo": -8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": -6, "felicidad": 7, "reservas": -14, "empleo": -9},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Choque externo de demanda.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 5, "felicidad": -5, "reservas": -14, "empleo": -8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 10, "felicidad": -3, "reservas": 13, "empleo": 5},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 2, "felicidad": 9, "reservas": -16, "empleo": -2},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 21, "felicidad": 4, "reservas": 14, "empleo": 6},
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 28, "felicidad": 1, "reservas": 20, "empleo": -8},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Caída en la productividad.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 30, "felicidad": -7, "reservas": -10, "empleo": 2},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -18, "felicidad": -9, "reservas": 7, "empleo": -7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 25, "felicidad": -6, "reservas": -5, "empleo": -4},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 19, "felicidad": -4, "reservas": 17, "empleo": 4},
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 0, "felicidad": 0, "reservas": 2, "empleo": 3},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Descontento por desigualdad.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -16, "felicidad": 4, "reservas": -16, "empleo": -4},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 28, "felicidad": -1, "reservas": 7, "empleo": -2},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 6, "felicidad": -6, "reservas": -2, "empleo": 10},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -7, "felicidad": 6, "reservas": -12, "empleo": -8},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Aumento del desempleo.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 5, "felicidad": -9, "reservas": 18, "empleo": 7},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 12, "felicidad": 7, "reservas": -5, "empleo": 0},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -28, "felicidad": 2, "reservas": 8, "empleo": 5},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 25, "felicidad": 9, "reservas": 13, "empleo": -9},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Aparición de sectores monopólicos.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -24, "felicidad": 7, "reservas": -4, "empleo": 7},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -3, "felicidad": 10, "reservas": 17, "empleo": 8},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 11, "felicidad": -3, "reservas": 12, "empleo": 3},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 16, "felicidad": -5, "reservas": -20, "empleo": -3},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Fuga de capitales.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 17, "felicidad": -6, "reservas": 1, "empleo": -10},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 7, "felicidad": -4, "reservas": 19, "empleo": 10},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 27, "felicidad": 5, "reservas": 4, "empleo": 3},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 12, "felicidad": -6, "reservas": -18, "empleo": -1},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Subsidios insostenibles.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 15, "felicidad": 2, "reservas": 11, "empleo": -3},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 11, "felicidad": 3, "reservas": 13, "empleo": -7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -12, "felicidad": -1, "reservas": 13, "empleo": -8},
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 14, "felicidad": 8, "reservas": -10, "empleo": -7},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Contagio financiero regional.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 6, "felicidad": -9, "reservas": -20, "empleo": 10},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -11, "felicidad": -10, "reservas": -10, "empleo": 2},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 20, "felicidad": -3, "reservas": -10, "empleo": 6},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 30, "felicidad": -6, "reservas": 15, "empleo": -3},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": -19, "felicidad": -4, "reservas": 13, "empleo": -4},
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Presión por apertura comercial.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -5, "felicidad": 6, "reservas": 3, "empleo": -5},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -10, "felicidad": -6, "reservas": -20, "empleo": -5},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": -25, "felicidad": 0, "reservas": 6, "empleo": 7},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 12, "felicidad": -5, "reservas": 4, "empleo": 2},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Fracaso de inversión pública.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": 23, "felicidad": 10, "reservas": 5, "empleo": -7},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -1, "felicidad": -2, "reservas": -3, "empleo": -2},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 16, "felicidad": -1, "reservas": -4, "empleo": 1},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -15, "felicidad": 7, "reservas": -6, "empleo": 9},
                    "etiqueta": "Estrategia 4"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Emergencia sanitaria masiva.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -16, "felicidad": -8, "reservas": -1, "empleo": -1},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 0, "felicidad": 5, "reservas": -15, "empleo": 4},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 23, "felicidad": -3, "reservas": 12, "empleo": -5},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -25, "felicidad": -1, "reservas": 11, "empleo": -4},
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": 10, "felicidad": -4, "reservas": -12, "empleo": -1},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Crisis climática productiva.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -28, "felicidad": -9, "reservas": -1, "empleo": 0},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": -28, "felicidad": 2, "reservas": 8, "empleo": -4},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 2, "felicidad": -2, "reservas": -4, "empleo": -8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": -11, "felicidad": -1, "reservas": 13, "empleo": 4},
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": -24, "felicidad": 1, "reservas": 6, "empleo": 4},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
        EventoInteractivo(
            descripcion="Explosión del mercado informal.",
            opciones=[
                {
                    "texto": "Opción 1",
                    "efectos": {"dinero": -27, "felicidad": 0, "reservas": 3, "empleo": 3},
                    "etiqueta": "Estrategia 1"
                },
                {
                    "texto": "Opción 2",
                    "efectos": {"dinero": 21, "felicidad": -6, "reservas": 11, "empleo": 7},
                    "etiqueta": "Estrategia 2"
                },
                {
                    "texto": "Opción 3",
                    "efectos": {"dinero": 1, "felicidad": -2, "reservas": -18, "empleo": -8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 3"
                },
                {
                    "texto": "Opción 4",
                    "efectos": {"dinero": 30, "felicidad": 10, "reservas": -11, "empleo": -4},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 4"
                },
                {
                    "texto": "Opción 5",
                    "efectos": {"dinero": -9, "felicidad": -3, "reservas": 4, "empleo": -8},
                    "clases_restringidas": ['Liberal', 'Colectivista'],
                    "etiqueta": "Estrategia 5"
                },
            ]
        ),
    ]
    probabilidad = 0.25
    if random.random() < probabilidad:
        return random.choice(eventos)
    return None


    probabilidad = 0.2  # 20% chance
    if random.random() < probabilidad:
        return random.choice(eventos)
    return None
