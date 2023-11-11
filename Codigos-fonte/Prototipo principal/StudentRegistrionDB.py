
import psycopg2 as pg
from tkinter import messagebox as mb

class StudentRegistrionDB:
#Construtor:
   def __init__(self):
        print('Método Construtor')
        
   def abrirConexao(self):
        try:
          self.connection = pg.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
        except (Exception, pg.Error) as error :
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)
# Fecha Conexão
   def fechaConexão(self,cursor):
        # closing database connection.
        if (self.connection):
            cursor.close()
            self.connection.close()
            print("A conexão com o PostgreSQL foi fechada.")
# Criar tabela:
   def criarTabela(self):
       try:
           self.abrirConexao()
           cursor = self.connection.cursor()

           query_create_table = '''
                CREATE TABLE IF NOT EXISTS TBMATRICULA(
                    MATRICULA INTEGER NOT NULL PRIMARY KEY,
                    CURSO TEXT NOT NULL,
                    TURMA TEXT NOT NULL,
                    DTCADASTRO TEXT,
                    foreign key(MATRICULA) REFERENCES TBALUNO(MATRICULA)
                );
            '''
           cursor.execute(query_create_table)
           self.connection.commit()
           mb.showinfo('Criação Tabela','Tabela criada com sucesso !')
    
       except (Exception, pg.Error) as error:
           mb.showerror('Erro',f'Erro na criação da tabela {error}')

# selecionar Dados:
   def selecionarDados(self):
       try:
           self.abrirConexao()
           self.criarTabela()
           cursor = self.connection.cursor()

           query_select = '''
                SELECT 
                    A.MATRICULA ,
                    M.CURSO  ,
                    M.TURMA ,
                    M.DTCADASTRO,
                    A.NOMEALUNO,
                    A.RESP1
                FROM TBALUNO A
                INNER JOIN TBMATRICULA M ON A.MATRICULA = M.MATRICULA;
            '''
           cursor.execute(query_select)
           registros = cursor.fetchall() 
           print(registros)

       except (Exception, pg.Error) as error:
           mb.showerror('Erro',f'Erro ao selcionar os dados {error}')
       finally:
           self.fechaConexão(cursor)
       return registros

# Inserir Dados:
   def inserirDados(self, MATRICULA ,CURSO ,TURMA,DTCADASTRO):
       try:
           self.abrirConexao()
           cursor = self.connection.cursor()

           query_insert = '''
                INSERT INTO TBMATRICULA(MATRICULA ,CURSO ,TURMA,DTCADASTRO)
                VALUES(%s,%s,%s,%s)
            '''
           records = (MATRICULA ,CURSO.upper() ,TURMA.upper(),DTCADASTRO)
           cursor.execute(query_insert,records)

           self.connection.commit()
           count = cursor.rowcount
           mb.showinfo('Sucesso',f'{count} Registro inserido com sucesso !')

       except  (Exception, pg.Error) as error:
            mb.showerror('Erro', f'Houve um erro na inserção de dados {error}')
       finally:
           self.fechaConexão(cursor)

# Atualizar Dados:
   def atualizarDados(self, MATRICULA ,CURSO ,TURMA,DTCADASTRO):
        try:
            self.abrirConexao() 
            cursor = self.connection.cursor()

            #Registro Antes da Atualização 
            sql_select_query = ''' SELECT * FROM TBMATRICULA WHERE MATRICULA = %s '''
            cursor.execute(sql_select_query, (MATRICULA,))
            record = cursor.fetchone()
            print(record)

            # Atualizar registro
            sql_update_query = """Update TBMATRICULA set  CURSO = %s, TURMA = %s, DTCADASTRO = %s where MATRICULA = %s"""
            cursor.execute(sql_update_query, (CURSO.upper() ,TURMA.upper(),DTCADASTRO, MATRICULA))
            self.connection.commit()
            count = cursor.rowcount
            mb.showinfo('Sucesso', f" {count} Registro atualizado com sucesso! ")    

            print("Registro Depois da Atualização ")
            sql_select_query = ''' SELECT * FROM TBMATRICULA WHERE MATRICULA = %s '''
            cursor.execute(sql_select_query, (MATRICULA,))
            record = cursor.fetchone()
            print(record)  
        except  (Exception, pg.Error) as error:
            mb.showerror('Erro', f"Erro na Atualização {error}")    
        finally:
            self.fechaConexão(cursor)

# Excluir Dados:
   def excluirDados(self, MATRICULA):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            #Excluir dados:
            query_delete = '''
                DELETE FROM TBMATRICULA WHERE MATRICULA = %s
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

#---------------------------------------------------------------------
#estudante = StudentRegistrionDB()

#estudante.inserirDados(4,'analise e desenvolvimento de sistemas','A50036','26/04/2023')
#estudante.atualizarDados(4,'analise e desenvolvimento de sistemas','A50037','01/01/2022')
#estudante.excluirDados(2)

