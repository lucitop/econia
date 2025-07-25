
def presentar_objetivos(ciudad):
    print(f"\n{'='*60}")
    print(f"Has sido elegido líder de una ciudad con valores {ciudad.clase.upper()}.")
    print("Tu pueblo espera que guíes su destino con sabiduría y convicción.")
    print("Tus misiones son las siguientes:")
    print(f"{'='*60}\n")

    print("🎯 Objetivos Principales:")
    for obj in ciudad.objetivos.get("principales", []):
        print(f"  - {obj}")

    print("\n🛠 Objetivos Secundarios:")
    for obj in ciudad.objetivos.get("secundarios", []):
        print(f"  - {obj}")

    print(f"\n{'='*60}\n")
    input("Presioná Enter para comenzar tu liderazgo...")
