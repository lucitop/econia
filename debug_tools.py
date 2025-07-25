def modo_debug_ciudad(ciudad):
    print("\n===== MODO DEBUG ACTIVADO =====")
    print(f"Nombre: {ciudad.nombre}")
    print(f"Clase: {ciudad.clase}")
    print(f"Día: {getattr(ciudad, 'dia', 'No definido')}")
    print(f"Dinero: {getattr(ciudad, 'dinero', 'No definido')}")
    print(f"Salud: {getattr(ciudad, 'salud', 'No definido')}")
    print(f"Felicidad: {getattr(ciudad, 'felicidad', 'No definido')}")
    print(f"Empleo: {getattr(ciudad, 'empleo', 'No definido')}")
    print(f"Reservas: {getattr(ciudad, 'reservas', 'No definido')}")
    print(f"Identidad: {getattr(ciudad, 'identidad', 'No definida')}")
    print(f"Efectos aplicados: {getattr(ciudad, 'efectos_aplicados', 'Ninguno')}")

    print(f"\nHistorial:")
    if hasattr(ciudad, 'historial') and ciudad.historial:
        for entrada in ciudad.historial:
            print(" -", entrada)
    else:
        print("Sin historial registrado.")
    print("===============================\n")

    # Guardado automático
    try:
        with open("debug_log.txt", "w", encoding="utf-8") as f:
            f.write("===== MODO DEBUG LOG =====\n")
            f.write(f"Nombre: {ciudad.nombre}\n")
            f.write(f"Clase: {ciudad.clase}\n")
            f.write(f"Día: {getattr(ciudad, 'dia', 'No definido')}\n")
            f.write(f"Dinero: {getattr(ciudad, 'dinero', 'No definido')}\n")
            f.write(f"Salud: {getattr(ciudad, 'salud', 'No definido')}\n")
            f.write(f"Felicidad: {getattr(ciudad, 'felicidad', 'No definido')}\n")
            f.write(f"Empleo: {getattr(ciudad, 'empleo', 'No definido')}\n")
            f.write(f"Reservas: {getattr(ciudad, 'reservas', 'No definido')}\n")
            f.write(f"Identidad: {getattr(ciudad, 'identidad', 'No definida')}\n")
            f.write(f"Efectos aplicados: {getattr(ciudad, 'efectos_aplicados', 'Ninguno')}\n\n")
            f.write("Historial:\n")
            if hasattr(ciudad, 'historial') and ciudad.historial:
                for entrada in ciudad.historial:
                    f.write(f" - {entrada}\n")
            else:
                f.write("Sin historial registrado.\n")
            f.write("===========================\n")
    except Exception as e:
        print(f"Error al guardar debug_log.txt: {e}")

    # === Menú interactivo de pruebas ===
    while True:
        print("\n¿Qué querés hacer?")
        print("1. Avanzar un día")
        print("2. Aplicar política de prueba")
        print("3. Ver estado actual")
        print("4. Editar variable")
        print("5. Ver historial")
        print("6. Simular evento aleatorio")
        print("0. Salir del modo debug")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            ciudad.dia += 1
            print(f"Avanzaste al día {ciudad.dia}.")
        elif opcion == "2":
            print("\nSeleccioná una política de prueba:")
            politicas = {
                "1": {"nombre": "Reducción de impuestos", "efectos": {"dinero": -200, "felicidad": +10}},
                "2": {"nombre": "Aumento en salud pública", "efectos": {"salud": +15, "dinero": -300}},
                "3": {"nombre": "Propaganda patriótica", "efectos": {"felicidad": +20, "dinero": -100}},
            }

            for clave, datos in politicas.items():
                print(f"{clave}. {datos['nombre']} → efectos: {datos['efectos']}")

            eleccion = input("Elegí una opción: ").strip()
            if eleccion in politicas:
                elegida = politicas[eleccion]
                ciudad.aplicar_efectos(elegida["efectos"], f"Debug - {elegida['nombre']}")
                print(f"Aplicaste: {elegida['nombre']}")
            else:
                print("Opción inválida.")
        elif opcion == "3":
            print("\nEstado actual:")
            print(f"Dinero: {ciudad.dinero}")
            print(f"Salud: {ciudad.salud}")
            print(f"Felicidad: {ciudad.felicidad}")
            print(f"Empleo: {ciudad.empleo}")
            print(f"Reservas: {ciudad.reservas}")
        elif opcion == "4":
            var = input("Variable a editar (dinero, salud, felicidad, empleo, reservas): ").strip()
            if hasattr(ciudad, var):
                try:
                    val = int(input(f"Nuevo valor para {var}: "))
                    setattr(ciudad, var, val)
                    print(f"{var} ahora vale {val}")
                except:
                    print("Valor inválido.")
            else:
                print("Variable no reconocida.")
        elif opcion == "5":
            print("\nHistorial:")
            for h in ciudad.historial:
                print(" -", h)
        elif opcion == "6":
            import random
            eventos = [
                ("Epidemia", {"salud": -20, "felicidad": -10}),
                ("Boom económico", {"dinero": +1000, "empleo": +10}),
                ("Crisis energética", {"dinero": -500, "felicidad": -5}),
                ("Inmigración masiva", {"poblacion": +500, "empleo": -5}),
                ("Donación internacional", {"dinero": +800}),
            ]
            evento = random.choice(eventos)
            nombre, efectos = evento
            ciudad.aplicar_efectos(efectos, f"Evento aleatorio - {nombre}")
            print(f"\nSe simuló el evento: {nombre}")
            print(f"Efectos: {efectos}")
        elif opcion == "0":
            print("Saliendo del modo debug...")
            break
        else:
            print("Opción inválida.")
