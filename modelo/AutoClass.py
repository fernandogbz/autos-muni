from connection import ConnectionDatabase
class Auto:
  # atributos
  patente: str
  marca: str
  modelo: str
  
  # ---- Metodo para guardar en la base de datos
  def add(self, patente, marca, modelo):
    # consulta para insertar datos, %s indica que lleva un valor
    query = ('INSERT INTO automovil (patente, marca, modelo) VALUES (%s, %s, %s)')

    # value indica el valor que se asigna a la consulta (si es uno debe llevar , al final)
    value = (patente, marca, modelo)
    
    # abrir conexión con la base de datos, creando el objeto db
    db = ConnectionDatabase()
    
    # ejecutar la consulta (pasamos la consuta y los valores)
    db.cursor.execute(query, value)
    
    # guardar los cambios en la base de datos
    db.connection.commit()
    
    # cerrar la conexión con la base de datos
    db.cursor.close()
  
  def lista(self):
    query = ('SELECT * FROM automovil')
    db = ConnectionDatabase()
    db.cursor.execute(query)
    # fetchall trae todos los datos de la consulta
    patentes = db.cursor.fetchall()
    db.connection.close()
    # retornamos la variable con los datos
    return patentes
  
  def eliminar (self, id):
    query = 'DELETE FROM automovil WHERE patente = %s'
    value = id,
    db = ConnectionDatabase()
    db.cursor.execute(query, value)
    db.connection.commit()
    db.cursor.close()
    
  def editar (self, patente, marca, modelo):
    query = 'UPDATE automovil SET patente = %s AND SET marca = %s AND SET modelo = %s  WHERE patente = %s'
    values = patente, marca, modelo
    db = ConnectionDatabase()
    db.cursor.execute(query, values)
    db.connection.commit()
    db.connection.close()