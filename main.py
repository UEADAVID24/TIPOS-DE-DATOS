# Este programa calcula el área de diferentes figuras geométricas.
# Puede calcular el área de un círculo, un rectángulo o un triángulo,
# dependiendo de la opción seleccionada por el usuario.

import math


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    area_circulo = math.pi * radio ** 2
    return area_circulo


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    area_rectangulo = base * altura
    return area_rectangulo


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    area_triangulo = (base * altura) / 2
    return area_triangulo


# Función principal del programa
def main():
    # Solicitar al usuario que elija una figura
    print("Elige una figura geométrica para calcular su área:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")

    # Obtener la opción del usuario
    opcion = int(input("Ingresa el número de la figura (1-3): "))

    if opcion == 1:
        # Calcular área de un círculo
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")

    elif opcion == 2:
        # Calcular área de un rectángulo
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")

    elif opcion == 3:
        # Calcular área de un triángulo
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")

    else:
        print("Opción inválida. Por favor elige una opción entre 1 y 3.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

