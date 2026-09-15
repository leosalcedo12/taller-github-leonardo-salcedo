def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


def mostrar_menu():
    print("\n--- CONVERTIDOR DE TEMPERATURA ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()

        if opcion == "3":
            print("¡Gracias por usar el convertidor!")
            break

        if opcion in ("1", "2"):
            try:
                temp = float(input("Ingresa la temperatura a convertir: "))
            except ValueError:
                print("Error: Ingresa un número válido.")
                continue

            if opcion == "1":
                resultado = celsius_a_fahrenheit(temp)
                print(f"-> {temp}°C equivalen a {resultado:.2f}°F")
            elif opcion == "2":
                resultado = fahrenheit_a_celsius(temp)
                print(f"-> {temp}°F equivalen a {resultado:.2f}°C")
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
