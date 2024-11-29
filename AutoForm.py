import tkinter as tk
from tkinter import ttk

# permite mostrar alertas en tkinter
from tkinter import messagebox as mb

# desde el archivo RolClass importa la clase Rol
from modelo.AutoClass import Auto

class AutoForm:
  # init es el constructor del formulario
  def __init__(self):
    # creamos el formulario en tkinter
    self.ventana = tk.Tk()
    # asignamos un titulo a la barra del formulario
    self.ventana.title("Formulario de Autos")
    # cambiar el tamaño de la ventana
    self.ventana.geometry('800x800')
    # cambiar color de fondo
    self.ventana.config(bg='blue')
    # instanciar la clase Rol
    self.auto = Auto()
    self.patente = ""
    # llamamos al metodo formulario
    self.formulario()
    self.cargar()
    # mostramos el formulario creado
    self.ventana.mainloop()

  def formulario(self):
    # label es el elemento de tkinter que permite mostrar texto
    # font sirve para cambiar el tipo de letra y el tamaño
    # bg cambia el color de fondo y fg cambiar el color de letra

    # Titulo del formulario
    labelTitulo = tk.Label(self.ventana, text="Formulario de Autos", font=("Arial Bold", 20), bg='blue', fg='white')
    labelTitulo.pack(pady=10)

    # Subtitulo auto
    labelAuto = tk.Label(self.ventana, text="Ingresa Auto", font=("Arial Bold", 16), bg='blue', fg='white')
    labelAuto.pack(pady=20)
    
    # Subtitulo Patente
    labelPatente = tk.Label(self.ventana, text="Ingresa Patente", font=("Arial Bold", 16), bg='blue', fg='white')
    labelPatente.pack(pady=5)
    
    # Input Patente
    self.inputPatente = tk.Entry(self.ventana, font=("Arial", 16), width=30)
    # mostramos el inputPatente en la ventana
    self.inputPatente.pack(pady=20)
    
    # Subtitulo Marca
    labelMarca = tk.Label(self.ventana, text="Ingresa Marca", font=("Arial Bold", 16), bg='blue', fg='white')
    labelMarca.pack(pady=5)
    
  # Input Patente
    self.inputMarca = tk.Entry(self.ventana, font=("Arial", 16), width=30)
    # mostramos el inputMarca en la ventana
    self.inputMarca.pack(pady=30)
    
    
    # Subtitulo Modelo
    labelModelo = tk.Label(self.ventana, text="Ingresa Modelo", font=("Arial Bold", 16), bg='blue', fg='white')
    labelModelo.pack(pady=5)
    
    # Input Patente
    self.inputModelo = tk.Entry(self.ventana, font=("Arial", 16), width=30)
    # mostramos el inputModelo en la ventana
    self.inputModelo.pack(pady=30)
    

    # -------------- BOTONES----------------

    self.btnFrame = tk.Frame(self.ventana, bg='blue')
    self.btnFrame.pack(pady=10)

    # creamos un boton guardar
    btnGuardar = tk.Button(self.btnFrame, text="Guardar", font=("Comic Sans", 16), bg='#cce6ff', fg='black', activebackground='#333399', activeforeground='white',borderwidth=10, command=self.guardar)
    # mostramos el boton guardar
    btnGuardar.pack(side=tk.LEFT, padx=10)

    btnLimpiar= tk.Button(self.btnFrame, text="Limpiar", font=("Comic Sans", 16), bg='#cce6ff', fg='black', activebackground='#333399', activeforeground='white',borderwidth=10, command=self.limpiar)
    btnLimpiar.pack(side=tk.LEFT, padx=10)
    
    btnEliminar = tk.Button(self.btnFrame, text="Eliminar", font=("Comic Sans", 16), bg='red', fg='black', activebackground='black', activeforeground='white',borderwidth=10, command=self.eliminar)
    btnEliminar.pack(side=tk.LEFT, padx=10)
    
    # Tabla
    # treeview es la tabla para mostrar los datos
    self.tabla = ttk.Treeview(self.ventana, columns=("patente", "marca", "modelo"), show='headings')

    # heading sirve para mostrar los encabezados de la tabla

    # definir ancho de la columna
    self.tabla.column("patente", width=50)
    self.tabla.heading("patente", text="Patente")
    self.tabla.heading("marca", text="Marca")
    self.tabla.heading("modelo", text="Modelo")

    # dimensiones de la tabla
    self.tabla.pack(pady=10, expand=True, fill='both')
    
    self.tabla.bind("<Double-1>", self.seleccionar)

  # Metodo guardar
  def guardar(self):
    # self.rol = self.input.get(), get permite obtener el valor del input
    if self.inputPatente.get() == "" or self.inputMarca.get() == "" or self.inputModelo.get() == "":
      # mb.showerror permite levantar una alerta
      mb.showerror("Error", "Todos los campos son requeridos")
    else:
      # si el id es igual a 0, significa que guarda uno nuevo
      if self.patente == "":
        # invocamos el método que permite guardar en la base de datos
        self.auto.add(self.inputPatente.get(), self.inputMarca.get(), self.inputModelo.get())
      else:
          # si el id es distinto de 0, modifica el registro
        self.auto.editar(self.patente, self.inputMarca.get(), self.inputModelo.get())
        # invocamos el método que permite guardar en la base de datos
      mb.showinfo("Mensaje", "Información del auto guardada correctamente")
      self.limpiar()
      self.cargar()

  def seleccionar(self, event):
    self.limpiar()
    fila = self.tabla.selection()
    
    if fila != "":
      item = self.tabla.item(fila)
      dato = item['values']
      
      self.patente = dato[0]
      self.inputPatente.insert(0, dato[0])
      self.inputMarca.insert(0, dato[1])
      self.inputModelo.insert(0, dato[2])
        
  def eliminar(self):
    # validamos si hay registro seleccionado
    if self.patente!= "":
      # preguntamos si queremos eliminar el Rol
      pregunta = mb.askyesno("Eliminar", "¿Desea eliminar el Automovil?")
      # verificamos la respuesta
      if pregunta:
        self.auto.eliminar(self.patente)
        self.cargar()
        self.limpiar()

  def limpiar(self):
    # limpiamos el input
    self.inputPatente.delete(0, tk.END)
    self.inputMarca.delete(0, tk.END)
    self.inputModelo.delete(0, tk.END)
    self.patente = ""
    
  def cargar(self):
    # eliminar los datos que tenga la tabla
    self.tabla.delete(*self.tabla.get_children())
    # traer los datos de la base de datos
    datos = self.auto.lista()
    # recorrer los datos de la base de datos
    for item in datos:
      # insertar los datos en la tabla
      self.tabla.insert('', tk.END, values=(item[0], item[1], item[2]), text=(item[0], item[1], item[2]))
      
# instanciamos la clase RolForm
form = AutoForm()