# Aplicação View 

import tkinter as tk
from tkinter import ttk
import StudentRegistrionDB as crud


class StudentRegistrionView:
    def __init__(self, win):
        self.objBD = crud.StudentRegistrionDB()
    
    #Componentes:
       
        self.lblMatricula = tk.Label(win, text='MATRÍCULA')
        self.lblCurso = tk.Label(win, text='CURSO')
        self.lblTurma = tk.Label(win, text='TURMA')
        self.lblDtcadastro = tk.Label(win, text='DATA MATRICULA')

        self.txtMatricula = tk.Entry(bd=3)
        self.txtCurso = tk.Entry()
        self.txtTurma = tk.Entry()
        self.txtDtcadastro = tk.Entry()

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
    # Componente TreeView
        self.dadosColunas = ( "MATRICULA","CURSO", "TURMA","DTCADASTRO","NOMEALUNO","RESP1")

        self.treeAlunos = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                         orient='vertical',
                                         command=self.treeAlunos.yview)
        
        self.verscrlbar.pack(side='right',fill='x')
        self.treeAlunos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeAlunos.heading("MATRICULA", text="MATRÍCULA")
        self.treeAlunos.heading("CURSO", text="CURSO")  
        self.treeAlunos.heading("TURMA", text="TURMA")   
        self.treeAlunos.heading("DTCADASTRO", text="DATA MATRÍCULA") 
        self.treeAlunos.heading("NOMEALUNO", text="ALUNO")
        self.treeAlunos.heading("RESP1",text= "RESPONSÁVEL FINANCEIRO")     

        self.treeAlunos.column("MATRICULA",minwidth=0,width=90)
        self.treeAlunos.column("CURSO",minwidth=0,width=100)
        self.treeAlunos.column("TURMA",minwidth=0,width=100)
        self.treeAlunos.column("DTCADASTRO",minwidth=0,width=200)
        self.treeAlunos.column("NOMEALUNO",minwidth=0,width=200)
        self.treeAlunos.column("RESP1",minwidth=0,width=200)

        self.treeAlunos.pack(padx=10, pady=10)

        self.treeAlunos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados) 
        
    #posicionamento dos componentes na janela

        self.lblMatricula.place(x=100,y=50)
        self.txtMatricula.place(x=250, y=50)


        self.lblCurso.place(x=100,y=100)
        self.txtCurso.place(x=250, y=100, width=190)

        self.lblTurma.place(x=100,y=150)
        self.txtTurma.place(x=250, y=150)

        self.lblDtcadastro.place(x=450,y=100)
        self.txtDtcadastro.place(x=610, y=100)


        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeAlunos.place(x=100, y=300)
        self.verscrlbar.place(x=1200, y=300, height=255)       
        self.carregarDadosIniciais()
    
    #-------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeAlunos.selection():  
            item = self.treeAlunos.item(selection)  
            MATRICULA, CURSO ,TURMA,DTCADASTRO = item["values"][0:4]  
            self.txtMatricula.insert(0, MATRICULA)
            self.txtCurso.insert(0, CURSO)  
            self.txtTurma.insert(0, TURMA)  
            self.txtDtcadastro.insert(0, DTCADASTRO)
    
    #----------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0         
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              MATRICULA = item[0]
              NOMEALUNO = item[1]
              CURSO = item[2]
              TURMA = item[3]
              RESP1 = item[4]
              DTCADASTRO = item[5]
              print("MATRICULA = ", MATRICULA, "\n")
              print("NOME = ", NOMEALUNO, "\n")
              print("CURSO = ", CURSO, "\n") 
              print("TURMA = ", TURMA, "\n")
              print("DTCADASTRO  = ", DTCADASTRO, "\n")
                        
              self.treeAlunos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=( MATRICULA, NOMEALUNO, CURSO, TURMA, RESP1,DTCADASTRO))                    
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
          MATRICULA=self.txtMatricula.get()
          print('MATRICULA', MATRICULA)
          CURSO=self.txtCurso.get()          
          print('CURSO', CURSO)
          TURMA=self.txtTurma.get()          
          print('TURMA', TURMA)
          DTCADASTRO=self.txtDtcadastro.get()        
          print('DTCADASTRO', DTCADASTRO)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return MATRICULA ,CURSO.upper(), TURMA.upper(), DTCADASTRO.upper()
    #---------------------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          MATRICULA ,CURSO ,TURMA,DTCADASTRO= self.fLerCampos()                    
          self.objBD.inserirDados(MATRICULA ,CURSO ,TURMA,DTCADASTRO)                    
          self.treeAlunos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(MATRICULA ,CURSO ,TURMA,DTCADASTRO))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.carregarDadosIniciais()
          self.fLimparTela()
          self.carregarDadosIniciais()
          print('Produto Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')
    #----------------------------------------------------------------------------------------
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          MATRICULA ,CURSO ,TURMA,DTCADASTRO= self.fLerCampos()
          self.objBD.atualizarDados(MATRICULA ,CURSO ,TURMA,DTCADASTRO)          
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
          MATRICULA ,CURSO ,TURMA,DTCADASTRO= self.fLerCampos()
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
          self.txtCurso.delete(0, tk.END)
          self.txtTurma.delete(0, tk.END)
          self.txtDtcadastro.delete(0,tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')
    #----------------------------------------------------------------------

janela=tk.Tk()
principal=StudentRegistrionView(janela)
janela.title('CADASTRO DE MATRICULA')
janela.geometry("1250x600+10+10")
janela.mainloop()



