# 2. Voltando ao cenário apresentado na situação-problema, que trata de um sistema de registro de
# notas de alunos em uma pequena instituição de ensino, desenvolver uma solução capaz de
# persistir (inserir) e ler os dados de notas de alunos em arquivos.

#  O programa deve registrar o nome, email e curso do aluno.
#  Cada novo registro deve ser armazenado em arquivo.
#  O usuário deve ter as seguintes opções:
#    Cadastrar um novo aluno.
#    Listar os alunos cadastrados.
#    Buscar um aluno pelo nome.


# _______________________________________________________

import os
import re


def save_student(registration, name, email, course):
    with open('students.txt', 'a') as file:
        file.write(f'{registration},{name},{email},{course}\n')


def read_students():
    filename = 'students.txt'
    if os.path.exists(filename):
        with open('students.txt', 'r') as file:
            lines = file.readlines()
            return [tuple(line.strip().split(',')) for line in lines]
    else:
        print(f'Erro: O arquivo {filename} não existe')
    return []


def find_student(name):
    students = read_students()
    for student in students:
        if student[1] == name:
            return student
    return None


def print_student(student):
    print(f'Registration: {student[0]} Name: {student[1]}, Email: {student[2]}, Course: {student[3]}')


def print_menu():
    print('1. Register a new student')
    print('2. List registered students')
    print('3. Find a student by name')
    print('4. Exit')


def onScreenDisplay():
    while True:
        print_menu()
        option = int(input('Enter an option: '))
        if option == 1:
            quant = int(input("Enter the number of students you want to register: "))
            for element in range(quant):

                registration = input('Enter the registration of student: ').strip()
                if not registration.isdigit():
                    while not registration.isdigit():
                        print('Erro: O número da matricula deve conter apenas digitos e não pode ter valor vazio: ')
                        registration = input('  Enter the registration of student: ').strip()
                        if not registration.isdigit():
                            print('Erro: O número da matricula deve conter apenas digitos e não pode ter valor vazio: ')
                            registration = input('  Enter the registration of student: ').strip()

                name = input('Enter the student\'s name: ').strip()
                if not name.isalpha():
                    while not name.isalpha():
                        print('Erro o nome do aluno não pode conter caracteres númericos e não poder ter valor vazio: ')
                        name = input('Enter the student\'s name: ').strip()
                        if not name.isalpha():
                            print('Erro o nome do aluno não pode conter caracteres númericos e não poder ter valor vazio: ')
                            name = input('Enter the student\'s name: ').strip()

                email = input('Enter the student\'s email: ').strip()
                if email == '':
                    while email == '':
                        print('Erro: digite um valor valido:  ')
                        email = input('Enter the student\'s email: ').strip()

                course = input('Enter the student\'s course: ').strip()
                if course == '':
                    while course == '':
                        print('Erro: digite um valor valido: ')
                        course = input('Enter the student\'s course: ').strip()

                save_student(registration, name, email, course)
                print('Student registered successfully!')

        elif option == 2:
            students = read_students()
            for student in students:
                print_student(student)
        elif option == 3:
            name = input('Enter the student\'s name: ')
            student = find_student(name)
            if student is not None:
                print_student(student)
            else:
                print('Student not found')
        elif option == 4:
            break





def main():
    try:
        onScreenDisplay()
        pass
    except ValueError as e:
        print(f'Ocorreu o seguinte erro: {e} , insira um valor valido.')
        flag = True
        while flag:
            try:
                onScreenDisplay()
                pass
            except ValueError as e:
                print(f'Ocorreu o seguinte erro: {e} , insira um valor valido.')
                flag = True
                while flag:
                    try:
                        onScreenDisplay()
                        pass
                    except ValueError:
                        onScreenDisplay()
                        break
                    break
            break
    except FileNotFoundError as e:
        print(f'Ocorreu o seguinte erro: {e}, não é possível ler um arquivo inextente')

    except KeyboardInterrupt as e:
        print(f'Ocorreu o seguinte erro: {e}, o programa foi encerrado pelo usuário: ')



if __name__ == '__main__':
    main()