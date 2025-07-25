class Ciudad:
    def __init__(self, nombre, clase):
        from city_goals import obtener_objetivos_para_clase
        self.nombre = nombre
        self.poblacion = 1000
        self.dinero = 100
        self.felicidad = 50
        self.salud = 60
        self.empleo = 70
        self.reservas = 50
        self.identidad = clase
        self.clase = clase
        self.objetivos = obtener_objetivos_para_clase(clase)

        self.dia = 1
        self.historial = []

    def aplicar_efectos(self, efectos: dict, fuente: str):
        for variable, cambio in efectos.items():
            if hasattr(self, variable):
                valor_actual = getattr(self, variable)
                nuevo_valor = max(0, valor_actual + cambio)
                setattr(self, variable, nuevo_valor)
        self.historial.append((self.dia, fuente, efectos))

    def mostrar_estado(self):
        print("\n=== Estado de la Ciudad ===")
        print(f"dia actual: {self.dia}")
        print(f"Población: {self.poblacion}")
        print(f"Dinero: {self.dinero}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Salud: {self.salud}")
        print(f"Empleo: {self.empleo}")
        print(f"Reservas: {self.reservas}")
        print("===========================\n")

    def avanzar_dia(self):
        self.dia += 1
