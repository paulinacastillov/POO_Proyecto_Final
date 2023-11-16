# !/usr/bin/python3
# -*- coding: utf-8 -*-
#awa
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3
import os
from Funciones import *
import datetime


class Inventario:
  def __init__(self, master=None):

    self.path = os.path.abspath('')#r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
    self.db_name = self.path + r'/bases_de_datos/Inventario.db' # Toca conseguir una base de datos
    

    # Dimensiones de la pantalla
    # root = tk.Tk()
    # ancho=root.winfo_screenwidth()
    # alto=root.winfo_screenheight() 
    # root.destroy()
    ancho=700
    alto=800

    Inventario.actualiza = None

    # Crea ventana principal
    self.win = tk.Tk() 
    self.win.geometry(f"{int(ancho/30)}x{int(alto/30)}")
    self.win.iconbitmap(self.path + r'/imagenes/dt.ico')
    self.win.resizable(True, True)
    self.win.title("Manejo de Proveedores") 

    #Centra la pantalla
    self.centra(self.win,ancho,alto)

    # Contenedor de widgets   
    self.win = tk.LabelFrame(master)
    self.win.configure(background="#e0e0e0",font="{Arial} 12 {bold}",
                       height=ancho,labelanchor="n",width=alto)
    self.tabs = ttk.Notebook(self.win)
    self.tabs.configure(height=700, width=799)

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
    self.idNit.bind("<Return>", self.validaIdNit)
    #self.idNit.bind("<Key>",self.id_valido)
    #self.idNit.bind("<BackSpace>", lambda event: self.idNit.delete("end"))
    
    #Etiqueta razón social del Proveedor
    self.lblRazonSocial = ttk.Label(self.frm1)
    self.lblRazonSocial.configure(text='Razon social', width=12)
    self.lblRazonSocial.place(anchor="nw", x=210, y=40)

    #Captura razón social del Proveedor
    self.razonSocial = ttk.Entry(self.frm1)
    self.razonSocial.configure(width=36,state= 'disabled')
    self.razonSocial.place(anchor="nw", x=290, y=40)

    #Etiqueta ciudad del Proveedor
    self.lblCiudad = ttk.Label(self.frm1)
    self.lblCiudad.configure(text='Ciudad', width=7)
    self.lblCiudad.place(anchor="nw", x=540, y=40)

    #Captura ciudad del Proveedor
    self.ciudad = ttk.Entry(self.frm1)
    self.ciudad.configure(width=30,state= 'disabled')
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
    self.codigo.configure(width=13, state= 'disabled')
    self.codigo.place(anchor="nw", x=60, y=120)

    #Etiqueta descripción del Producto
    self.lblDescripcion = ttk.Label(self.frm1)
    self.lblDescripcion.configure(text='Descripción', width=11)
    self.lblDescripcion.place(anchor="nw", x=220, y=120)

    #Captura la descripción del Producto
    self.descripcion = ttk.Entry(self.frm1)
    self.descripcion.configure(width=36, state= 'disabled')
    self.descripcion.place(anchor="nw", x=290, y=120)

    #Etiqueta unidad o medida del Producto
    self.lblUnd = ttk.Label(self.frm1)
    self.lblUnd.configure(text='Unidad', width=7)
    self.lblUnd.place(anchor="nw", x=540, y=120)

    #Captura la unidad o medida del Producto
    self.unidad = ttk.Entry(self.frm1)
    self.unidad.configure(width=10, state= 'disabled')
    self.unidad.place(anchor="nw", x=590, y=120)

    #Etiqueta cantidad del Producto
    self.lblCantidad = ttk.Label(self.frm1)
    self.lblCantidad.configure(text='Cantidad', width=8)
    self.lblCantidad.place(anchor="nw", x=10, y=170)

    #Captura la cantidad del Producto
    self.cantidad = ttk.Entry(self.frm1)
    self.cantidad.configure(width=12,state= 'disabled')
    #self.cantidad.bind("<Key>", self.validaCantidad)
    self.cantidad.place(anchor="nw", x=70, y=170)

    #Etiqueta precio del Producto
    self.lblPrecio = ttk.Label(self.frm1)
    self.lblPrecio.configure(text='Precio $', width=8)
    self.lblPrecio.place(anchor="nw", x=170, y=170)

    #Captura el precio del Producto
    self.precio = ttk.Entry(self.frm1)
    self.precio.configure(width=15,state= 'disabled')
    self.precio.place(anchor="nw", x=220, y=170)

    #Etiqueta fecha de compra del Producto
    self.lblFecha = ttk.Label(self.frm1)
    self.lblFecha.configure(text='Fecha', width=6)
    self.lblFecha.place(anchor="nw", x=350, y=170)

    #Captura la fecha de compra del Producto
    self.fecha = ttk.Entry(self.frm1)
    self.fecha.configure(width=10,state= 'disabled')
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
    # Comentada para no mostrar los datos iniciales, esto los muestra
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
    self.frm2.configure(height=90, width=ancho)
   

    #Botón para Buscar un Proveedor
    self.btnBuscar = ttk.Button(self.frm2)
    self.btnBuscar.configure(text='Buscar', command=lambda: (self.buscarDB()))
    self.btnBuscar.pack(side="bottom")
    self.btnBuscar.place(anchor="nw", width=70, x=140, y=10)

    # Botón para Guardar los datos
    self.btnGrabar = ttk.Button(self.frm2)
    self.btnGrabar.configure(text='Grabar',command=lambda: (self.grabarDB()))
    self.btnGrabar.pack(side="bottom")
    self.btnGrabar.place(anchor="nw", width=70, x=210, y=10)

    # Botón para Editar los datos
    self.btnEditar = ttk.Button(self.frm2)
    self.btnEditar.configure(text='Editar', command= self.editaTP)
    self.btnEditar.pack(side="bottom")
    self.btnEditar.place(anchor="nw", width=70, x=280, y=10)

    # Botón para Eliminar datos
    self.btnEliminar = ttk.Button(self.frm2)
    self.btnEliminar.configure(text='Eliminar', command = self.eliminaRegistro)
    self.btnEliminar.pack(side="bottom")
    self.btnEliminar.place(anchor="nw", width=70, x=350, y=10)

    # Botón para cancelar una operación
    self.btnCancelar = ttk.Button(self.frm2)
    self.btnCancelar.configure(text='Cancelar', command=self.cancelar)
    self.btnCancelar.pack(side="bottom")
    self.btnCancelar.place(anchor="nw", width=70, x=420, y=10)
    
    #Ubicación del Frame 2
    self.frm2.place(anchor="nw", height=90, relwidth=1, y=635)
    self.win.pack(anchor="s",side="top")

    # widget Principal del sistema
    self.mainwindow = self.win

  #Fución de manejo de eventos del sistema
  def run(self):
      self.mainwindow.mainloop()

  ''' ......... Métodos utilitarios del sistema .............'''
  #Rutina de centrado de pantalla
  def centra(self,win,ancho,alto): 
      fraccion_pantalla = 2
      """ centra las ventanas en la pantalla """ 
      x = win.winfo_screenwidth() // fraccion_pantalla  - ancho // fraccion_pantalla 
      y = win.winfo_screenheight() // fraccion_pantalla - alto // fraccion_pantalla
      win.geometry(f'{ancho}x{alto}+{x}+{y}') 
      win.deiconify() # Se usa para restaurar la ventana

 # Validaciones del sistema
 # ver que hacer cuando se pase de los 15, borra los 15 pero el 16 lo deja ahí
 # Buscar como blanquear
  # Borra el último 

  def validaIdNit(self):
  #Valida que la longitud no sea mayor a 15 caracteres y que solo se inserten números. '''
    cadena = self.idNit.get()
    if len(cadena) > 14:
        self.idNit.delete(0, "end")  # Eliminar todo el contenido del campo
        mssg.showerror('Atención!!', 'El Id/NIT solo puede estar compuesto por 15 caracteres.')
    elif not cadena.isdigit() and cadena:
        # Buscar caracteres no válidos y eliminarlos
        for char in cadena:
            if not char.isdigit():
                cadena = cadena.replace(char, "")
        self.idNit.delete(0, "end")  # Eliminar todo el contenido del campo
        mssg.showerror('Atención!!', 'El Id/NIT solo puede estar compuesto por números')
    else: return True


