from save_manager import save_game, load_game
from ui import mostrar_estado, mostrar_menu, mostrar_bienvenida
from city import Ciudad
from events import get_random_event
from policy import create_default_policies
from advisor import Advisor
import sys
import os
import keyboard
import random
from city_identity import seleccionar_preguntas, clasificar_ciudad, PREGUNTAS_POOL, aplicar_bonos_ciudad
from city_loader import cargar_ciudad
import time
from colorama import init, Fore, Style
init(autoreset=True, convert=True, strip=False)
import shutil
import msvcrt

interrumpir_animacion = False

def mostrar_objetivos_esteticos(ciudad):
    print(Fore.YELLOW + "\n" + "─" * 10 + " 🎯 OBJETIVOS DE TU CIUDAD " + "─" * 10 + Style.RESET_ALL)

    primarios = ciudad.objetivos.get("principales", [])
    secundarios = ciudad.objetivos.get("secundarios", [])

    if primarios:
        print(Fore.CYAN + "🔸 Objetivos Primarios:" + Style.RESET_ALL)
        for obj in primarios:
            print("   •", obj)
    if secundarios:
        print(Fore.MAGENTA + "\n🔹 Objetivos Secundarios:" + Style.RESET_ALL)
        for obj in secundarios:
            print("   •", obj)
    print()

def imprimir_titulo_enmarcado(texto, padding=5):
    columnas = shutil.get_terminal_size().columns
    ancho_total = len(texto) + 2 * padding
    linea_superior = "╔" + "═" * ancho_total + "╗"
    linea_central = "║" + " " * padding + texto + " " * padding + "║"
    linea_inferior = "╚" + "═" * ancho_total + "╝"

    
    margen_izquierdo = (columnas - (ancho_total + 2)) // 2
    print()
    print(" " * margen_izquierdo + linea_superior)
    print(" " * margen_izquierdo + linea_central)
    print(" " * margen_izquierdo + linea_inferior)

