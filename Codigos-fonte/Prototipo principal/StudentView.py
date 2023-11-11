# Aplicação View 

import tkinter as tk
from tkinter import ttk
import StudentDB as crud


class StudentView:
    def __init__(self, win):
        self.objBD = crud.StudentDB()
    
    #Componentes:
        
        self.lblMatricula =tk.Label(win, text='MATRÍCULA')
        self.lblNome = tk.Label(win, text='ALUNO')
        self.lblDtNasc = tk.Label(win, text='DATA DE NASCIMENTO')
        self.lblRepPrincipal = tk.Label(win, text='RESPONSÁVEL PRINCIPAL')
        self.lblResSecudario = tk.Label(win, text='RESPONSÁVEL SECUNDÁRIO')

        self.txtMatricula = tk.Entry(border=3)
        self.txtNome = tk.Entry()
        self.txtDtNasc = tk.Entry()
        self.txtRepPrincipal = tk.Entry()
        self.txtResSecudario = tk.Entry()

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
    # Componente TreeView
        self.dadosColunas = ( "MATRICULA", "NOMEALUNO", "DATANASC", "RESP1", "RESP2")

        self.treeAlunos = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                         orient='vertical',
                                         command=self.treeAlunos.yview)
        
        self.verscrlbar.pack(side='right',fill='x')
        self.treeAlunos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeAlunos.heading("MATRICULA", text="MATRÍCULA")
        self.treeAlunos.heading("NOMEALUNO", text="ALUNO")
        self.treeAlunos.heading("DATANASC", text="NASCIMENTO")  
        self.treeAlunos.heading("RESP1", text="RESPONSÁVEL PRINCIPAL")   
        self.treeAlunos.heading("RESP2", text="RESPONSÁVEL SECUDÁRIO")      

        self.treeAlunos.column("MATRICULA",minwidth=0,width=90)
        self.treeAlunos.column("NOMEALUNO",minwidth=0,width=100)
        self.treeAlunos.column("DATANASC",minwidth=0,width=100)
        self.treeAlunos.column("RESP1",minwidth=0,width=200)
        self.treeAlunos.column("RESP2",minwidth=0,width=200)

        self.treeAlunos.pack(padx=10, pady=10)

        self.treeAlunos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados) 
        
    #posicionamento dos componentes na janela

        self.lblMatricula.place(x=100,y=50)
        self.txtMatricula.place(x=250, y=50)

        self.lblNome.place(x=100,y=100)
        self.txtNome.place(x=250, y=100, width=190)

        self.lblDtNasc.place(x=100,y=150)
        self.txtDtNasc.place(x=250, y=150)

        self.lblRepPrincipal.place(x=450,y=100)
        self.txtRepPrincipal.place(x=610, y=100, width=190)

        self.lblResSecudario.place(x=450,y=150)
        self.txtResSecudario.place(x=610, y=150, width=190)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeAlunos.place(x=100, y=300)
        self.verscrlbar.place(x=999, y=300, height=255)       
        self.carregarDadosIniciais()
    
    #-------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeAlunos.selection():  
            item = self.treeAlunos.item(selection)  
            MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2 = item["values"][0:5]  
            self.txtMatricula.insert(0, MATRICULA)  
            self.txtNome.insert(0, NOMEALUNO)  
            self.txtDtNasc.insert(0, DATANASC)
            self.txtRepPrincipal.insert(0, RESP1)
            self.txtResSecudario.insert(0, RESP2)
    
    #----------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0         
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              MATRICULA=item[0]
              NOMEALUNO=item[1]
              DATANASC=item[2]
              RESP1 = item[3]
              RESP2 = item[4]
              print("MATRICULA = ", MATRICULA, "\n")
              print("NOME = ", NOMEALUNO, "\n")
              print("DATANASC = ", DATANASC, "\n") 
              print("RESP1 = ", RESP1, "\n")
              print("RESP2  = ", RESP2, "\n")
                        
              self.treeAlunos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2 ))                    
              self.iid = self.iid + 1
              self.id = self.id + 1
          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar') 
          print(registros)

    #----------------------------------------------------------------------------------
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          MATRICULA= int(self.txtMatricula.get())
          print('MATRICULA', MATRICULA)
          NOMEALUNO=self.txtNome.get()
          print('NOME', NOMEALUNO)
          DATANASC=self.txtDtNasc.get()          
          print('DATANASC', DATANASC)
          RESP1=self.txtRepPrincipal.get()          
          print('RESP1', RESP1)
          RESP2=self.txtResSecudario.get()        
          print('RESP2', RESP2)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return MATRICULA, NOMEALUNO.upper(), DATANASC, RESP1.upper(), RESP2.upper()
    #---------------------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2= self.fLerCampos()                    
          self.objBD.inserirDados(MATRICULA,NOMEALUNO, DATANASC, RESP1, RESP2)                    
          self.treeAlunos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(MATRICULA
                                        ,NOMEALUNO, 
                                        DATANASC, 
                                        RESP1, 
                                        RESP2))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fLimparTela()
          print('Produto Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')
    #----------------------------------------------------------------------------------------
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2= self.fLerCampos()
          self.objBD.atualizarDados(MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2)          
          #recarregar dados na tela
          self.treeAlunos.delete(*self.treeAlunos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Atualizado com Sucesso!')        
        except:
          print('Não foi possível fazer a atualização.')
    #---------------------------------------------------------------------------------------
    def fExcluirProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          MATRICULA, NOMEALUNO, DATANASC, RESP1, RESP2= self.fLerCampos()
          self.objBD.excluirDados(MATRICULA)          
          #recarregar dados na tela
          self.treeAlunos.delete(*self.treeAlunos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do produto.')
    #----------------------------------------------------------------------------------------
    def fLimparTela(self):
        try:
          print("************ dados dsponíveis ***********")      
          self.txtMatricula.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtDtNasc.delete(0, tk.END)
          self.txtRepPrincipal.delete(0,tk.END)
          self.txtResSecudario.delete(0,tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')
    #----------------------------------------------------------------------
    def main():  
     janela=tk.Tk()
     principal=StudentView(janela)
     janela.title('CADASTRO ALUNO')
     janela.geometry("1200x600+10+10")
     janela.mainloop()


StudentView.main()
