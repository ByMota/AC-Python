# ATIVIDADE CONTÍNUA 02

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


class Socio:
    def __init__(self, nome, nascimento, cpf, mes, ano):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.mes = mes
        self.ano = ano



class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, socio):
        self.socios.append(socio) #Correto

    def numero_de_socios(self):
        return len(self.socios) #Correto

    def mes_associacao (self,mes, ano):

        '''Ainda não está contando, apenas quero verificar se ele pega o indice'''
        for i in range(len(self.socios)):
            print(self.socios[i][4])
            print(self.socios[i][5])

        if mes not in range(1, 12):
            raise ValueError #Correto

        if ano not in len(4):
            raise TypeError #Correto

        else:
            return 0 #Correto

    def expulsar (self, mes, ano):
        expulsos = ()
        if mes < 1 or mes > 12:
            raise ValueError #Correto

        if ano not in len(4):
            raise TypeError #Correto

        #Expulsar vai aqui

        else:
            return expulsos #Correto
