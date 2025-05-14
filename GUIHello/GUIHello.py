from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class principal:
    def __init__ (self):
        self.root = Tk()
        self.root.title("Mi primera ventana")
        self.root.geometry("300x300")
        self.root.configure(bg="#4fdee7")
        
        # Insertar imagen
        self.gif = Image.open("Saludo.gif")
        self.frames = []
        try:
            while True:
                frame = ImageTk.PhotoImage(self.gif.copy())
                self.frames.append(frame)
                self.gif.seek(len(self.frames))
        except EOFError:
            pass 
        
        self.current_frame = 0
        
        # Creacion de widgets
        self.mensaje = Label(self.root, text="Ingresa tu nombre", bg="#4fdee7")
        self.entrada = Entry(self.root)
        self.bot = Button(self.root, text="¿Quieres un Saludo?", command=self.button_clicked)
        self.boton = Button(self.root, text="Cerrar", bg="red", command=self.root.quit)
        self.imagen_label = Label(self.root)
        
        
        # Llamado a la ventana 
        self.mensaje.pack(pady=5)        
        self.entrada.pack(pady= (0,10))        
        self.bot.pack()        
        self.boton.pack(pady=(10,0))
        self.imagen_label = Label(self.root)
        self.vistaImagen = False
        
        
        #Funcion saludo
    def button_clicked(self):
        nombre = self.entrada.get()
        messagebox.showinfo("ventana", f"Hola mi rey ({nombre})")
        self.imagen_label.pack(pady=10)
        self.animate_gif()
        
        
    def animate_gif(self):
        frame = self.frames[self.current_frame]
        self.imagen_label.config(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.root.after(100, self.animate_gif)
            
p=principal()
p.root.mainloop()