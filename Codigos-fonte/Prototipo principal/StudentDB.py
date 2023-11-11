# Importação do biblioteca Psycopg2
import psycopg2 as pg
from tkinter import messagebox as mb

class StudentDB:

    def __init__(self):
        print('Método Construtor')

    # Conexão com o banco:
    def abrirConexão(self):
        try:
            self.connection = pg.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
        except (Exception, pg.Error) as error:
            if self.connection:
                mb.showerror('Erro',f'Falha ao se conectar com o banco de dados {error}')
    
    def fechaConexão(self,cursor):
        # closing database connection.
        if (self.connection):
            cursor.close()
            self.connection.close()
            print("A conexão com o PostgreSQL foi fechada.")

    #Criar a tabela:
    def criarTabela(self):
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()

            #Comando para criar a tabela:
            query_create_table = '''
                CREATE TABLE IF NOT EXISTS TBALUNO (
                    MATRICULA INTEGER PRIMARY KEY NOT NULL,
                    NOMEALUNO TEXT NOT NULL,
                    DATANASC TEXT NOT NULL,
                    RESP1 TEXT NOT NULL,
                    RESP2 TEXT
                );
            '''
            cursor.execute(query_create_table)
            self.connection.commit()

        except (Exception, pg.Error) as error:
            if(self.connection):
                mb.showinfo('Erro',f'Houve um problema na criação da tabela {error}')
                print(error)
        finally:
            self.fechaConexão(cursor)
        
    # Selecionar Dados
    def selecionarDados(self):
        try:
            self.criarTabela()
            self.abrirConexão()
            cursor = self.connection.cursor()

            #Consultal:
            query_select = '''
                SELECT * FROM TBALUNO ORDER BY NOMEALUNO;
            '''

            cursor.execute(query_select)
            registros = cursor.fetchall()             
            print(registros)
        
        except (Exception, pg.Error) as error:
            mb.showerror('Erro', 'Erro ao selecionar os dados' + error)
        finally:
            self.fechaConexão(cursor)
        return registros
    
    # Inserir Dados:
    def inserirDados(self,MATRICULA,NOMEALUNO, DATANASC, RESP1, RESP2):
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()

            insert_values = '''
                INSERT INTO TBALUNO(MATRICULA,NOMEALUNO, DATANASC, RESP1, RESP2)
                VALUES (%s,%s,%s,%s,%s)
            '''
            record_to_values = (MATRICULA,NOMEALUNO.upper(), DATANASC, RESP1.upper(), RESP2.upper())
            cursor.execute(insert_values,record_to_values)

            self.connection.commit()
            count = cursor.rowcount
            mb.showinfo('Sucesso',f'{count} Registro inserido com sucesso !')

        except  (Exception, pg.Error) as error:
            mb.showerror('Erro', f'Houve um erro na inserção de dados {error}')
        finally:
            self.fechaConexão(cursor)
        
    # Atualizar dados
    def atualizarDados(self, MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2):
        try:
            self.abrirConexão() 
            cursor = self.connection.cursor()

            #Registro Antes da Atualização 
            sql_select_query = ''' SELECT * FROM TBALUNO WHERE MATRICULA = %s '''
            cursor.execute(sql_select_query, (MATRICULA,))
            record = cursor.fetchone()
            print(record)

            # Atualizar registro
            sql_update_query = """Update TBALUNO set  NOMEALUNO = %s, DATANASC = %s, RESP1 = %s, RESP2 = %s    
            where MATRICULA = %s"""
            cursor.execute(sql_update_query, (NOMEALUNO.upper(), DATANASC, RESP1.upper(), RESP2.upper(), MATRICULA))
            self.connection.commit()
            count = cursor.rowcount
            mb.showinfo('Sucesso', f" {count} Registro atualizado com sucesso! ")    

            print("Registro Depois da Atualização ")
            sql_select_query = """ SELECT * FROM TBALUNO where MATRICULA = %s"""
            cursor.execute(sql_select_query, (MATRICULA,))
            record = cursor.fetchone()
            print(record)   
        except  (Exception, pg.Error) as error:
            mb.showerror('Erro', f"Erro na Atualização {error}")    
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
    
    # Excluir Alunos:
    def excluirDados(self, MATRICULA):
        try:
            self.abrirConexão()
            cursor = self.connection.cursor()

            #Excluir dados:
            query_delete = '''
                DELETE FROM TBALUNO WHERE MATRICULA = %s
            '''

            cursor.execute(query_delete,(MATRICULA,))
            if mb.askyesno("Verificar", " Deseja excluir esse dado ?"):
                mb.showwarning('Yes', 'Deseja excluir esse dado')
                self.connection.commit()
                count = cursor.rowcount
                mb.showinfo('Sucesso', f'{count} Item Excuido com sucesso !')
            else:
              mb.showinfo('No', 'Exclusão cancelada')

        except (Exception, pg.Error) as error:
            mb.showerror('Erro','Erro ao excuir um Aluno' + error)
        finally:
            self.fechaConexão(cursor)


#---------------------------------------
estudante = StudentDB()
#estudante.criarTabela()
#estudante.inserirDados(1,'Heloisa','2003.09.20','Higor','ana')
#estudante.atualizarDados(1,'ALICE','2003.04.30','HELIO OLIVEIRA','MARIA SANTANA')
#estudante.excluirDados(1)
estudante.selecionarDados();






