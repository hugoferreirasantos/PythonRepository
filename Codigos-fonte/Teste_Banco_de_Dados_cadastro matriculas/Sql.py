# importando o a biblioteca Sqlite3:
import sqlite3 as connector


# Criando uma conexão Sql:
class Sql:

    # Atributos:
    def __init__(self):
        self.conn = connector.connect(
            'D:\Ambiente_Desenvolvimento\Aulas_Python 3 - 2 - 2023\Repositorio\Codigos-fonte\Teste_Banco_de_Dados_cadastro matriculas\instituicao_faculdade.db')
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

    def update(self, query, data):
        conxeion = self.conn
        cursor = conxeion.cursor()
        cursor.execute(query, data)
        conxeion.commit()

    def delete(self, query, data):
        conxeion = self.conn
        cursor = conxeion.cursor()
        cursor.execute(query, data)
        conxeion.commit()

    def select(self, query, data=None):

        if data == None:
            conexion = self.conn
            cursor = conexion.cursor()

            consult = cursor.execute(query)

            return consult
        elif data is not None:
            conexion = self.conn
            cursor = conexion.cursor()

            consult = cursor.execute(query, data)

            return consult
