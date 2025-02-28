#!/usr/bin/env python3

"""
Título de práctica: Inventario tienda 1

Descripción extendida del programa

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-02-27
"""

class inventario: 
    """Clase que representa el inventario de una tienda"""
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    #muestra los productos seleccionados
    def show_inventory(self):
        return f"{self.nombre:<12}" f"{self.cantidad:<8}" f"{self.precio:<8}"

def add_product():
    """Agrega un producto al inventario"""
    nombre = input("Nombre del producto: ")
    cantidad = int(input(f"Cantidad del producto {nombre}: "))
    precio = int(input(f"Precio del unitario del producto {nombre}: "))
    return inventario(nombre, cantidad, precio)

def see_inventory(inventario):
    """Muestra el inventario"""
    print ("\n Nombre Cantidad Precio")
    print("-----------------------")
    #Muestra el inventario
    for producto in inventario:
        print(producto.show_inventory())

def main():
    productos = []
    # Pedimos los datos para añadir los productos
    for i in range(3):
        print(f"\n {i+1} Producto:")
        producto = add_product()
        productos.append(producto)
    #muestra el inventario en forma de tabla
    print("\nDatos de los productos ingresados:")
    see_inventory(productos)
         
if __name__ == "__main__":
    main()
