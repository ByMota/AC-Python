# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Vinicius Camargo Mota Morici
# ALUNO 2: Gabriel De A. Eiras medeiros
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''
lista = [2, 3, 4, 8, 7]


def pertence(lista, item1, item2):
    if item1 and item2 in lista:
        return True
    else:
        return False


print(pertence(lista, 3, 8))

'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma lista e dois itens (velho e novo) e retorna uma lista onde todas as
ocorrências A do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):

    for i in range(len(lista)):
        while lista[i] == velho:
            if lista[i] == velho:
                lista[i] = novo
    return(lista)


lista = [1, 2, 4, 6]
print(substituir(lista, 2, 5))

'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''
tupla = (5, 6, 5, 3, 5)


def posicoes(tupla, item):
    indice = []
    for i in enumerate(tupla):
        if i[1] == item:
            indice.append(i[0])

    return indice


print(posicoes(tupla, 5))

'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''


def reprovados(alunos):
    reprovado = []
    for key in alunos:
        lista_notas = alunos[key]
        media = sum(lista_notas) / len(lista_notas)
        if media < 6:
            reprovado.append(key)
    return reprovado


aluno = {'vitor': [5, 7, 8], 'ana': [5, 6, 7.5], 'Ana Paula': [3.5, 1.0, 6.5]}
print(reprovados(aluno))

'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o
dicionário sem alterações.
'''


def excluir_nota(alunos, nome):
    for i in alunos:
        if i == nome:
            alunos[i].pop(0)
            return alunos
    return alunos


notas_aluno = {'pedro': [5, 7, 8], 'martins': [5, 6, 7]
                , 'vitor': [3.5, 1.0, 6.5]}

print(excluir_nota(notas_aluno, 'pedro'))

'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menor_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a menor nota
de cada aluno.
'''


def menor_nota(alunos):
    menorDic = {}
    for value in alunos:
        menor = min(alunos[value])
        menorDic[value] = menor

    return menorDic


notas_aluno = {'pedro': [5, 7, 8], 'martins': [5, 6, 7], 'vitor': [3.5, 1.0, 6.5]}

print(menor_nota(notas_aluno))
