import random

class Advisor:
    def __init__(self):
        self.last_used_turn = -10  # permite usarlo al inicio
        self.cooldown = 3  # dias mínimos entre consultas

    def can_consult(self, current_turn):
        return (current_turn - self.last_used_turn) >= self.cooldown

    def consult(self, city):
        self.last_used_turn = city.dia

        recomendaciones = []

        if city.salud < 40:
            recomendaciones.append("Invertir en salud")
        if city.felicidad < 35:
            recomendaciones.append("Subsidios a la cultura")
        if city.dinero < 40:
            recomendaciones.append("Subir impuestos")
        if city.empleo < 50:
            recomendaciones.append("Construir fábricas")
        if city.reservas < 20:
            recomendaciones.append("Evitar emitir dinero")

        if not recomendaciones:
            recomendaciones.append("Podés permitirte asumir riesgos. Tal vez emitir dinero o invertir en infraestructura.")

        # Posibilidad de error o duda
        if random.random() < 0.15:
            return "Mmm... difícil saberlo. Yo probaría con: " + random.choice([
                "Subir impuestos",
                "Recortar gastos",
                "Emitir dinero"
            ])
        else:
            return "Según los indicadores actuales, te recomiendo: " + random.choice(recomendaciones)
