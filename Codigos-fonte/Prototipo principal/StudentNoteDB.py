
import psycopg2 as pg
from tkinter import messagebox as mb

class StudentNoteDB:
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

#Fechar Conexão
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
                CREATE TABLE IF NOT EXISTS TBNOTA(
                    IDLANC INT PRIMARY KEY NOT NULL,
                    NOTA DECIMAL(10,2),
                    MATRICULA INT NOT NULL,
                    DISCIPLINA TEXT NOT NULL,
                    foreign key(MATRICULA) REFERENCES TBMATRICULA(MATRICULA)
                );
            '''
           cursor.execute(query_create_table)
           self.connection.commit()
           #mb.showinfo('Tabela','Tabela criada com sucesso !')
    
       except (Exception, pg.Error) as error:
           mb.showerror('Erro',f'Erro na criação da tabela {error}')
       
# Selecionar Dados
   def selecionarDados(self):
        try:
            self.criarTabela()
            self.abrirConexao()
            cursor = self.connection.cursor()

            #Consultal:
            query_select = '''
                SELECT 
                    N.IDLANC,
                    N.DISCIPLINA,
                    N.NOTA,
                    N.MATRICULA,
                    A.NOMEALUNO,
                    M.CURSO,
                    M.TURMA
                FROM TBALUNO A
                INNER JOIN TBMATRICULA M ON A.MATRICULA = M.MATRICULA
                INNER JOIN TBNOTA N ON M.MATRICULA = N.MATRICULA
                ORDER BY A.NOMEALUNO;
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
   def inserirDados(self,IDLANC,DISCIPLINA,NOTA,MATRICULA):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            insert_values = '''
                INSERT INTO TBNOTA(IDLANC,NOTA,MATRICULA,DISCIPLINA)
                VALUES (%s,%s,%s,%s)
            '''
            record_to_values = (IDLANC,NOTA,MATRICULA,DISCIPLINA.upper())
            cursor.execute(insert_values,record_to_values)

            self.connection.commit()
            count = cursor.rowcount
            mb.showinfo('Sucesso',f'{count} Registro inserido com sucesso !')

        except  (Exception, pg.Error) as error:
            mb.showerror('Erro', f'Houve um erro na inserção de dados {error}')
        finally:
            self.fechaConexão(cursor)
        
    # Atualizar dados
   def atualizarDados(self, IDLANC,DISCIPLINA,NOTA,MATRICULA):
        try:
            self.abrirConexao() 
            cursor = self.connection.cursor()

            #Registro Antes da Atualização 
            sql_select_query = ''' SELECT * FROM TBNOTA WHERE MATRICULA = %s '''
            cursor.execute(sql_select_query, (MATRICULA,))
            record = cursor.fetchone()
            print(record)

            # Atualizar registro
            sql_update_query = """Update TBNOTA set  NOTA = %s, MATRICULA = %s, DISCIPLINA = %s where IDLANC = %s"""
            cursor.execute(sql_update_query, (NOTA, MATRICULA,DISCIPLINA.upper(),IDLANC))
            self.connection.commit()
            count = cursor.rowcount
            mb.showinfo('Sucesso', f" {count} Registro atualizado com sucesso! ")    

            print("Registro Depois da Atualização ")
            sql_select_query = """ SELECT * FROM TBNOTA WHERE MATRICULA = % """
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
            self.abrirConexao()
            cursor = self.connection.cursor()

            #Excluir dados:
            query_delete = '''
                DELETE FROM TBNOTA WHERE MATRICULA = %s
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
#------------------------------------------------------------------------------------------------------------

#estudante = StudentNoteDB()

#estudante.selecionarDados()
#estudante.inserirDados(1,'RAD',9.5,1)
#$estudante.atualizarDados(1,'RAD',10,1)
#estudante.excluirDados(1)

