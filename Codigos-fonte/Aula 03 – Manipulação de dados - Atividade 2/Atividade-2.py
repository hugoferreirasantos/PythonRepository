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

def save_student(name, email, course):
    with open('students.txt', 'a') as file:
        file.write(f'{name},{email},{course}\n')

def read_students():
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as file:
            lines = file.readlines()
            return [tuple(line.strip().split(',')) for line in lines]
    return []

def find_student(name):
    students = read_students()
    for student in students:
        if student[0] == name:
            return student
    return None

def print_student(student):
    print(f'Name: {student[0]}, Email: {student[1]}, Course: {student[2]}')

def print_menu():
    print('1. Register a new student')
    print('2. List registered students')
    print('3. Find a student by name')
    print('4. Exit')

def main():
    while True:
        print_menu()
        option = int(input('Enter an option: '))
        if option == 1:
            quant = int(input("Enter the number of students you want to register"))
            for element in range(quant):
                name = input('Enter the student\'s name: ')
                email = input('Enter the student\'s email: ')
                course = input('Enter the student\'s course: ')
                save_student(name, email, course)
                print('Student registered successfully!')

        elif option == 2:
            students = read_students()
            for student in students:
                print_student(student)
        elif option == 3:
            name = input('Enter the student\'s name: ')
            student = find_student(name)
            if student:
                print_student(student)
            else:
                print('Student not found')
        elif option == 4:
            break

if __name__ == '__main__':
    main()