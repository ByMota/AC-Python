# ATIVIDADE CONTÍNUA 02

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Vinicius Camargo Mota Morici
# ALUNO 2: Vinicius Santos de Souza
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
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao(self, mes, ano):
        associados = 0
        for socio in self.socios:
            if(socio.mes == mes and socio.ano == ano):
                associados += 1
        if mes not in range(1, 12):
            raise ValueError
        if len(str(ano)) != 4:
            raise TypeError
        return associados

    def expulsar(self, mes, ano):
        lista = []
        lista_pop = []
        if mes < 1 or mes > 12:
            raise ValueError

        elif len(str(ano)) != 4:
            raise TypeError

        else:
            for index in range(len(self.socios)):
                if self.socios[index].mes == mes and self.socios[index].ano == ano:
                    lista_pop.append(self.socios[index])
                    lista.append(self.socios[index].nome)
            for x in lista_pop:
                self.socios.remove(x)
        return tuple(sorted((lista)))
