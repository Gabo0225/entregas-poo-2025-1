#!/usr/bin/env python3

"""
Título de práctica: Inventario tienda 3

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-03-11
"""


class Inventario:
    """Clase que representa el inventario de una tienda"""
    def __init__(self, nombre, descripcion, clasificacion, cantidad,
                 precio, total_precio, totalx5):
        self.nombre = nombre
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.cantidad = cantidad
        self.precio = precio
        self.total_precio = total_precio
        self.totalx5 = totalx5
    # muestra los productos seleccionados

    def show_inventory(self):
        return [f"{self.nombre}",
                f"{self.descripcion}",
                f"{self.clasificacion}",
                f"{self.cantidad} Unidad(es)",
                f"{self.precio} COP",
                f"{self.total_precio} COP",
                f"{self.totalx5} COP"]


def add_product():
    """Agrega un producto al inventario"""
    nombre = input("Nombre del producto: ")
    descripcion = input(f"Descripcion del producto {nombre}: ")
    clasificacion = input(f"Clasificacion del producto {nombre}: ").lower()
    cantidad = int(input(f"Cantidad de {descripcion}: "))
    precio = int(input(f"Precio unitario de {descripcion}: "))
    total_precio = precio * cantidad
    totalx5 = precio * 5
    return Inventario(nombre, descripcion, clasificacion,
                      cantidad, precio, total_precio, totalx5)


def see_inventory(inventario):
    """Muestra el inventario"""
    encabezado = ["Nombre", "Descripción", "Clasificación",
                  "Cantidad", "Precio", "Precio total", "Precio x5 unidades"]
    print(
        f"{encabezado[0]:<15} {encabezado[1]:<25}"
        f"{encabezado[2]:<20} {encabezado[3]:<15}"
        f"{encabezado[4]:<10} {encabezado[5]:<15}"
        f"{encabezado[6]:<18}"
    )
    print("--------------------------------------------"
          "---------------------------------------------"
          "---------------------------------------------")
    # Muestra el inventario
    for producto in inventario:
        (
            nombre, descripcion, clasificacion,
            cantidad, precio, total_precio, totalx5
        ) = producto.show_inventory()
        print(
            f"{nombre:<15} {descripcion:<25}"
            f"{clasificacion:<20} {cantidad:<15}"
            f"{precio:<10} {total_precio:<15}"
            f"{totalx5:<18}")


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
        total_precio = sum(producto.precio for producto in producto)
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