# Hace falta conectarlo a los botones de busqueda o editar para que cuando se presionen
# Muestre error. Preguntar a Diego

# Este se puede usar para validad cantidad y precio porque basicamente es lo mismo, en caso contrario cambiar
# a funciones separadass pero no lo veo necesario por ahora. Charlar

#Validación de cantidad
  def validaCantidad(self):
    # Validar
    cadena = self.cantidad.get()
    try:
        valor = float(cadena)
        self.errorCampos=False
        # Validación exitosa, es un número double
    except ValueError:
        # Error, no es un número double
        mssg.showerror('Atención!!', 'La cantidad es inválida')
        self.errorCampos=True
        # Limpia el campo
        #self.cantidad.delete(0, "end")
    

#Validación de precio
  def validaPrecio(self):
    valor_original = self.precio.get()
    # Valida que sea un número double.
    cadena = self.precio.get()
    try:
        valor = float(cadena)
        self.errorCampos=False
        # Validación exitosa, es un número double
    except ValueError:
        # Error, no es un número double
        mssg.showerror('Atención!!', 'El precio es inválido')
        self.errorCampos=True
        #self.errorCampos=True
        # Limpia el campo
        #self.precio.delete(0, "end")
    

#Validar Unidad
  def validaUnidad(self):
    cadena = self.unidad.get()
    if not cadena.strip():  # Verifica si la cadena está vacía o compuesta solo por espacios en blanco
        mssg.showerror('Error', 'El campo de unidad no puede estar vacío o contener solo espacios en blanco')
        self.unidad.delete(0,"end")
        self.errorCampos=True
        #self.unidad.delete(0,"end")
    elif len(cadena) > 10:
        mssg.showerror('Error', 'El campo de unidad no puede superar los 10 caracteres')
        self.unidad.delete(0,"end")
        self.errorCampos=True
    else: 
      self.errorCampos=False

