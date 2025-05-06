#!/usr/bin/env python3

"""
Título de práctica: Calculadora de Matrices

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-05-05
"""


class Matriz:
    """Ingreso datos de la matriz, operaciones"""
    def __init__(self, a11, a12, a21, a22):
        self.matriz = [[a11, a12], [a21, a22]]

    def __str__(self):
        return (
            f"{self.matriz[0][0]}"
            f"{self.matriz[0][1]}\n{self.matriz[1][0]}"
            f"{self.matriz[1][1]}"
            )

    def __add__(self, Segunda):
        """Suma de matrices"""
        return Matriz(
            self.matriz[0][0] + Segunda.matriz[0][0],
            self.matriz[0][1] + Segunda.matriz[0][1],
            self.matriz[1][0] + Segunda.matriz[1][0],
            self.matriz[1][1] + Segunda.matriz[1][1]
            )

    def __sub__(self, Segunda):
        """Resta de matrices"""
        return Matriz(
            self.matriz[0][0] - Segunda.matriz[0][0],
            self.matriz[0][1] - Segunda.matriz[0][1],
            self.matriz[1][0] - Segunda.matriz[1][0],
            self.matriz[1][1] - Segunda.matriz[1][1])

    def __mul__(self, otra):
        """Multiplicación de matrices"""
        a11 = [self.matriz[0][0] * otra.matriz[0][0]
               + self.matriz[0][1] * otra.matriz[1][0]]
        a12 = [self.matriz[0][0] * otra.matriz[0][1]
               + self.matriz[0][1] * otra.matriz[1][1]]
        a21 = [self.matriz[1][0] * otra.matriz[0][0]
               + self.matriz[1][1] * otra.matriz[1][0]]
        a22 = [self.matriz[1][0] * otra.matriz[0][1]
               + self.matriz[1][1] * otra.matriz[1][1]]
        return Matriz(a11, a12, a21, a22)


def ingresar_matriz():
    print("Introduce los valores de la matriz 2x2:")
    while True:
        try:
            a11 = int(input("a11: "))
            a12 = int(input("a12: "))
            a21 = int(input("a21: "))
            a22 = int(input("a22: "))
            break
        except ValueError:
            print("Datos no validos")
    return Matriz(a11, a12, a21, a22)


def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar matrices")
    print("2. Restar matrices")
    print("3. Multiplicar matrices")
    print("4. Salir")


def Otra_operacion():
    """Preguntar si desea hacer una nueva operacion
    con la misma matriz"""
    while True:
        respuesta = input("Deseas realizar otra "
                          "operacion? Si/No ").strip().lower()
        if respuesta == 'si':
            return True
        elif respuesta == 'no':
            return False
        else:
            print("Elija una opción valida")


def main():
    print("Calculadora de matrices 2x2")

    # Ingresar dos matrices
    print("Matriz 1:")
    matriz1 = ingresar_matriz()
    print("Matriz 2:")
    matriz2 = ingresar_matriz()

    while True:
        mostrar_menu()
        opcion = int(input("Opción: "))

        if opcion == 1:
            resultado = matriz1 + matriz2
            print(f"\nResultado de la suma:\n{resultado}")
        elif opcion == 2:
            resultado = matriz1 - matriz2
            print(f"\nResultado de la resta:\n{resultado}")
        elif opcion == 3:
            resultado = matriz1 * matriz2
            print(f"\nResultado de la multiplicación:\n{resultado}")
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona de nuevo.")
            continue
        if not Otra_operacion():
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()
