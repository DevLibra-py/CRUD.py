#Import das bibliotecas usadas no projeto
import os
from time import sleep

#Variável do tipo List ultilizada como banco de dados em memória
db_produto = []

#Função que chama a edição do cabeçalho no terminal
def header():
    print('*-' * 50)
    print('\n                                     BEM VINDO AO SISTEMA CRUD.py\n')
    print('*-' * 50)
    print('')


#Função que checa o tipo de sistema operacional e limpa a tela do terminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#Função que cadastra novos produtos e armazena-os em um Dict, adicionando-o db_produto[]
def cadastrar():
    clear()
    header()
    global db_produto
    while True:
        try:
            codigo = int(input('Digite o ID do produto: '))
            if codigo == int:
                break
            break
        except:
            print('\nPor favor digite apenas números.')
            sleep(1)
            clear()
            header()
    
    nome = input('Digite o NOME do produto: ').title()

    while True:
        try:
            preco = float(input('Digite o PREÇO do produto: '))
            if nome == float:
                break
            break
        except:
            print('\nPor favor digite apenas números utilizando o ponto " . " para separar os centavos dos reais.')
            sleep(2)
            clear()
            header()
            print(f'Digite o ID do produto: {codigo}')
            print(f'Digite o NOME do produto: {nome}')

    while True:
        try:
            quantidade = int(input('Digite a QUANTIDADE do produto: '))
            if quantidade == int:
                break
            break
        except:
            print('\nPor favor digite apenas números.')
            sleep(1)
            clear()
            header()
            print(f'Digite o ID do produto: {codigo}')
            print(f'Digite o NOME do produto: {nome}')
            print(f'Digite o PREÇO do produto: {preco}')    
    
    newProduto = {"id": codigo, "nome": nome, "preco" : preco, "quantidade": quantidade}
    db_produto.append(newProduto)
    print(f'\n{nome} foi cadastrado com sucesso!')
    sleep(2)


#Função que lista cada elemento Dict dentro da List de forma editada e ordenada pela Key 'id'
def consultar():
    clear()
    header()
    global db_produto
    db_produto.sort(key = lambda produto: produto['id'])
    for produto in db_produto:
        print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')


#Função que edita os elementos do Dict usando o filtro pela Key 'id'
def editar():
    clear()
    header()
    consultar()
    global db_produto
    while True:
        try:
            opcao = int(input('\nDigite o ID do produto que deseja editar: '))
            if opcao == int:
                break
            break
        except:
            print('\nPor favor digite apenas números.')
            sleep(1)
            clear()
            header()
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

            while True:
                try:
                    opcao2 = int(input('Digite a opção desejada: '))
                    if opcao2 == int:
                        break
                    break
                except:
                    print('\nPor favor digite apenas números.')
                    sleep(1)
                    clear()
                    header()
                    print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')
                    print('\n[1] - ID')
                    print('[2] - NOME')
                    print('[3] - PREÇO')
                    print('[4] - QUANTIDADE')
                    print('[5] - Para voltar ao menu\n')
            
            clear()
            header()
            print(f'ID: {produto["id"]} NOME: {produto["nome"]} PREÇO: {produto["preco"]} QUANTIDADE: {produto["quantidade"]}')
            print('\n[1] - ID')
            print('[2] - NOME')
            print('[3] - PREÇO')
            print('[4] - QUANTIDADE')
            print('[5] - Para voltar ao menu\n')
            
            if opcao2 == 1:
                newId = int(input('Digite o novo ID: '))
                produto['id'] = newId
                print('\nID alterado com sucesso!')
                sleep(2)
            elif opcao2 == 2:
                newName = input('Digite o novo NOME: ').title()
                produto['nome'] = newName
                print('\nNOME alterado com sucesso!')
                sleep(2)
            elif opcao2 == 3:
                newPrice = float(input('Digite o novo PREÇO: '))
                produto['preco'] = newPrice
                print('\nPREÇO alterado com sucesso!')
                sleep(2)
            elif opcao2 == 4:
                newQuantity = int(input('Digite o novo QUANTIDADE: '))
                produto['quantidade'] = newQuantity
                print('\nQUANTIDADE alterado com sucesso!')
                sleep(2)
            elif opcao2 == 5:
                pass


#Função que exclui o elemento Dict selecionado pela Key 'id' e excluído do elemento List através do index
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


#Produtos cadastrados de forma não interativa apenas para finalidade de testar o sistema
box = {"id": 1, "nome": "Feijão", "preco": 6.49, 'quantidade': 5}, {"id": 2, "nome": "Arroz", "preco": 2.98, 'quantidade': 10}, {"id": 3, "nome": "Macarrão", "preco": 4.25, 'quantidade': 2}
db_produto.extend(box)
print(db_produto)

#O menu inicial do programa onde conforme entrada do usuário, acessa as funções acima
while True:
    clear()
    header()
    print('[1] - Adicionar')
    print('[2] - Editar')
    print('[3] - Listar')
    print('[4] - Deletar')
    print('[5] - Sair\n')

    while True:
        try:
            opcao = int(input('Digite a opção: '))
            if opcao == int:
                break
            break
        except:
            print('\nPor favor digite apenas o número correspondente.')
            sleep(1)
            clear()
            header()
            print('[1] - Adicionar')
            print('[2] - Editar')
            print('[3] - Listar')
            print('[4] - Deletar')
            print('[5] - Sair\n')
        
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

