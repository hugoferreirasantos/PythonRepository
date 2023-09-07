# importando o a biblioteca Sqlite3:
import sqlite3 as connector


# Criando uma conexão Sql:
class Sql:

    # Atributos:
    def __init__(self):
        self.conn = connector.connect('db_cadastro_matriculas')
        self.cursor = self.conn.cursor()

    # Metodos:
    def create_table(self, table):
        conexion = self.conn
        cursor = conexion.cursor()
        cursor.execute(table)
        conexion.commit()

    def insert(self, query, data):
        conxeion = self.conn
        cursor = conxeion.cursor()
        cursor.executemany(query, data)
        conxeion.commit()

    def select(self, query):
        conexion = self.conn
        cursor = conexion.cursor()

        consult = cursor.execute(query)

        return consult
