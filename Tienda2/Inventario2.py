#!/usr/bin/env python3

"""
Título de práctica: Inventario tienda 2

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-03-06
"""


class Inventario:
    """Clase que representa el inventario de una tienda"""
    def __init__(self, nombre, descripcion, clasificacion, cantidad, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.cantidad = cantidad
        self.precio = precio
    # muestra los productos seleccionados

    def show_inventory(self):
        return (f"{self.nombre:<11}" f"{self.descripcion:<15}"
                f"{self.clasificacion:<20}" f"{self.cantidad:<8}"
                f"{self.precio:<8} COP")


def add_product():
    """Agrega un producto al inventario"""
    nombre = input("Nombre del producto: ")
    descripcion = input(f"Descripcion del producto {nombre}: ")
    clasificacion = input(f"Clasificacion del producto {nombre}: ")
    cantidad = int(input(f"Cantidad de {descripcion}: "))
    precio = int(input(f"Precio unitario de {descripcion}: "))
    return Inventario(nombre, descripcion, clasificacion, cantidad, precio)


def see_inventory(inventario):
    """Muestra el inventario"""
    print("\n Nombre   Descripcion   Clasificacion   Cantidad   Precio")
    print("------------------------------------------------------------")
    # Muestra el inventario
    for producto in inventario:
        print(producto.show_inventory())


def show_group_food(inventario):
    """Agrupa los productos por clasificación"""
    clasificacion = {}
    for producto in inventario:
        if producto.clasificacion in clasificacion:
            clasificacion[producto.clasificacion].append(producto)
        else:
            clasificacion[producto.clasificacion] = [producto]
    print("\nProductos agrupados por clasificación:")
    print("Clasificación  Total precio")
    print("---------------------------")
    for clasificacion, producto in clasificacion.items():
        total_precio = sum([producto.precio * producto.cantidad
                            for producto in producto])
        print(f"{clasificacion:<15} {total_precio:<10} COP")


def main():
    cant_product = int(input("Cuantos productos vas a ingresar: "))
    productos = []
    # Pedimos los datos para añadir los productos
    for i in range(cant_product):
        print(f"\n {i+1} Producto:")
        producto = add_product()
        productos.append(producto)
    # muestra el inventario en forma de tabla
    print("\nDatos de los productos ingresados:")
    see_inventory(productos)
    show_group_food(productos)


if __name__ == "__main__":
    main()