def imprimir_linea_animada(texto, delay=0.055):
    global interrumpir_animacion

    for i, char in enumerate(texto):
        if msvcrt.kbhit():  # si se presionó alguna tecla
            tecla = msvcrt.getch()
            if tecla == b'\r':  # si fue Enter
                sys.stdout.write(texto[i:])
                sys.stdout.flush()
                interrumpir_animacion = True
                break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def imprimir_linea_animada_centrada(texto, delay=0.055):
    global interrumpir_animacion
    columnas = shutil.get_terminal_size().columns
    margen = (columnas - len(texto)) // 2
    sys.stdout.write(" " * margen)
    sys.stdout.flush()

    for i, char in enumerate(texto):
        if msvcrt.kbhit():  # si se presionó alguna tecla
            tecla = msvcrt.getch()
            if tecla == b'\r':  # si fue Enter
                sys.stdout.write(texto[i:])
                sys.stdout.flush()
                interrumpir_animacion = True
                break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def imprimir_linea_animada_centrada_rapida(texto, delay=0.03):
    global interrumpir_animacion
    columnas = shutil.get_terminal_size().columns
    margen = (columnas - len(texto)) // 2
    sys.stdout.write(" " * margen)
    sys.stdout.flush()

    for i, char in enumerate(texto):
        if msvcrt.kbhit():  # si se presionó alguna tecla
            tecla = msvcrt.getch()
            if tecla == b'\r':  # si fue Enter
                sys.stdout.write(texto[i:])
                sys.stdout.flush()
                interrumpir_animacion = True
                break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def esperar_tecla_final_y_limpiar_buffer():
    print()
    print(" " * ((shutil.get_terminal_size().columns - 30) // 2) + "[Presioná Enter para continuar...]")
    while True:
        if msvcrt.kbhit():
            if msvcrt.getch() == b'\r':
                break
    while msvcrt.kbhit():
        msvcrt.getch()

def realizar_test_personalidad():
    import random

    os.system('cls' if os.name == 'nt' else 'clear')

    imprimir_linea_animada_centrada("Antes de guiar a tu ciudad, debés descubrir quién sos.")
    imprimir_linea_animada_centrada("Responderás una serie de preguntas fundamentales.")
    imprimir_linea_animada_centrada("Tus respuestas determinarán la personalidad de tu ciudad.")
    imprimir_linea_animada_centrada("." * 3)
    input("Presioná Enter para comenzar el test...")

    os.system('cls' if os.name == 'nt' else 'clear')

    preguntas = seleccionar_preguntas(PREGUNTAS_POOL, 10)
    respuestas = []

    for idx, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {idx}/10:")
        print(pregunta["texto"])
        opciones = list(pregunta["opciones"].keys())
        for i, opcion in enumerate(opciones):
            print(f"  {i + 1}. {opcion}")

        while True:
            try:
                eleccion = int(input("Seleccioná una opción: "))
                if 1 <= eleccion <= len(opciones):
                    clase_asociada = pregunta["opciones"][opciones[eleccion - 1]]
                    respuestas.append(clase_asociada if clase_asociada else None)
                    break
            except ValueError:
                pass
            print("Entrada inválida. Intentá de nuevo.")

        os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nEvaluando tus respuestas", end="")
    for _ in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)
    time.sleep(1)
    print("\n")

    clase_final = clasificar_ciudad(respuestas)

    imprimir_linea_animada_centrada("El destino de tu ciudad ya está marcado.")
    imprimir_linea_animada_centrada(f"Clase asignada: {clase_final.upper()}")
    input("Presioná Enter para continuar...")

    return clase_final


def introduccion():
    imprimir_titulo_enmarcado("CIVITAS: El Legado de las Ciudades", padding=4)

    time.sleep(0.6)
    print()
    imprimir_linea_animada_centrada("Año 2450. El viejo mundo ha colapsado.")
    time.sleep(0.6)

    imprimir_linea_animada_centrada("Pequeñas comunidades independientes comienzan a emerger de las ruinas,")
    imprimir_linea_animada_centrada("buscando forjar una nueva era.")
    time.sleep(0.6)

    print()
    imprimir_linea_animada_centrada("Tu rol es guiar a una de esas ciudades.")
    imprimir_linea_animada_centrada("¿Serás un líder sabio, implacable, espiritual o progresista?")
    time.sleep(0.6)
    print("\n" + "═" * 60 + "\n")



def imprimir_titulo(titulo):
    borde = "=" * (len(titulo) + 8)
    print(f"\n{borde}\n==  {titulo}  ==\n{borde}")

def imprimir_seccion(titulo):
    print(f"\n-- {titulo} --")


def iniciar_juego():
    ciudad = None
    introduccion()
    eleccion = input("¿Querés comenzar un (N)uevo juego o (C)argar uno existente? ").strip().lower()

    if eleccion == "debugmode":
        from debug_tools import modo_debug_ciudad
        ciudad = Ciudad("Debugópolis", "Pragmática")
        ciudad.dia = 42
        ciudad.dinero = 9999
        ciudad.salud = 80
        ciudad.felicidad = 70
        ciudad.reservas = 120
        ciudad.historial = [("1", "Inicio", {"dinero": +100})]
        modo_debug_ciudad(ciudad)
        input("\nPresioná Enter para continuar en modo debug...")
    
    elif eleccion == 'c':
        ciudad = cargar_ciudad()

    else:
        clase_ciudad = realizar_test_personalidad()
        efectos = aplicar_bonos_ciudad(None, clase_ciudad, solo_devolver=True)
        imprimir_titulo(f"Tu ciudad ha sido clasificada como: {clase_ciudad}")
        print(f"Descripción: {efectos['descripcion']}")

        imprimir_seccion("Efectos positivos")
        for bono in efectos['bonos']:
            print(f" - {bono}")

        imprimir_seccion("Efecto negativo")
        print(efectos['penalizacion'])
        print()

        nombre_ciudad = input(Fore.YELLOW + Style.BRIGHT + "🏙️ ¿Cómo querés llamar a tu ciudad? " + Fore.WHITE)
        ciudad = Ciudad(nombre=nombre_ciudad, clase=clase_ciudad)
        from city_goals import obtener_objetivos_para_clase

        objetivos = obtener_objetivos_para_clase(clase_ciudad)
        print("\n🌟 Objetivos estratégicos de tu ciudad:\n")
        print("🔹 Objetivos principales:")
        for obj in objetivos["principales"]:
            print(f"  - {obj}")

        print("\n🔸 Objetivos secundarios:")
        for obj in objetivos["secundarios"]:
            print(f"  - {obj}")

    return ciudad

def mostrar_menu():
    print(Fore.MAGENTA + Style.BRIGHT + "\n╔══════════════════════════════════════════╗")
    print("║           MENÚ PRINCIPAL                ║")
    print("╚══════════════════════════════════════════╝")
    print(Fore.CYAN + "1." + Fore.WHITE + " Aplicar política")
    print(Fore.CYAN + "2." + Fore.WHITE + " Consultar al consejero")
    print(Fore.CYAN + "3." + Fore.WHITE + " Ver estado actual")
    print(Fore.CYAN + "4." + Fore.WHITE + " Ver historial")
    print(Fore.CYAN + "5." + Fore.WHITE + " Avanzar un día")
    print(Fore.CYAN + "6." + Fore.WHITE + " Guardar juego")
    print(Fore.CYAN + "7." + Fore.WHITE + " Cargar juego")
    print(Fore.CYAN + "8." + Fore.WHITE + " Salir")

def mostrar_estado_estetico(city):
    print("\n" + Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(f"{Fore.YELLOW}Estado actual de {city.nombre} (Día {city.dia}):")
    print(Fore.CYAN + "-" * 50)
    print(f"{Fore.GREEN}Clase: {Fore.WHITE}{city.identidad}")
    print(f"{Fore.GREEN}Población: {Fore.WHITE}{city.poblacion}")
    print(f"{Fore.GREEN}Dinero: {Fore.WHITE}${city.dinero}")
    print(f"{Fore.GREEN}Felicidad: {Fore.WHITE}{city.felicidad}%")
    print(f"{Fore.GREEN}Salud: {Fore.WHITE}{city.salud}%")
    print(f"{Fore.GREEN}Empleo: {Fore.WHITE}{city.empleo}%")
    print(f"{Fore.GREEN}Reservas: {Fore.WHITE}{city.reservas} unidades")
    print(Fore.CYAN + "=" * 50 + "\n")

def menu_aplicar_politica(city, policies):
    print("\nPolíticas disponibles:")
    for i, policy in enumerate(policies):
        print(f"{i + 1}. {policy.name}")
    try:
        eleccion = int(input("Elegí una política para aplicar (número): "))
        politica_seleccionada = policies[eleccion - 1]
        efectos = politica_seleccionada.apply()
        city.aplicar_efectos(efectos, politica_seleccionada.name)
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\nAplicada política: {politica_seleccionada.name}")
        print(Fore.YELLOW + f"Efectos: {efectos}")
        mostrar_estado_estetico(city)
        print(Fore.LIGHTBLUE_EX + "─" * 50)


    except (ValueError, IndexError):
        print("Opción no válida.")

def menu_ver_historial(city):
    print(Fore.LIGHTMAGENTA_EX + "\n╔══════════════════════════════════════╗")
    print("║         HISTORIAL DE DECISIONES     ║")
    print("╚══════════════════════════════════════╝")
    if not city.historial:
        print(Fore.YELLOW + "Todavía no tomaste ninguna acción.")
    for dia, fuente, efectos in city.historial:
        efecto_str = ', '.join(f"{k}: {v:+}" for k, v in efectos.items())
        print(Fore.WHITE + f"🗓️ Día {dia} - {fuente}: {Fore.CYAN}{efecto_str}")
    print(Fore.LIGHTMAGENTA_EX + "════════════════════════════════════════")

def main():
    city = iniciar_juego()
    if city is None:
        print("No se pudo iniciar el juego correctamente.")
        return

    policies = create_default_policies()
    advisor = Advisor()

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            menu_aplicar_politica(city, policies)

        elif opcion == "2":
            if advisor.can_consult(city.dia):
                recomendacion = advisor.consult(city)
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\nConsejero: " + Fore.LIGHTGREEN_EX + recomendacion)
            else:
                dias_restantes = advisor.cooldown - (city.dia - advisor.last_used_turn)
                print(f"\nEl consejero necesita descansar. Podés volver a consultarlo en {dias_restantes} dia(s).")

        elif opcion == "3":
            mostrar_estado_estetico(city)

        elif opcion == "4":
            menu_ver_historial(city)

        elif opcion == "5":
            city.avanzar_dia()
            evento = get_random_event()
            if evento:
                print("\n" + evento.apply(city))
            print("\nPasó un día. Nuevo dia.")

        elif opcion == "6":
            save_game(city, advisor)

        elif opcion == "7":
            load_game(city, advisor)

        elif opcion == "8":
            print(Fore.GREEN + Style.BRIGHT + "\n╔════════════════════════════╗")
            print("║ ¡Gracias por jugar! 🌆     ║")
            print("╚════════════════════════════╝")
            sys.exit()

        else:
            print("Opción no válida. Por favor, intentá de nuevo.")

if __name__ == "__main__":
    main()
