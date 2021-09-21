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
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao (self,mes, ano):
        if mes in self.socios and ano in self.socios:
            return self.socios.count(mes)

        if mes not in range(1, 12):
            raise ValueError
        if ano not in len(4):
            raise TypeError
        else:
            return 0
    def expulsar (self, mes, ano):
        expulsos = []
        '''if mes in self.socios and ano in self.socios:
            self.socios.pop()
            self.socios.append(expulsos)
            return sorted(expulsos)'''
        if mes < 1 or mes >12:
            raise ValueError
        if ano not in len(4):
            raise TypeError
        else:
            return expulsos
