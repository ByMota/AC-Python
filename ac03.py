# ATIVIDADE CONTÍNUA 03

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Vinicius Camargo
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        try:
            self.__poderes.append(superpoder)
        except ValueError:
            pass

    def get_poder_total(self):
        sum(self.__poderes)


class SuperHeroi(Personagem):
    def __init__(self, nome, nome_vida_real):
        super().__init__(nome, nome_vida_real)

    def get_poder_total(self):
        heroi = SuperHeroi.get_poder_total() * 1.10
        return heroi


class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:
    def lutar(self, heroi, vilao):
        if SuperHeroi.get_poder_total() >  Vilao.get_poder_total():
            return 1
        elif Vilao.get_poder_total() > SuperHeroi.get_poder_total():
            return 2
        else:
            return 0 
