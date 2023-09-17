from Sql import Sql


class Estudent:

    # Atributos:
    def __init__(self):
        self.matricula = None
        self.nome = None
        self.cpf = None
        self.curso = None
        self.item = None
        self.id_matricula = None
        self.nota = None

    # Metodos:
    # Métodos gets and sets
    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def getCurso(self):
        return self.curso

    def getItem(self):
        return self.item

    def getId_matricula(self):
        return self.id_matricula

    def getNota(self):
        return self.nota

    def setMatricula(self, value):
        self.matricula = value

    def setNome(self, value):
        self.nome = value

    def setCpf(self, value):
        self.cpf = value

    def setCurso(self, value):
        self.curso = value

    def setItem(self, value):
        self.item = value

    def setId_matricula(self, value):
        self.id_matricula = value

    def setNota(self, value):
        self.nota = value

    # Método: Create Table(cria as tabelas ALUNOS E NOTAS)
    def createTables(self):

        try:
            sql = Sql();

            tableStudent = '''
                        CREATE TABLE ALUNOS (
                            matricula INTEGER PRIMARY KEY NOT NULL,
                            nome TEXT NOT NULL,
                            cpf varchar(12) NOT NULL,
                            curso TEXT NOT NULL
                        );
                    '''

            sql.create_table(tableStudent)

            tableNotas = '''
                        CREATE TABLE IF NOT EXISTS NOTAS(
                            item INTEGER PRIMARY KEY NOT NULL,
                            matricula INTEGER NOT NULL,
                            nota REAL NOT NULL,
                            FOREIGN KEY (matricula)
                            REFERENCES ALUNOS (matricula) 
                        );
                    '''

            sql.create_table(tableNotas)

            print('--------------------| TABELAS CRIADAS COM SUCESSO |-------------------------')

        except sql.conn.OperationalError as error:
            print(f"---------------| TABELAS JÁ CRIADA |---------:")
            print(f'{error}')



        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()

    # Método setar dados:
    def setDataEstudents(self, quantity):
        try:
            data = []
            for row in range(quantity):
                nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                if nome == '':
                    while nome == '':
                        print('Atenção: é preciso informar o nome do aluno')
                        nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                self.setNome(nome)

                cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not len(cpf) == 11:
                    while not len(cpf) == 11:
                        print('São permitidos somente 11 números no CPF, digite novamente: ')
                        cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not cpf.isdigit():
                    while not cpf.isdigit():
                        print('Erro: o cpf do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        cpf = input('INSIRA O NOME DO ALUNO: ').strip()
                        if not cpf.isdigit():
                            print(
                                'Erro o nome do aluno não pode conter caracteres númericos e não poder ter valor '
                                'vazio !')
                            nome = input('INSIRA O NOME DO ALUNO: ').strip()
                self.setCpf(cpf)

                curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                if curso == '':
                    while curso == '':
                        print('Atenção: é preciso inserir o nome do curso do aluno !')
                        curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                self.setCurso(curso)

                print('-----------------------------------------------------------------------------------------------')

                data.append(
                    (self.getNome(), self.getCpf(), self.getCurso()))

            return data

        except SyntaxError as e:
            print(f'Erro: Ocorreu um erro de Sintaxe: {e}')
            print('digite F5 para voltar a tela de cadastro')

    # Método de cadastro de estudantes:
    def registerEstudents(self, quantity):
        try:
            sql = Sql()

            data = self.setDataEstudents(quantity)

            query = '''
                        INSERT INTO ALUNOS(
                        NOME,
                        CPF,
                        CURSO
                        )
                        VALUES(?,?,?);
                    '''

            sql.insert(query, data)

            print('Cadastro realizado com sucesso !')

        except sql.conn.OperationalError as e:
            print(f'Erro: {e}')

        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()
                print('Digite F5 para iniciar ir para a tela principal:')

    def consultEstudents(self, consult=True, type=None):

        try:

            if consult and type == 'all':
                sql = Sql()
                query = '''SELECT * FROM ALUNOS;'''
                consult = sql.select(query)
                for row in consult:
                    print(
                        f'Matricula: {row[0]:15} | Nome: {row[1]:15} | CPF : {row[2]:15} | Curso: {row[3]:15} ')

            elif not consult and type == 'name':
                sql = Sql()
                nome = input('INSIRA UM NOME PARA PESQUISA: ').upper()
                if nome == '':
                    while nome == '':
                        print('Atenção: é necessário informar um nome para consulta: ')
                        nome = input('INSIRA UM NOME PARA PESQUISA: ').upper()
                query = "SELECT * FROM ALUNOS t WHERE t.NOME = '" + nome + "';"
                consult = sql.select(query)
                if consult:
                    for row in consult:
                        print('----------------------------CONSULTA---------------------------------------------------')
                        print(
                            f'Matricula: {row[0]:15} | Nome: {row[1]:20} | CPF : {row[2]:20} | Curso: {row[3]:20} ')
                else:
                    print('Nenhum resultado encontrado para a consulta.')

            elif not consult and type == 'cpf':
                sql = Sql()
                cpf = input('INSIRA UM CPF PARA CONSULTA: ').strip()
                if cpf == '':
                    while cpf == '':
                        print('Atenção: é necessário informar um cpf para consulta: ')
                        cpf = input('INSIRA UM CPF PARA PESQUISA: ').strip()
                query = "SELECT * FROM ALUNOS t WHERE t.CPF = '" + cpf + "';"
                consult = sql.select(query)
                if consult:
                    for row in consult:
                        print('----------------------------CONSULTA---------------------------------------------------')
                        print(
                            f'Matricula: {row[0]:15} | Nome: {row[1]:20} | CPF : {row[2]:20} | Curso: {row[3]:20} ')
                else:
                    print('Nenhum resultado encontrado para a consulta.')


        except sql.conn.OperationalError as e:
            print(f'Erro:  {e}')


        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()

    def UpdateStudent(self, comandType=None):

        global sql
        try:
            sql = Sql()

            if comandType == 'values_all':

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                if nome == '':
                    while nome == '':
                        print('Atenção: é preciso informar o nome do aluno')
                        nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                self.setNome(nome)

                cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not len(cpf) == 11:
                    while not len(cpf) == 11:
                        print('São permitidos somente 11 números no CPF, digite novamente: ')
                        cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not cpf.isdigit():
                    while not cpf.isdigit():
                        print('Erro: o cpf do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                        if not cpf.isdigit():
                            print(
                                'Erro o nome do aluno não pode conter caracteres númericos e não poder ter valor '
                                'vazio !')
                            cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                self.setCpf(cpf)

                curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                if curso == '':
                    while curso == '':
                        print('Atenção: é preciso inserir o nome do curso do aluno !')
                        curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                self.setCurso(curso)

                print('-----------------------------------------------------------------------------------------------')

                query = '''
                            UPDATE ALUNOS  
                            SET NOME = :nome,
                            CPF = :cpf,
                            CURSO = :curso
                            WHERE MATRICULA = :matricula;
                        '''

                sql.update(query, {'matricula': self.getMatricula(), 'nome': self.getNome(), 'cpf': self.getCpf(),
                                   'curso': self.getCurso()})

                print('DADOS ALTERADO COM SUCESSO !')

            if comandType == 'nome':

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                if nome == '':
                    while nome == '':
                        print('Atenção: é preciso informar o nome do aluno')
                        nome = input('INSIRA O NOME DO ALUNO : ').upper().strip()
                self.setNome(nome)

                print('-----------------------------------------------------------------------------------------------')

                query = '''
                            UPDATE ALUNOS  
                            SET NOME = :nome
                            WHERE MATRICULA = :matricula;
                        '''

                sql.update(query, {'matricula': self.getMatricula(), 'nome': self.getNome()})

                print('DADOS ALTERADO COM SUCESSO !')

            if comandType == 'cpf':

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not len(cpf) == 11:
                    while not len(cpf) == 11:
                        print('São permitidos somente 11 números no CPF, digite novamente: ')
                        cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                if not cpf.isdigit():
                    while not cpf.isdigit():
                        print('Erro: o cpf do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                        if not cpf.isdigit():
                            print(
                                'Erro o nome do aluno não pode conter caracteres númericos e não poder ter valor '
                                'vazio !')
                            cpf = input('INSIRA O CPF DO ALUNO: ').strip()
                self.setCpf(cpf)
                print('-----------------------------------------------------------------------------------------------')

                query = '''
                            UPDATE ALUNOS  
                            SET CPF = :cpf
                            WHERE MATRICULA = :matricula;
                        '''

                sql.update(query, {'matricula': self.getMatricula(), 'cpf': self.getCpf()})

                print('DADOS ALTERADO COM SUCESSO !')

            if comandType == 'curso':

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                if curso == '':
                    while curso == '':
                        print('Atenção: é preciso inserir o nome do curso do aluno !')
                        curso = input('INSIRA O NOME DO CURSO  DO ALUNO: ').upper().strip()
                self.setCurso(curso)

                print('-----------------------------------------------------------------------------------------------')

                query = '''
                            UPDATE ALUNOS  
                            SET CURSO = :curso
                            WHERE MATRICULA = :matricula;
                        '''

                sql.update(query, {'matricula': self.getMatricula(), 'curso': self.getCurso()})

                print('DADOS ALTERADO COM SUCESSO !')

        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()

    def deleteStudents(self):

        global sql
        try:
            sql = Sql()
            print('1 - EXCLUIR UM ALUNO: ')
            print('2 - CANCELAR A EXCLUSÃO: ')
            print()
            option = input('DIGITE A OPÇÃO: ')
            while option == '':
                print('Escolha uma opção :')
                option = input('DIGITE A OPÇÃO: ')
            option = int(option)

            while option == 1:
                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                while not matricula.isdigit():
                    print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                    matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                print('Deseja mesmo excluir esse aluno ?')
                print('1 para SIM')
                print('2 para NÃO ')

                option2 = input('Digite aqui a opção: ')
                while option2 == '':
                    option2 = input('Digite aqui a opção: ')
                option2 = int(option2)

                if option2 == 1:
                    query = '''
                            DELETE FROM ALUNOS WHERE matricula = :matricula;
                    '''
                    sql.delete(query, {'matricula': self.getMatricula()})

                    sql2 = Sql()
                    query2 = '''
                        DELETE FROM NOTAS WHERE matricula = :matricula;
                    '''
                    sql2.delete(query2, {'matricula': self.getMatricula()})

                    print('Matricula, excluída com sucesso !')
                    break

                elif option2 == 2:
                    print('Operação de exclusão encerrada: ')
                    break

            if option == 2:
                print('Operação cancelada com sucesso!')

        except sql.conn.ProgrammingError as e:
            print(f'Erro na programação: {e}')
        except sql.conn.AttributeError as e:
            print(f'Erro na entrada de atributo: {e}')
        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()


    def setDataNotas(self, quantity):
        try:
            data = []
            for row in range(quantity):

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                nota = input('INSIRA A NOTA DO ALUNO: ').strip()
                if not nota.isdigit():
                    while not nota.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        float(nota)
                        if not nota.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                            float(nota)
                self.setNota(nota)

                print('-----------------------------------------------------------------------------------------------')

                data.append(
                    (self.getMatricula(), self.getNota()))

            return data

        except SyntaxError as e:
            print(f'Erro: Ocorreu um erro de Sintaxe: {e}')
            print('digite F5 para voltar a tela de cadastro')


    def registerNotasStudents(self, quantity):
        try:
            sql = Sql()

            data = self.setDataNotas(quantity)

            query = '''
                        INSERT INTO NOTAS(
                        MATRICULA,
                        NOTA
                        )
                        VALUES(?,?);
                    '''

            sql.insert(query, data)

            print('Cadastro realizado com sucesso !')

        except sql.conn.OperationalError as e:
            print(f'Erro: {e}')

        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()
                print('Digite F5 para iniciar ir para a tela principal:')

    def UpdateNotas(self, comandType=None):

        global sql
        try:
            sql = Sql()

            if comandType == 'values_all':

                item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                if not item.isdigit():
                    while not item.isdigit():
                        print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                        item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                        if not item.isdigit():
                            print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                            item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()

                self.setItem(item)

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                nota = input('INSIRA A NOTA DO ALUNO: ').strip()
                if not nota.isdigit():
                    while not nota.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        float(nota)
                        if not nota.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                            float(nota)
                self.setNota(nota)





                print('-----------------------------------------------------------------------------------------------')

                query = '''
                               UPDATE NOTAS
                               SET MATRICULA = :matricula,
                               NOTA= :nota
                               WHERE ITEM = :item ;
                           '''

                sql.update(query, {'matricula': self.getMatricula(), 'nota': self.getNota(), 'item':self.getItem()})

                print('DADOS ALTERADO COM SUCESSO !')

            if comandType == 'matricula':

                item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                if not item.isdigit():
                    while not item.isdigit():
                        print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                        item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                        if not item.isdigit():
                            print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                            item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()

                self.setItem(item)

                matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                if not matricula.isdigit():
                    while not matricula.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        if not matricula.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            matricula = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                self.setMatricula(matricula)

                print('-----------------------------------------------------------------------------------------------')

                query = '''
                               UPDATE NOTAS 
                               SET MATRICULA = :matricula
                               WHERE item = :item;
                           '''

                sql.update(query, {'matricula': self.getMatricula(), 'item': self.getItem()})

                print('DADOS ALTERADO COM SUCESSO !')

            if comandType == 'nota':

                item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                if not item.isdigit():
                    while not item.isdigit():
                        print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                        item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()
                        if not item.isdigit():
                            print('Erro: o item deve conter apenas digitos e não pode ter valor vazio !')
                            item = input('INSIRA O ITEM DA TABELA NOTAS: ').strip()

                self.setItem(item)

                nota = input('INSIRA A NOTA DO ALUNO: ').strip()
                if not nota.isdigit():
                    while not nota.isdigit():
                        print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                        nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                        float(nota)
                        if not nota.isdigit():
                            print('Erro: a matricula do aluno deve conter apenas digitos e não pode ter valor vazio !')
                            nota = input('INSIRA A MATRICULA DO ALUNO: ').strip()
                            float(nota)
                self.setNota(nota)
                print('-----------------------------------------------------------------------------------------------')

                query = '''
                               UPDATE NOTAS
                               SET NOTA = :nota
                               WHERE ITEM = :item;
                           '''

                sql.update(query, {'nota': self.getNota(), 'item': self.getItem()})

                print('DADOS ALTERADO COM SUCESSO !')

        except sql.conn.OperationalError as e:
            print(f'Erro: {e}')
        finally:
            if sql.conn:
                sql.cursor.close()
                sql.conn.close()





