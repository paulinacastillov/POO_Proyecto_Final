import tkinter as tk

def obtener_dimensiones_pantalla():
    root = tk.Tk()
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()
    root.destroy()
    return ancho, alto

print(obtener_dimensiones_pantalla())