#Validar Descripción        
  def validaDescripcion(self):
    cadena = self.descripcion.get()
    if not cadena.strip():
        mssg.showerror('Error', 'El campo de descripción no puede estar vacío o contener solo espacios en blanco')
        self.errorCampos=True
        self.descripcion.delete(0,"end")
    else: 
      self.errorCampos=False
      

# #Valida Fecha
#colocar que fecha no mayor a hoy
  def validaFecha(self):
    fecha_str = self.fecha.get()
    
    # Verificar el formato de la fecha (dd-mm-aaa)
    fecha_parts = fecha_str.split('-')
    if len(fecha_parts) != 3:
        mssg.showerror("Error", "El formato de la fecha es incorrecto.")
        self.errorCampos=True
        return
    try:
        dia, mes, año = map(int, fecha_parts)

        if not (1 <= mes <= 12):
            mssg.showerror("Error", "La fecha es inválida. Mes fuera de rango")
            self.errorCampos=True
            return

        if mes in [4, 6, 9, 11]:
            max_dia = 30
        elif mes == 2:
            max_dia = 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28
        else:
            max_dia = 31

        if not (1 <= dia <= max_dia):
            mssg.showerror("Error", "La fecha es inválida. Día no corresponde al mes")
            self.errorCampos=True
    except ValueError:
        mssg.showerror("Error", "La fecha es inválida.")
        self.errorCampos=True
        
        
 # def validaFecha(self):
  #Valida que la longitud no sea mayor a 15 caracteres y que solo se inserten números. '''
  #  cadena = self.idNit.get()

   # if not datetime.datetime.strptime(cadena, "%d-%m-%y").is_valid():
    #   mssg.showerror('Atención!', 'La fecha debe tener formato dd/mm/aaaa además de ser valida')

 # def id_valido(self, event):
 #       ''' Valida que solo se inserten números en el campo y muestra un mensaje de alerta en caso de caracteres inválidos '''
 #       caracteres = self.idNit.get()
 #       if not caracteres.isdigit():
 #           mssg.showerror('Atención!!', 'El Id/NIT solo puede estar compuesto por números.')
 #           self.idNit.delete(0, "end")  # Eliminar todo el contenido
  

  #Rutina de limpieza de datos
  def limpiaCampos(self):
      ''' Limpia todos los campos de captura'''
      Inventario.actualiza = None
      self.idNit.config(state = 'normal')
      self.idNit.delete(0,'end')
      self.razonSocial.delete(0,'end')
      self.ciudad.delete(0,'end')
      self.codigo.delete(0,'end')
      self.descripcion.delete(0,'end')
      self.unidad.delete(0,'end')
      self.cantidad.delete(0,'end')
      self.precio.delete(0,'end')
      self.fecha.delete(0,'end')

  def limpiaProveedor(self):
    '''Limpia campos del proveedor'''
    self.razonSocial.delete(0,'end')
    self.ciudad.delete(0,'end')
    
  def limpiaProductos(self):
    '''Limpia campos de Productos'''
    self.codigo.delete(0,'end')
    self.descripcion.delete(0,'end')
    self.unidad.delete(0,'end')
    self.cantidad.delete(0,'end')
    self.precio.delete(0,'end')
    self.fecha.delete(0,'end')

  def habilitaProductos(self):
    '''Habilita los campos para crear productos'''
    self.codigo.configure(state='normal')
    self.descripcion.configure(state='normal')
    self.unidad.configure(state='normal')
    self.cantidad.configure(state='normal')
    self.precio.configure(state='normal')
    self.fecha.configure(state='normal')
    
  def habilitaProveedor(self):
    self.razonSocial.configure(state='normal')
    self.ciudad.configure(state='normal')  
    
  def deshabilitaProductos(self):
    self.razonSocial.configure(state='disabled')
    self.ciudad.configure(state='disabled')
    self.codigo.configure(state='disabled')
    self.descripcion.configure(state='disabled')
    self.unidad.configure(state='disabled')
    self.cantidad.configure(state='disabled')
    self.precio.configure(state='disabled')
    self.fecha.configure(state='disabled')

  def deshabilitaProveedor(self):
    self.idNit.configure('disabled')
    self.razonSocial.configure('disabled')
    self.ciudad.configure('disabled')
    
  def capturaComparacion(self):
    self.comparaRazonSocial = self.razonSocial.get()
    self.comparaCiudad = self.ciudad.get()
    
    self.comparaDescripcion = self.descripcion.get()
    self.comparaCantidad = self.cantidad.get()
    self.comparaFecha = self.fecha.get()
    self.comparaIdNit = self.idNit.get()
    self.comparaPrecio = self.precio.get()  
    self.comparaUnidad = self.unidad.get()
    
  # Operaciones con la base de datos
  def run_Query(self, query, parametros = ()):
    
  
    ''' Función para ejecutar los Querys a la base de datos '''
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parametros)
        conn.commit()
    return result
  #Valida si el Proveedor existe 
  def valEx_idNitProv(self,busqueda):
    '''Revision si el idNitProv Insertado existe en la tabla proveedores, requiere el valor a buscar'''
    query = '''SELECT idNitProv from Proveedores'''
    column = self.run_Query(query)
    busca = []
    for db_column in column:
      busca.append(db_column[0])
    i = busca.count(busqueda)
    if(i==0):
      return False
    else :
      return True
  #Valida si existen productos de un proveedor dado
  def valEx_idNit(self,busqueda):
    '''Revision si el idNit Insertado existe en la tabla proveedores, requiere el valor a buscar'''
    query = '''SELECT idNit from Productos'''
    column = self.run_Query(query)
    busca = []
    for db_column in column:
      busca.append(db_column[0])
    i = busca.count(busqueda)
    if(i==0):
      return False
    else :
      return True
 
 
 
