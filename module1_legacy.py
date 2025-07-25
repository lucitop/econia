import random

class Ciudad:
    def __init__(self):
        self.poblacion = 1000
        self.dinero = 100
        self.felicidad = 50
        self.salud = 60
        self.empleo = 70
        self.historial = []

    def aplicar_politica(self, politica):
        efecto = politica.ejecutar()
        for k, v in efecto.items():
            if hasattr(self, k):
                setattr(self, k, max(0, getattr(self, k) + v))
        self.historial.append((politica.nombre, efecto))

    def mostrar_estado(self):
        print(f"Población: {self.poblacion}")
        print(f"Dinero: {self.dinero}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Salud: {self.salud}")
        print(f"Empleo: {self.empleo}")
        print("-" * 30)


class PoliticaEconomica:
    def __init__(self, nombre, descripcion, efectos_probabilisticos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.efectos = efectos_probabilisticos  # dict de {'variable': función aleatoria}

    def ejecutar(self):
        resultado = {}
        for k, funcion in self.efectos.items():
            resultado[k] = funcion()
        return resultado

# Ejemplo de políticas con efectos probabilísticos
def crear_politicas():
    return [
        PoliticaEconomica(
            "Subir Impuestos",
            "Aumenta el dinero, pero puede bajar la felicidad.",
            {
                "dinero": lambda: random.randint(10, 30),
                "felicidad": lambda: random.choice([-5, -10, 0])
            }
        ),
        PoliticaEconomica(
            "Invertir en salud",
            "Gasta dinero, pero mejora salud y felicidad.",
            {
                "dinero": lambda: -random.randint(10, 25),
                "salud": lambda: random.randint(5, 15),
                "felicidad": lambda: random.choice([0, 3, 5])
            }
        )
    ]

# Lógica del juego (bucle)
def main():
    ciudad = Ciudad()
    politicas = crear_politicas()
    dia = 1

    while True:
        print(f"\n--- dia {dia} ---")
        ciudad.mostrar_estado()

        print("Elegí una política:")
        for i, p in enumerate(politicas):
            print(f"{i + 1}. {p.nombre} - {p.descripcion}")
        eleccion = input("Tu elección (1 o 2, q para salir): ")

        if eleccion == 'q':
            break

        try:
            politica = politicas[int(eleccion) - 1]
            ciudad.aplicar_politica(politica)
            dia += 1
        except:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
