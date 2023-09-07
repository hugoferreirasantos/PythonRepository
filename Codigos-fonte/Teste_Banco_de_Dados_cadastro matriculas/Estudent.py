from Sql import Sql


class Estudent:

    # Atributos:
    def __init__(self):
        self.matricula = None
        self.nome = None
        self.dtnasc = None
        self.altura = None
        self.peso = None
        self.curso = None
        self.email = None

    # Metodos:
    # Métodos gets and sets
    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome

    def getDtnasc(self):
        return self.dtnasc

    def getAltura(self):
        return self.altura

    def getPeso(self):
        return self.peso

    def getCurso(self):
        return self.curso

    def getEmail(self):
        return self.email

    def setMatricula(self, value):
        self.matricula = value

    def setNome(self, value):
        self.nome = value

    def setDtnasc(self, value):
        self.dtnasc = value

    def setAltura(self, value):
        self.altura = value

    def setPeso(self, value):
        self.peso = value

    def setCurso(self, value):
        self.curso = value

    def setEmail(self, value):
        self.email = value

    # Método setar dados:
    def setData(self, quantity):
        data = []
        for row in range(quantity):
            nome = input('INSIRA O NOME: ')
            self.setNome(nome)

            date = input('INSIRA A DATA DE NASCIMENTO: ')
            self.setDtnasc(date)

            altura = input('INSIRA A ALTURA: ')
            self.setAltura(altura)

            peso = input('INSIRA O PESO: ')
            self.setPeso(peso)

            curso = input('INSIRA O CURSO: ')
            self.setCurso(curso)

            email = input('INSIRA O EMAIL: ')
            self.setEmail(email)

            data.append(
                (self.getNome(), self.getDtnasc(), self.getAltura(), self.getPeso(), self.getCurso(), self.getEmail()))

        return data

    # Método de cadastro de estudantes:
    def registerEstudents(self, quantity):
        sql = Sql()

        data = self.setData(quantity)

        query = '''
            INSERT INTO TBCADALUNOS(
            NOME,
            DTNASC,
            ALTURA,
            PESO,
            CURSO,
            EMAIL
            )
            VALUES(?,?,?,?,?,?);
        '''
        sql.insert(query, data)

    def consultEstudents(self, consult=True):

        if consult:
            sql = Sql()
            query = '''SELECT * FROM TBCADALUNOS'''
            consult = sql.select(query)
            for row in consult:
                print(f'Matricula: {row[0]:15} | Nome: {row[1]:15} | Data Nascimento: {row[2]:15} | Altura: {row[3]:15} | Peso: {row[4]:15} | ID Curso: {row[5]:15} | Email: {row[6]:15}')

        elif not consult:
            sql = Sql()
            nome = input('INSIRA UM NOME PARA PESQUISA: ')
            query = "SELECT * FROM TBCADALUNOS t WHERE t.NOME = '" + nome + "';"
            consult = sql.select(query)
            for row in consult:
                print(
                    f'Matricula: {row[0]:15} | Nome: {row[1]:15} | Data Nascimento: {row[2]:15} | Altura: {row[3]:15} | Peso: {row[4]:15} | ID Curso: {row[5]:15} | Email: {row[6]:15}')