#Funciones validacion
  def cambioProveedores(self):
    '''Valida los cambios en los campos del Proveedor, si hay cambios retorna False'''
    if(self.comparaRazonSocial!=self.razonSocial.get()):
      print('cambio en razon social')
      return False
    elif(self.comparaCiudad!=self.ciudad.get()):
      print('cambio en ciudad')
      return False
   
  def cambioProductos(self):
    '''Valida los cambios en los campos del Producto, si hay cambios retorna False'''
    if(self.comparaDescripcion!=self.descripcion.get()):
      return False
    elif(self.comparaUnidad!=self.unidad.get()):
      return False
    elif(self.comparaCantidad!=self.cantidad.get()):
      return False
    elif(self.comparaPrecio!=self.precio.get()):
      return False
    elif(self.comparaFecha!=self.fecha.get()):
      return False     

  def actualiza_Proveedor(self):
    query = '''UPDATE Proveedores SET Razon_Social = ?, Ciudad = ? WHERE idNitProv = ?'''
    param = [self.razonSocial.get(),self.ciudad.get(),self.idNit.get()]
    self.run_Query(query,param)
  
  def nuevo_Proveedor(self):
    query = '''INSERT INTO Proveedores VALUES(?,?,?) '''
    param = [self.idNit.get(),self.razonSocial.get(),self.ciudad.get()]
    self.run_Query(query,param)
 
  def actualiza_Producto(self):
    query= '''UPDATE Productos SET Descripcion = ?, Und = ?, Cantidad = ?, Precio = ?, Fecha = ? WHERE Codigo = ?'''
    param= [self.descripcion.get(),self.unidad.get(),self.cantidad.get(),self.precio.get(),self.fecha.get(),self.codigo.get()]
    self.run_Query(query,param) 
  
  def nuevo_Producto(self):
    query = '''INSERT INTO Productos VALUES(?,?,?,?,?,?,?)'''
    param= [self.idNit.get(),self.codigo.get(),self.descripcion.get(),self.unidad.get(),self.cantidad.get(),self.precio.get(),self.fecha.get()]
    self.run_Query(query,param) 
  
  def actualizaTreeview(self):
    tabla_TreeView = self.treeProductos.get_children()
    for linea in tabla_TreeView:
      self.treeProductos.delete(linea) # Límpia la filas del TreeView
    query2 = '''SELECT * from Productos WHERE idNit = ? '''
    #Rellena casillas de Productos
    db_rows = self.run_Query(query2,[self.param])
    for row in db_rows:
      self.treeProductos.insert('',0, text = row[0], values = [row[1],row[2],row[3],row[4],row[5],row[6]])
      # El for ubica los valores del query en el treeview(GUI)
    
  # Funciones de botones
