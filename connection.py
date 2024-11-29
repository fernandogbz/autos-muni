# instalar mysql-connector para conectar con la db
# pip install mysql-connector o py -m pip install mysql-connector 

import mysql.connector

class ConnectionDatabase:
  def __init__(self):
    self.connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="autosdb"
    )
    
    # cursor sirve para ejecutar las consultas en la db
    self.cursor = self.connection.cursor()
    
# -- Test database connection
#   def showtables(self):
#     query="SHOW TABLES"
#     self.cursor.execute(query)
#     tables = self.cursor.fetchall()
#     return tables
  
# bd = ConnectionDatabase()
# print(bd.showtables())