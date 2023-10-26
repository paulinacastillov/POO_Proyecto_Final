import tkinter as tk
from tkinter import messagebox as mssg

def obtener_dimensiones_pantalla():
    root = tk.Tk()
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()
    root.destroy()
    return ancho, alto

# # Hacer que solo pueda tener un guincito
# def id_valido(cadena):
#   #Verifica que el ID soolo contenga numeros o
#   for caracter in cadena:
#     if not caracter.isdigit(): #and caracter != '-':
#       return False
#   return True


# def id_valido(event):
#   """
#   Permite solo la entrada de números en el widget de entrada de texto y borra el último carácter ingresado si no es un número.

#   Args:
#     event: El evento de la tecla presionada.
#   """
#   cadena = self.idNit.get()
#   widget = event.widget
#   caracter = event.char

#   if not caracter.isdigit():
#     mssg.showerror('Atención!!',
#                        'El Id/Nit solo puede estar compuesto numeros.')
#     cadena = cadena[:14]
#     self.idNit.delete(0, "end")
#     self.idNit.insert("end", cadena)
   