#Boton cancelar
  def cancelar(self):
    self.idNit.configure(state='normal')  
    self.codigo.configure(state='normal')
    self.habilitaProveedor()
    self.limpiaProveedor()
    tabla_TreeView = self.treeProductos.get_children()
    for linea in tabla_TreeView:
        self.treeProductos.delete(linea) # Límpia la filas del TreeView
    self.limpiaCampos()
    self.deshabilitaProductos()
       
#Boton grabar 
  def grabarDB(self):
    '''Graba lo que se a cambiado en la interface '''  
    #Proveedores--------------
    if(self.cambioProveedores()==False):
      if(mssg.askyesno(title='Grabar', message='Se realizaron cambios en el Proveedor, desea continuar?')==True):
        #Nuevo proveedor
        if(self.nuevoProveedor==True):
          self.nuevo_Proveedor()
          mssg.showinfo(title='Sucsess',message='Se creo el nuevo proveedor correctamente') 
          self.nuevoProveedor == False
          self.capturaComparacion()
          self.codigo.configure(state='disabled')
        else:
        #Proveedor ya existente
          self.actualiza_Proveedor()
          mssg.showinfo(title='Sucsess',message='Se actualizo la informacion del Proveedor correctamente')
          self.capturaComparacion()
      else:
      #No desea continuar con los cambios
        self.limpiaProveedor()
    else: print('cambio proveedores true')
    
    #Productos--------------
    if(len(self.codigo.get())!=0):
      #Validaciones de Campos Productos
      self.validaCantidad()
      self.validaPrecio()
      self.validaUnidad()
      self.validaDescripcion()
      self.validaFecha()  
      if(self.errorCampos==False):        
        if(self.cambioProductos()==False):
          if(mssg.askyesno(title='Grabar', message='Se realizaron cambios en el Producto, desea continuar?')==True): 
            if(self.nuevoProducto==True):
              self.nuevo_Producto()
              mssg.showinfo(title='Succes!',message='Se creo el nuevo producto correctamente')
              self.nuevoProducto==False
              self.actualizaTreeview()
            else: 
              self.actualiza_Producto()
              mssg.showinfo(title='Sucsess',message='Se actualizo la informacion del Producto correctamente')
              self.actualizaTreeview()
          else:
            self.limpiaProductos()
      else:   
        mssg.showerror(title='Error',message='No se realizo el guardado de datos') 
    print('espacio codigo = 0')
