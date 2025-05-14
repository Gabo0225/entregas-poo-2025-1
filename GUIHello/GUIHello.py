#!/usr/bin/env python3

"""
Título de práctica: Saludo en GUI

Autor: Gabriel Santamaria <gabrielsaher@hotmail.com>
Fecha: 2025-05-13
"""

from tkinter import *
from tkinter import messagebox


class principal:
    def __init__(self):
        self.root = Tk()
        self.root.title("Mi primera ventana")
        self.root.geometry("300x300")
        self.root.configure(bg="#4fdee7")

        # Creacion de widgets
        self.mensaje = Label(self.root, text="Ingresa tu nombre", bg="#4fdee7")
        self.entrada = Entry(self.root)
        self.bot = Button(self.root, text="¿Quieres un Saludo?",
                          command=self.button_clicked)
        self.boton = Button(self.root, text="Cerrar", bg="red",
                            command=self.root.quit)
        self.imagen_label = Label(self.root)

        # Llamado a la ventana
        self.mensaje.pack(pady=5)
        self.entrada.pack(pady=(0, 10))
        self.bot.pack()
        self.boton.pack(pady=(10, 0))

        # Funcion saludo
    def button_clicked(self):
        nombre = self.entrada.get()
        messagebox.showinfo("ventana", f"Hola mi rey ({nombre})")


p = principal()
p.root.mainloop()
