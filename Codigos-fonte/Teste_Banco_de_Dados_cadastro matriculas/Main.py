from Sql import Sql
from Estudent import Estudent

import sqlite3 as connector


def print_screen():
    print('Bem vindo !')
    print('1 - Cadastrar aluno: ')
    print('2 - Consultar cadastro de estudentes: ')
    print()


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