#Boton editar
  def editaTP(self):
    ''' Edita una tupla del TreeView despues de seleccionarla'''
    #Para revisar si esta vacio el campo en grabar
    self.emptyidNit = self.idNit.get()
    self.emptyCodigo = self.codigo.get()
    self.codigo.configure(state='normal')
    self.limpiaProductos()
    self.codigo.configure(state='disabled')
    
    
    if(mssg.askyesno(message='Desea editar el Proveedor?')==True):
      self.editaProveedor= True
    else:
      self.editaProveedor= False
      self.deshabilitaProductos()
      

    if(self.editaProveedor == True):
      self.habilitaProveedor() 
      self.idNit.configure(state = 'readonly')   
      
    seleccion = self.treeProductos.focus()
    self.values =self.treeProductos.item(seleccion)["values"]
    print(len(seleccion))
    
    if(len(seleccion)!=0):
      if(mssg.askyesno(message='Desea editar el producto?')==True):
        self.editaProducto = True
      else:
        self.editaProducto=False
        self.deshabilitaProductos()
    else:
      self.editaProducto= False
      
      
    if(self.editaProducto==True):
      self.habilitaProductos()
      self.codigo.insert(0,self.values[0])
      self.descripcion.insert(0,self.values[1]) 
      self.unidad.insert(0,self.values[2])
      self.cantidad.insert(0,self.values[3])
      self.precio.insert(0,self.values[4])
      self.fecha.insert(0,self.values[5])
      self.codigo.configure(state='disabled')
      self.nuevoProducto = False
    elif(mssg.askyesno(message='Desea Agregar un producto?')==True):
      self.habilitaProductos()
      self.nuevoProducto = True
      
    self.capturaComparacion()



#Boton eliminar
#Boton eliminar
 # Falta poner la ventana bonita, que esta se cierre con cancelar 
 # y cuando se cierre el programa,ademas poner el mensaje de error si no se ha puesto o seleccionado un producto o provedor.
  #  pass

  def eliminaRegistro(self, event=None):

    self.ventana1 = tk.Tk()
    self.seleccion = tk.IntVar(self.ventana1, 2)
    ancho_ventana = 300  # Ancho en píxeles
    alto_ventana = 300   # Alto en píxeles
    self.ventana1.geometry(f"{ancho_ventana}x{alto_ventana}")

    self.radio1 = tk.Radiobutton(self.ventana1, text="Proveedor", variable=self.seleccion, value=1)
    self.radio1.grid(column=0, row=0)
    self.radio2 = tk.Radiobutton(self.ventana1, text="Producto", variable=self.seleccion, value=2)
    self.radio2.grid(column=0, row=1)
    self.boton1 = tk.Button(self.ventana1, text="Eliminar", command=self.borrar)
    self.boton1.grid(column=0, row=2)
    self.label1 = tk.Label(self.ventana1, text="Opción seleccionada: ")
    self.label1.grid(column=0, row=3)

  def borrar(self):

    id_nit = self.idNit.get()
    if not id_nit:
        mssg.showerror('Error', 'Debes ingresar un ID/NIT de proveedor para eliminar.')
        return

    if (self.seleccion.get() == 1):


        query_proveedor = "DELETE FROM Proveedores WHERE idNitProv = ?"
        self.run_Query(query_proveedor, (id_nit,))
        query_productos = "DELETE FROM Productos WHERE idNit = ?"
        self.run_Query(query_productos, (id_nit,))
        self.limpiaCampos()
        self.deshabilitaProductos()
        self.treeProductos.delete(*self.treeProductos.get_children())
        mssg.showinfo('Éxito', 'El proveedor y sus productos se han eliminado con éxito.')


    id_cod = self.codigo.get()
    if not id_cod:
        mssg.showerror('Error', 'Debes ingresar un codigo de proveedor para eliminar.')
        return

    if (self.seleccion.get() == 2):
        query_productos2 = "DELETE FROM Productos WHERE Codigo = ?"
        self.treeProductos.delete(*self.treeProductos.get_children())
        self.run_Query(query_productos2, (id_cod,))
        mssg.showinfo('Éxito', 'Los productos del proveedor se han eliminado con éxito.')
  
  
