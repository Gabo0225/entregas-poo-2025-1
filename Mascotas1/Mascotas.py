#!/usr/bin/env python3

"""
Título de práctica: Ingreso Mascotas 1

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-03-30
"""

from datetime import datetime

class Mascota:
    """Mascotas que ingresan a una veterinaria"""
    def __init__(self, Nombre, Edad, Raza):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Raza = Raza
        self.FechaIN = datetime.now().isoformat()

    def mostrar_datos (self):
        return [
            self.Nombre,
            f'{self.Edad} años',
            self.Raza,
            self.FechaIN,
        ]


class Perro(Mascota):
    clase = "perro"

class Gato(Mascota):
    clase = "gato"


def info_mascotas():
    """Agrega una mascota"""
    mascotas = []
    cantidad = int(input("¿Cuantas mascotas vas a ingresar? "))
    for i in range (1, cantidad + 1):
        TipoMascota = input(f"Mascota {i}, "
                            "¿Es perro o gato?").strip().lower()
        while TipoMascota not in ['perro', 'gato']:
            TipoMascota = input("Opcion no valida, "
                                "ingrese, que tipo de mascota "
                                f"es Mascota {i}, ¿Es perro o gato? ")
        Nombre = input(f"¿Cúal es el nombre del {TipoMascota}?: ")
        Edad = int(input(f"¿Que edad tiene {Nombre}?: "))
        Raza = input(f"Que raza es {Nombre}?: ")
        mascota = (
        Perro(Nombre, Edad, Raza) if TipoMascota == 'perro'
        else Gato(Nombre, Edad, Raza))
        mascotas.append(mascota)
    return mascotas


def Mostrar(mascotas):
    """Muestra las mascotas ingresadas"""
    encabezado = ["Clase", "Nombre", "Edad", "Fecha ingreso"]
    print(
        f"{encabezado [0]:<8} {encabezado [1]:<12}"
        f"{encabezado [2]:<8} {encabezado [3]:<25}"
    )
    for mascota in mascotas:
        (
            Clase, Nombre, Raza, FechaIN
        ) = mascota.mostrar_datos()
        print (
            f"{Clase:<8} {Nombre:<12}"
            f"{Raza:<8} {FechaIN:<25}"
        )


if __name__ == "__main__":
    mascotas = info_mascotas()
    Mostrar(mascotas)