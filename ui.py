from colorama import Fore, Style, init

init(autoreset=True)

def separador():
    print(f"\n{Fore.WHITE + '=' * 50}")

def mostrar_estado(ciudad):
    separador()
    print(f"{Style.BRIGHT + Fore.CYAN}🏙️  ESTADO ACTUAL DE TU CIUDAD")
    separador()
    print(f"{Style.BRIGHT}📛 Nombre:       {Style.RESET_ALL}{ciudad.nombre}")
    print(f"{Style.BRIGHT}🏷️  Clase:        {Style.RESET_ALL}{ciudad.identidad}")
    print(f"{Style.BRIGHT}📅 Día:          {Style.RESET_ALL}{ciudad.dia}")
    print("-" * 50)
    print(f"{Fore.YELLOW}💰 Dinero:        {ciudad.dinero}")
    print(f"{Fore.RED}❤️ Salud:         {ciudad.salud}")
    print(f"{Fore.GREEN}😊 Felicidad:     {ciudad.felicidad}")
    print(f"{Fore.BLUE}🔧 Empleo:        {ciudad.empleo}")
    print(f"{Fore.MAGENTA}🏦 Reservas:      {ciudad.reservas}")
    separador()

def mostrar_menu():
    separador()
    print(f"{Style.BRIGHT + Fore.CYAN}📋 MENÚ PRINCIPAL")
    separador()
    print(f"{Fore.GREEN}1. Aplicar política")
    print(f"{Fore.BLUE}2. Consultar al consejero")
    print(f"{Fore.CYAN}3. Ver estado actual")
    print(f"{Fore.YELLOW}4. Ver historial")
    print(f"{Fore.MAGENTA}5. Avanzar un día")
    print(f"{Fore.WHITE}6. Guardar juego")
    print(f"{Fore.WHITE}7. Cargar juego")
    print(f"{Fore.RED}8. Salir")
    separador()

def mostrar_bienvenida():
    separador()
    print(f"{Style.BRIGHT + Fore.CYAN}=== Bienvenido a CIVITAS: El Legado de las Ciudades ===")
    separador()
    print(f"{Fore.WHITE}Año 2450. El viejo mundo ha colapsado.")
    print("Pequeñas comunidades independientes emergen de las ruinas, buscando forjar una nueva era.")
    print("Tu rol es guiar a una de esas ciudades: ¿serás un líder sabio, implacable, espiritual o progresista?")
    separador()
