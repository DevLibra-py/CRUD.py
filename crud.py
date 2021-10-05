import os
from time import sleep

db_produto = []

def header():
    print('*-' * 50)
    print('\n                                     BEM VINDO AO SISTEMA CRUD.py\n')
    print('*-' * 50)
    print('')


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cadastrar():
    clear()
    header()
    global db_produto
    codigo = int(input('Digite o ID do produto: '))
    nome = input('Digite o NOME do produto: ').title()
    preco = float(input('Digite o PREÇO do produto: '))
    quantidade = int(input('Digite a QUANTIDADE do produto: '))
    newProduto = {"id": codigo, "nome": nome, "preco" : preco, "quantidade": quantidade}
    db_produto.append(newProduto)
    print(f'\n{nome} foi cadastrado com sucesso!')
    sleep(2)


def consultar():
    clear()
    header()
    global db_produto
    db_produto.sort(key = lambda produto: produto['id'])
    for produto in db_produto:
        produto = produto
        print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')


def editar():
    clear()
    header()
    consultar()
    global db_produto
    opcao = int(input('\nDigite o ID do produto que deseja editar: '))
    clear()
    header()
    for produto in db_produto:
        if produto['id'] == opcao:
            print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')
            print('\n[1] - ID')
            print('[2] - NOME')
            print('[3] - PREÇO')
            print('[4] - QUANTIDADE')
            print('[5] - Para voltar ao menu\n')
            opcao2 = int(input('Digite a opção desejada: '))
            if opcao2 == 1:
                newId = int(input('Digite o novo ID: '))
                produto['id'] = newId
                print('ID alterado com sucesso!')
                sleep(2)
            elif opcao2 == 2:
                newName = input('Digite o novo NOME: ').title()
                produto['nome'] = newName
                print('NOME alterado com sucesso!')
                sleep(2)
            elif opcao2 == 3:
                newPrice = float(input('Digite o novo PREÇO: '))
                produto['preco'] = newPrice
                print('PREÇO alterado com sucesso!')
                sleep(2)
            elif opcao2 == 4:
                newQuantity = int(input('Digite o novo QUANTIDADE: '))
                produto['quantidade'] = newQuantity
                print('QUANTIDADE alterado com sucesso!')
                sleep(2)
            elif opcao2 == 5:
                pass


def deletar():
    clear()
    header()
    consultar()
    global db_produto
    opcao = int(input('\nDigite o ID do produto que deseja deletar: '))
    clear()
    header()
    for produto in db_produto:
        if produto['id'] == opcao:
            posicao = db_produto.index(produto)
            print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')
            print('\nTem certeza que deseja excluir o produto selecionado?')
            opcao2 = input('Digite "S" para SIM ou "N" para NÃO: ').upper()
            if opcao2 == 'S':
                del db_produto[posicao]
                print('\nProduto excluído com sucesso!')
                sleep(2)
            elif opcao2 == 'N':
                pass

box = {"id": 1, "nome": "Feijão", "preco": 6.49, 'quantidade': 5}, {"id": 2, "nome": "Arroz", "preco": 2.98, 'quantidade': 10}, {"id": 3, "nome": "Macarrão", "preco": 4.25, 'quantidade': 2}
db_produto.extend(box)
print(db_produto)


while True:
    clear()
    header()
    print('[1] - Adicionar')
    print('[2] - Editar')
    print('[3] - Listar')
    print('[4] - Deletar')
    print('[5] - Sair\n')

    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        consultar()
        input('\nPresione ENTER para voltar ao menu!')
    elif opcao == 4:
        deletar()
    elif opcao == 5:
        break
    else:
        print('Você digitou uma opção inválida!')
        sleep(2)

