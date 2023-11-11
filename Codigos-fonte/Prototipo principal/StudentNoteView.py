# Aplicação View 

import tkinter as tk
from tkinter import ttk
import StudentNoteDB as crud


class StudentView:
    def __init__(self, win):
        self.objBD = crud.StudentNoteDB()
    
    #Componentes:
        self.lblLanc = tk.Label(win, text='LANÇAMENTO')
        self.lblDisciplina = tk.Label(win,text='DISCIPLINA')
        self.lblNota = tk.Label(win, text='NOTA')
        self.lblMatricula = tk.Label(win, text='MATRICULA')

        self.txtLanc = tk.Entry(border=3)
        self.txtDisciplina = tk.Entry()
        self.txtNota = tk.Entry()
        self.txtMatricula = tk.Entry()

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)
    # Componente TreeView
        self.dadosColunas = ("IDLANC","DISCIPLINA", "NOTA", "MATRICULA", "NOMEALUNO", "CURSO", "TURMA")

        self.treeAlunos = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                         orient='vertical',
                                         command=self.treeAlunos.yview)
        
        self.verscrlbar.pack(side='right',fill='x')
        self.treeAlunos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeAlunos.heading("IDLANC", text="ID")
        self.treeAlunos.heading("DISCIPLINA", text='DISCIPLINA')
        self.treeAlunos.heading("NOTA", text="NOTA")
        self.treeAlunos.heading("MATRICULA", text="MATRICULA")  
        self.treeAlunos.heading("NOMEALUNO", text="ALUNO")   
        self.treeAlunos.heading("CURSO", text="CURSO")  
        self.treeAlunos.heading("TURMA", text="TURMA")      

        self.treeAlunos.column("IDLANC",minwidth=0,width=90)
        self.treeAlunos.column("DISCIPLINA",minwidth=0,width=100)
        self.treeAlunos.column("NOTA",minwidth=0,width=100)
        self.treeAlunos.column("MATRICULA",minwidth=0,width=100)
        self.treeAlunos.column("NOMEALUNO",minwidth=0,width=200)
        self.treeAlunos.column("CURSO",minwidth=0,width=200)
        self.treeAlunos.column("TURMA",minwidth=0,width=100)

        self.treeAlunos.pack(padx=10, pady=10)

        self.treeAlunos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados) 
        
    #posicionamento dos componentes na janela

        self.lblLanc.place(x=100,y=50)
        self.txtLanc.place(x=250, y=50)

        self.lblDisciplina.place(x=100,y=100)
        self.txtDisciplina.place(x=250, y=100, width=190)

        self.lblNota.place(x=100,y=150)
        self.txtNota.place(x=250, y=150)

        self.lblMatricula.place(x=450,y=100)
        self.txtMatricula.place(x=610, y=100)



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
            IDLANC, DISCIPLINA, NOTA, MATRICULA= item["values"][0:4]  
            self.txtLanc.insert(0, IDLANC)
            self.txtDisciplina.insert(0,DISCIPLINA)
            self.txtNota.insert(0, NOTA)
            self.txtMatricula.insert(0, MATRICULA)  
    #----------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0         
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              IDLANC = item[0] 
              DISCIPLINA = item[1]
              NOTA = item[2]   
              MATRICULA = item[3]  
              NOMEALUNO = item[4]  
              CURSO = item[5]  
              TURMA = item[6]
              print("IDLANC", IDLANC, "\n")
              print('DISCIPLINA', DISCIPLINA, "\n")
              print("NOTA", NOTA, "\n")
              print("MATRICULA = ", MATRICULA, "\n")
              print("NOME = ", NOMEALUNO, "\n")
              print("CURSO = ", CURSO, "\n") 
              print("TURMA = ", TURMA, "\n")
              self.treeAlunos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(IDLANC,DISCIPLINA,NOTA,MATRICULA, NOMEALUNO, CURSO, TURMA))                    
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
          IDLANC=self.txtLanc.get()
          print('IDLANC', IDLANC)
          DISCIPLINA = self.txtDisciplina.get()
          print('DISCIPLINA', DISCIPLINA)
          NOTA=float(self.txtNota.get())          
          print('NOTA', NOTA)
          MATRICULA=self.txtMatricula.get()          
          print('MATRICULA', MATRICULA)      
        except:
          print('Não foi possível ler os dados.')
        return IDLANC,DISCIPLINA.upper(), float(NOTA), MATRICULA
    #---------------------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          IDLANC,DISCIPLINA,NOTA,MATRICULA= self.fLerCampos()                    
          self.objBD.inserirDados(IDLANC,DISCIPLINA,NOTA,MATRICULA)                    
          self.treeAlunos.insert('', 'end',
                                iid=self.iid,                                   
                                values=(IDLANC,DISCIPLINA,NOTA,MATRICULA))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fLimparTela()
          self.carregarDadosIniciais()
          print('Produto Cadastrado com Sucesso!')        
        except:
          print('Não foi possível fazer o cadastro.')
    #----------------------------------------------------------------------------------------
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          IDLANC,DISCIPLINA,NOTA,MATRICULA= self.fLerCampos()
          self.objBD.atualizarDados(IDLANC,DISCIPLINA,float(NOTA),MATRICULA)          
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
          IDLANC,DISCIPLINA,NOTA,MATRICULA= self.fLerCampos()
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
          self.txtLanc.delete(0, tk.END)
          self.txtDisciplina.delete(0, tk.END)
          self.txtNota.delete(0, tk.END)
          self.txtMatricula.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')
    #----------------------------------------------------------------------

janela=tk.Tk()
principal=StudentView(janela)
janela.title('CADASTRO NOTA FINAL - CURSO')
janela.geometry("1250x600+10+10")
janela.mainloop()



