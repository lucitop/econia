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

    probabilidad_evento = 0.25  # 25% de chance por dia
    if random.random() < probabilidad_evento:
        return random.choice(eventos)
    else:
        return None
