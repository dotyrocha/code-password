# Importrando Modulos
from biblioteca import *

# Montando Layout
titulo('CRIPTO')
space()

# Lista de Dados para codificar
alfabeto = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5',
            'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

while True:

    space()
    code = int(input('[1] CODIFICAR \n[2] DESCDIFICAR \n\n: '))

    if code == 1:
        # Inserção da Mensagem
        quebralinha()
        mensagem = str(input('CODIFICAR: ')).lower().strip()
        space()
        quebralinha()
        space()

        # Padrao de cifra
        c = len(alfabeto)
        chave = 3

        # Algoritimo de Codificacao
        cifrada = ''
        for letra in mensagem:
            indice = alfabeto.index(letra)
            nova_letra = alfabeto[(indice + chave) % c]
            cifrada = cifrada + nova_letra

        # Entrega da Mensagem Codificada
        print('RESULTADO :{}'.format(cifrada))
        space()

    elif code == 2:
        # Inserção da Mensagem
        space()
        quebralinha()
        space()
        mensagem = str(input('DESCODIFICAR: ')).lower().strip()
        space()
        quebralinha()
        space()
        # Padrao de cifra
        c = len(alfabeto)
        chave = - 3

        # Algoritimo de Desodificacao
        cifrada = ''
        for letra in mensagem:
            indice = alfabeto.index(letra)
            nova_letra = alfabeto[(indice + chave) % c]
            cifrada = cifrada + nova_letra

        # Entrega da Mensagem Descodificada
        print('RESULTADO :{}'.format(cifrada))
        space()
    quebralinha()
    r = str(input('Quer usar denovo (y/n) :'))

    if r == 'n':
        space()
        quebra('-')
        print('Obrigado por usar :) \n\nFeito por André Rocha')
        quebra('-')
        space()
        sair = input('Pressione qualquer tela para sair')
        break