# #Voy a intentar crear una ventana para que se diga que quiere editar si PROVEEDOR PRODUCTO o PRODUCTO NUEVO 
#  def editar(self):
#    self.ventana2= tk.Tk()
#    self.ventana2.geometry(f"{200}x{200}")
#    
#    self.btnGrabar = ttk.Button(self.frm2)
#    self.btnGrabar.configure(text='Grabar',command=lambda: (self.grabarDB()))
#    self.btnGrabar.pack(side="bottom")
#    self.btnGrabar.place(anchor="nw", width=70, x=210, y=10)
#    
#    self.btnProv = ttk.Button(self.frm2)
#    self.btnProv.configure(text='Proveedor')
#    self.btnProv.pack(side="bottom")
#    self.btnProv.place(anchor="nw", width=70, x=210, y=10)
#    
#    self.btnProd = ttk.Button(self.frm2)
#    self.btnProvNue=ttk.Button(self.frm2)
      
  
  
  
  
  #Boton buscar  
  def buscarDB(self): 
    '''Consulta con Id o Nit del proveedor'''
    #valida el idNit
    if(self.validaIdNit()==True):
      #Trae DB al treeview
      tabla_TreeView = self.treeProductos.get_children()
      for linea in tabla_TreeView:
          self.treeProductos.delete(linea) # Límpia la filas del TreeView   
      self.param = self.idNit.get()    
      if(len(self.idNit.get())!=0):
        if(self.valEx_idNitProv(self.param) == True):  
          #Seleccionando los datos de la BD
          query1 = '''SELECT * from Proveedores WHERE idNitProv = ? ''' 
          #Rellena casillas de proveedor
          db_rows = self.run_Query(query1,[self.param])
          for row in db_rows:
            pass
          self.idNit.configure(state='disabled')
          self.razonSocial.configure(state='normal')
          self.ciudad.configure(state='normal')
          self.limpiaProveedor()
          self.razonSocial.insert(0,row[1])
          self.ciudad.insert(0,row[2])
          self.razonSocial.configure(state='disabled')
          self.ciudad.configure(state='disabled')
          self.nuevoProveedor = False 
          
          if(self.valEx_idNit(self.param) == True):
            query2 = '''SELECT * from Productos WHERE idNit = ? '''
            #Rellena casillas de Productos
            db_rows = self.run_Query(query2,[self.param])
            for row in db_rows:
              self.treeProductos.insert('',0, text = row[0], values = [row[1],row[2],row[3],row[4],row[5],row[6]])
            # El for ubica los valores del query en el treeview(GUI)
          else:
            
            if(mssg.askyesno(title="Error", message="No existen productos para este proveedor, desea crear uno?") == True ):
              self.nuevoProducto = True
              self.habilitaProductos()
              self.comparaDescripcion = 0
              self.comparaUnidad = 0
              self.comparaCantidad = 0
              self.comparaPrecio = 0
              self.comparaFecha = 0
            else:
              self.nuevoProducto = False    
        else:
          if(mssg.askyesno(title="Error", message="No existe el proveedor, desea crear uno?")== True):
            self.habilitaProveedor()
            self.comparaIdNit=self.idNit.get()
            self.nuevoProveedor = True     
            #Toma valores para comparar cambios   
            self.comparaRazonSocial = 0
            self.comparaCiudad = 0      
          else:
            self.idNit.delete(0,'end')
      else:
        mssg.showerror(title="Error",message="No hay IdNit para buscar")
    else:
      self.emptyCodigo = self.codigo.get()
   
    
if __name__ == "__main__":
    app = Inventario()
    app.run()
