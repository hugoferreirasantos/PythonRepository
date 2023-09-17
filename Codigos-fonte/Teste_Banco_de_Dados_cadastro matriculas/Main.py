from Sql import Sql
from Estudent import Estudent

import sqlite3 as connector

'''


def print_screen():
    print('Bem vindo !')
    print('1 - Cadastrar aluno: ')
    print('2 - Consultar cadastro de estudentes: ')
    print('3 - Consultar expecifica por nome: ')


flag = True
while flag:
    print_screen()
    option = int(input('DIGITE UMA OPÇÃO: '))

    if option == 1:
        student = Estudent()
        quantity = int(input('DESEJA CADASTRAR QUANTOS ESTUDENTES ?: '))
        student.registerEstudents(quantity)

    elif option == 2:
        print('------------------------CONSULTA-------------------')
        print()
        student2 = Estudent()
        student2.consultEstudents(True)
        print()

    elif option == 3:
        student3 = Estudent()
        student3.consultEstudents(False)
'''



'''
student = Estudent()
quantity = int(input('DESEJA CADASTRAR QUANTOS ESTUDENTES ?: '))
student.registerEstudents(quantity)

student2 = Estudent()
student2.UpdateStudent('curso')

student2 = Estudent()
student2.UpdateNotas('nota')
'''


def print_screen():
    print('Bem vindo !')
    print('1 - Cadastrar aluno: ')
    print('2 - Consultar cadastro de estudentes: ')
    print('3 - Consulta expecifica por nome(aluno): ')
    print('4 - Consulta expecifica por CPF(aluno)')
    print('5 - Alteração de informações de todas as informações do aluno: ')
    print('6 - Alteração de informações do aluno: NOME')
    print('7 - Alteração de informações do aluno: CPF')
    print('8 - Alteração de informações do aluno: CURSO')
    print('9 - 9 - Exclusão de notas dos alunos, junto com as informações do aluno')
    print('-----------------------------------------------------------------------------------------------------------')
    print('  __________________EDIÇÃO DE NOTAS_____________________________')
    print('10 - Registrar notas para estudantes:  ')
    print('11 - Alteração de informações de notas - DO ALUNO')
    print('12 - Alteração de informações de notas - MATRICULA VINCULADA A NOTA')
    print('13 - Alteração de informações de notas - NOTA VINCULADA AO ID DA NOTA NA TABELA NOTAS')
    print('9 - Exclusão de notas dos alunos, junto com as informações do aluno')




try:
    flag = True
    while flag:
        print_screen()
        option = int(input('DIGITE UMA OPÇÃO: '))

        if option == 1:
            student = Estudent()
            quantity = int(input('DESEJA CADASTRAR QUANTOS ESTUDENTES ?: '))
            student.registerEstudents(quantity)

        elif option == 2:
            print('------------------------CONSULTA-------------------')
            print()
            student2 = Estudent()
            student2.consultEstudents(True,'all')
            print()

        elif option == 3:
            print('------------------------CONSULTA ESPECIFICA - ALUNO -------------------')
            print()
            student3 = Estudent()
            student3.consultEstudents(False, 'name')
            print()

        elif option == 4:
            print('------------------------CONSULTA ESPECIFICA - CPF(ALUNO) -------------------')
            print()
            student4 = Estudent()
            student4.consultEstudents(False, 'cpf')
            print()

        elif option == 5:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES - ALUNO -------------------')
            print()
            student5 = Estudent()
            student5.UpdateStudent('values_all')
            print()

        elif option == 6:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES - NOME(ALUNO) -------------------')
            print()
            student6 = Estudent()
            student6.UpdateStudent('nome')
            print()

        elif option == 7:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES - CPF(ALUNO) -------------------')
            print()
            student7 = Estudent()
            student7.UpdateStudent('cpf')
            print()

        elif option == 8:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES - CURSO(ALUNO) -------------------')
            print()
            student8 = Estudent()
            student8.UpdateStudent('curso')
            print()

        elif option == 9:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES - CURSO(ALUNO) -------------------')
            print()
            student9 = Estudent()
            student9.deleteStudents()
            print()

        elif option == 10:
            student10 = Estudent()
            quantity = int(input('DESEJA CADASTRAR QUANTOS ESTUDENTES ?: '))
            student10.registerNotasStudents(quantity)

        elif option == 11:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES DE NOTAS - DO ALUNO -------------------')
            print()
            student11 = Estudent()
            student11.UpdateNotas('values_all')
            print()

        elif option == 12:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES DE NOTAS - MATRICULA -------------------')
            print()
            student12 = Estudent()
            student12.UpdateNotas('matricula')
            print()

        elif option == 13:
            print('------------------------ALTERAÇÃO DE INFORMAÇÕES DE NOTAS - NOTA -------------------')
            print()
            student13 = Estudent()
            student13.UpdateNotas('nota')
            print()



except KeyboardInterrupt as e:
    print(f'Programa encerrado pelo usuário: {e}')

finally:
    print('Programa executado com sucesso !')



