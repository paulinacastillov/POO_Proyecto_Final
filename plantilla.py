# !/usr/bin/python3
# -*- coding: utf-8 -*-
#owo
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
import os


class Inventario:
  def __init__(self, master=None):

    self.path = os.path.abspath('')#r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
    self.db_name = self.path + r'/Inventario.db' # Toca conseguir una base de datos
    ancho=830;alto=840 # Dimensione de la pantalla
    actualiza = None

    # Crea ventana principal
    self.win = tk.Tk() 
    self.win.geometry(f"{ancho}x{alto}")
    self.win.iconbitmap("dt.ico")
    self.win.resizable(False, False)
    self.win.title("Manejo de Proveedores") 

    #Centra la pantalla
    self.centra(self.win,ancho,alto)

    # Contenedor de widgets   
    self.win = tk.LabelFrame(master)
    self.win.configure(background="#e0e0e0",font="{Arial} 12 {bold}",
                       height=ancho,labelanchor="n",width=alto)
    self.tabs = ttk.Notebook(self.win)
    self.tabs.configure(height=800, width=799)

    #Frame de datos
    self.frm1 = ttk.Frame(self.tabs)
    self.frm1.configure(height=200, width=200)

    #Etiqueta IdNit del Proveedor
    self.lblIdNit = ttk.Label(self.frm1)
    self.lblIdNit.configure(text='Id/Nit', width=6)
    self.lblIdNit.place(anchor="nw", x=10, y=40)

    #Captura IdNit del Proveedor
    self.idNit = ttk.Entry(self.frm1)
    self.idNit.configure(takefocus=True)
    self.idNit.place(anchor="nw", x=50, y=40)
    self.idNit.bind("<Key>", self.validaIdNit)
    self.idNit.bind("<BackSpace>", lambda _:self.idNit.delete(len(self.idNit.get())),'end')

    #Etiqueta razón social del Proveedor
    self.lblRazonSocial = ttk.Label(self.frm1)
    self.lblRazonSocial.configure(text='Razon social', width=12)
    self.lblRazonSocial.place(anchor="nw", x=210, y=40)

    #Captura razón social del Proveedor
    self.razonSocial = ttk.Entry(self.frm1)
    self.razonSocial.configure(width=36)
    self.razonSocial.place(anchor="nw", x=290, y=40)

    #Etiqueta ciudad del Proveedor
    self.lblCiudad = ttk.Label(self.frm1)
    self.lblCiudad.configure(text='Ciudad', width=7)
    self.lblCiudad.place(anchor="nw", x=540, y=40)

    #Captura ciudad del Proveedor
    self.ciudad = ttk.Entry(self.frm1)
    self.ciudad.configure(width=30)
    self.ciudad.place(anchor="nw", x=590, y=40)

    #Separador
    self.separador1 = ttk.Separator(self.frm1)
    self.separador1.configure(orient="horizontal")
    self.separador1.place(anchor="nw", width=800, x=0, y=79)

    #Etiqueta Código del Producto
    self.lblCodigo = ttk.Label(self.frm1)
    self.lblCodigo.configure(text='Código', width=7)
    self.lblCodigo.place(anchor="nw", x=10, y=120)

    #Captura el código del Producto
    self.codigo = ttk.Entry(self.frm1)
    self.codigo.configure(width=13)
    self.codigo.place(anchor="nw", x=60, y=120)

    #Etiqueta descripción del Producto
    self.lblDescripcion = ttk.Label(self.frm1)
    self.lblDescripcion.configure(text='Descripción', width=11)
    self.lblDescripcion.place(anchor="nw", x=220, y=120)

    #Captura la descripción del Producto
    self.descripcion = ttk.Entry(self.frm1)
    self.descripcion.configure(width=36)
    self.descripcion.place(anchor="nw", x=290, y=120)

    #Etiqueta unidad o medida del Producto
    self.lblUnd = ttk.Label(self.frm1)
    self.lblUnd.configure(text='Unidad', width=7)
    self.lblUnd.place(anchor="nw", x=540, y=120)

    #Captura la unidad o medida del Producto
    self.unidad = ttk.Entry(self.frm1)
    self.unidad.configure(width=10)
    self.unidad.place(anchor="nw", x=590, y=120)

    #Etiqueta cantidad del Producto
    self.lblCantidad = ttk.Label(self.frm1)
    self.lblCantidad.configure(text='Cantidad', width=8)
    self.lblCantidad.place(anchor="nw", x=10, y=170)

    #Captura la cantidad del Producto
    self.cantidad = ttk.Entry(self.frm1)
    self.cantidad.configure(width=12)
    self.cantidad.place(anchor="nw", x=70, y=170)

    #Etiqueta precio del Producto
    self.lblPrecio = ttk.Label(self.frm1)
    self.lblPrecio.configure(text='Precio $', width=8)
    self.lblPrecio.place(anchor="nw", x=170, y=170)

    #Captura el precio del Producto
    self.precio = ttk.Entry(self.frm1)
    self.precio.configure(width=15)
    self.precio.place(anchor="nw", x=220, y=170)

    #Etiqueta fecha de compra del Producto
    self.lblFecha = ttk.Label(self.frm1)
    self.lblFecha.configure(text='Fecha', width=6)
    self.lblFecha.place(anchor="nw", x=350, y=170)

    #Captura la fecha de compra del Producto
    self.fecha = ttk.Entry(self.frm1)
    self.fecha.configure(width=10)
    self.fecha.place(anchor="nw", x=390, y=170)

    #Separador
    self.separador2 = ttk.Separator(self.frm1)
    self.separador2.configure(orient="horizontal")
    self.separador2.place(anchor="nw", width=800, x=0, y=220)


    #tablaTreeView
    self.style=ttk.Style()
    self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background="#e0e0e0", font=('Calibri Light',10))
    self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
    self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])
    
    #Árbol para mosrtar los datos de la B.D.
    self.treeProductos = ttk.Treeview(self.frm1, style="estilo.Treeview")
    
    self.treeProductos.configure(selectmode="extended")

    # Etiquetas de las columnas para el TreeView
    self.treeProductos["columns"]=("Codigo","Descripcion","Und","Cantidad","Precio","Fecha")
    # Características de las columnas del árbol
    self.treeProductos.column ("#0",          anchor="w",stretch=True,width=3)
    self.treeProductos.column ("Codigo",      anchor="w",stretch=True,width=3)
    self.treeProductos.column ("Descripcion", anchor="w",stretch=True,width=150)
    self.treeProductos.column ("Und",         anchor="w",stretch=True,width=3)
    self.treeProductos.column ("Cantidad",    anchor="w",stretch=True,width=3)
    self.treeProductos.column ("Precio",      anchor="w",stretch=True,width=8)
    self.treeProductos.column ("Fecha",       anchor="w",stretch=True,width=3)

    # Etiquetas de columnas con los nombres que se mostrarán por cada columna
    self.treeProductos.heading("#0",          anchor="center", text='ID / Nit')
    self.treeProductos.heading("Codigo",      anchor="center", text='Código')
    self.treeProductos.heading("Descripcion", anchor="center", text='Descripción')
    self.treeProductos.heading("Und",         anchor="center", text='Unidad')
    self.treeProductos.heading("Cantidad",    anchor="center", text='Cantidad')
    self.treeProductos.heading("Precio",      anchor="center", text='Precio')
    self.treeProductos.heading("Fecha",       anchor="center", text='Fecha')

    #Carga los datos en treeProductos
    # Comentada para no mostrar los datos iniciales
    self.lee_treeProductos() 
    self.treeProductos.place(anchor="nw", height=560, width=790, x=2, y=230)

    #Scrollbar en el eje Y de treeProductos
    self.scrollbary=ttk.Scrollbar(self.treeProductos, orient='vertical', command=self.treeProductos.yview)
    self.treeProductos.configure(yscroll=self.scrollbary.set)
    self.scrollbary.place(x=778, y=25, height=478)

    # Título de la pestaña Ingreso de Datos
    self.frm1.pack(side="top")
    self.tabs.add(self.frm1, compound="center", text='Ingreso de datos')
    self.tabs.pack(side="top")

    #Frame 2 para contener los botones
    self.frm2 = ttk.Frame(self.win)
    self.frm2.configure(height=60, width=800)
   

    #Botón para Buscar un Proveedor
    self.btnBuscar = ttk.Button(self.frm2)
    self.btnBuscar.configure(text='Buscar', command=self.consultarDB)
    self.btnBuscar.pack(side="left", padx=10, fill="x", expand=True)

    # Botón para Guardar los datos
    self.btnGrabar = ttk.Button(self.frm2)
    self.btnGrabar.configure(text='Grabar', command=self.adiciona_Registro)
    self.btnGrabar.pack(side="left", padx=10, fill="x", expand=True)

    # Botón para Editar los datos
    self.btnEditar = ttk.Button(self.frm2)
    self.btnEditar.configure(text='Editar', command=self.editaTreeProveedores)
    self.btnEditar.pack(side="left", padx=10, fill="x", expand=True)

    # Botón para Eliminar datos
    self.btnEliminar = ttk.Button(self.frm2)
    self.btnEliminar.configure(text='Eliminar', command=self.eliminaRegistro)
    self.btnEliminar.pack(side="left", padx=10, fill="x", expand=True)

    # Botón para cancelar una operación
    self.btnCancelar = ttk.Button(self.frm2)
    self.btnCancelar.configure(text='Cancelar', command=self.limpiaCampos)
    self.btnCancelar.pack(side="left", padx=10, fill="x", expand=True)

    #Ubicación del Frame 2
    self.frm2.place(anchor="nw", height=60, relwidth=1, y=680)
    self.win.pack(anchor="center",side="top")

    # widget Principal del sistema
    self.mainwindow = self.win

  #Fución de manejo de eventos del sistema
  def run(self):
      self.mainwindow.mainloop()



  ''' ......... Métodos utilitarios del sistema .............'''
  #Rutina de centrado de pantalla
  def centra(self,win,ancho,alto): 
      fraccion_pantalla = 8
      """ centra las ventanas en la pantalla """ 
      x = win.winfo_screenwidth() // fraccion_pantalla  - ancho // fraccion_pantalla 
      y = win.winfo_screenheight() // fraccion_pantalla - alto // fraccion_pantalla
      win.geometry(f'{ancho}x{alto}+{x}+{y}') 
      win.deiconify() # Se usa para restaurar la ventana

 # Validaciones del sistema
  def validaIdNit(self, event):
    ''' Valida que la longitud no sea mayor a 15 caracteres'''
    if event.char:
      if len(self.idNit.get()) >= 15:
         mssg.showerror('Atención!!','.. ¡Máximo 15 caracteres! ..')
    else:
        self.idNit.delete(14)

  #Rutina de limpieza de datos
  def limpiaCampos(self):
      ''' Limpia todos los campos de captura'''
      Inventario.actualiza = None
      self.idNit.config(state = 'normal')
      self.idNit.delete(0,'end')
      self.razonSocial.delete(0,'end')
      self.ciudad.delete(0,'end')
      self.idNit.delete(0,'end')
      self.codigo.delete(0,'end')
      self.descripcion.delete(0,'end')
      self.unidad.delete(0,'end')
      self.cantidad.delete(0,'end')
      self.precio.delete(0,'end')
      self.fecha.delete(0,'end')
 
  #Rutina para cargar los datos en el árbol  
  def carga_Datos(self):
    self.idNit.insert(0,self.treeProductos.item(self.treeProductos.selection())['text'])
    self.idNit.configure(state = 'readonly')
    self.razonSocial.insert(0,self.treeProductos.item(self.treeProductos.selection())['values'][0])
    self.unidad.insert(0,self.treeProductos.item(self.treeProductos.selection())['values'][3])

  # Operaciones con la base de datos
  def run_Query(self, query, parametros =()): 
    ''' Función para ejecutar los Querys a la base de datos '''
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parametros)
        conn.commit()
    return result

  def lee_treeProductos(self):
    ''' Carga los datos y Limpia la Tabla tablaTreeView '''
    tabla_TreeView = self.treeProductos.get_children()
    for linea in tabla_TreeView:
        self.treeProductos.delete(linea) # Límpia la filas del TreeView
    
    #Seleccionando los datos de la BD
    query = '''SELECT * from Proveedores INNER JOIN Productos WHERE idNitProv = idNit ORDER BY idNitProv'''
    db_rows = self.run_Query(query) # db_rows contine la vista del query
      
    # Insertando los datos de la BD en treeProductos de la pantalla
    for row in db_rows:
      self.treeProductos.insert('',0, text = row[0], values = [row[4],row[5],row[6],row[7],row[8],row[9]])

    ''' Al final del for row queda con la última tupla
        y se usan para cargar las variables de captura
    '''
    self.idNit.insert(0,row[0])
    self.razonSocial.insert(0,row[1])
    self.ciudad.insert(0,row[2])
    self.codigo.insert(0,row[3])
    self.descripcion.insert(0,row[4])
    self.unidad.insert(0,row[5])
    self.cantidad.insert(0,row[6])
    self.precio.insert(0,row[7])
    self.fecha.insert(0,row[8])  
          
  # Crear Código que haga estas caracteristicas
  def adiciona_Registro(self, event=None):
    '''Adiciona un producto a la BD si la validación es True'''
    pass

  def editaTreeProveedores(self, event=None):
    ''' Edita una tupla del TreeView'''
    pass
      
  def eliminaRegistro(self, event=None):
    '''Elimina un Registro en la BD'''
    pass
  
  def consultarDB(self):
    '''Consulta con Id o Nit del proveedor'''
  #  self.limpiaCampos()
  #  query = '''SELECT * FROM Proveedores WHERE idNitProv = ?'''
  #  self.run_Query(query,[self.idNit.get()])
  #  self.lee_treeProductos()
  #  self.carga_Datos()
    pass
  

if __name__ == "__main__":
    app = Inventario()
    app.run()
