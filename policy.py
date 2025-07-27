class Politica:
    def __init__(self, nombre, efectos, clases_permitidas=None):
        self.nombre = nombre
        self.efectos = efectos  # dict: {"dinero": -20, "salud": +10}
        self.clases_permitidas = clases_permitidas or []

    def aplicar(self, ciudad):
        ciudad.aplicar_efectos(self.efectos, self.nombre)
        return self.efectos

def crear_politicas_por_defecto():
    return [
        Politica(
            "Inversión en salud pública",
            {"dinero": -20, "salud": +10},
            clases_permitidas=["Colectivista", "Tradicionalista"]
        ),
        Politica(
            "Reducción de impuestos",
            {"dinero": -10, "felicidad": +5},
            clases_permitidas=["Liberal"]
        ),
        Politica(
            "Subsidios al empleo",
            {"dinero": -15, "empleo": +8},
            clases_permitidas=["Pragmática", "Colectivista"]
        ),
        Politica(
            "Ajuste fiscal severo",
            {"dinero": +30, "felicidad": -10},
            clases_permitidas=["Liberal", "Tecno-Productivista"]
        ),
        Politica(
            "Reforma educativa pública",
            {"dinero": -25, "empleo": +5, "felicidad": +4},
            clases_permitidas=["Colectivista", "Tradicionalista"]
        )
    ]
