import os

'''Este é um dicionário dos restaurantes'''
restaurantes = [{'nome': 'Papa´s Pizzaria', 'categoria':'Italiana', 'ativo':False},
                {'nome':'Cantina', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Milk Sorvetes', 'categoria':'Belgo', 'ativo': True}]

def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela'''
    print("""
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Finalizando o programa')

def finalizar_app():
    '''Exibe a memsagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
     '''Solicita uma tecla para voltar ao menu principal
        
        Outputs:
        - Retorna ao menu principal
     '''
     input('\nDigite uma tecla para voltar ao menu principal')
     main()

def opcao_invalida():
    '''Exibe a mensagem de opção inválida e retorn ao menu principal
    
       Outputs: 
       - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe um subtitulo estilizado na tela
       
       Inputs:
       - testo: str = O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função cadastra um novo restaurante
        Inputs: 
        - Nome do restaurante
        - Categoria do restaurante
        
        Outputs: 
        - Adiciona um novo restaurante a lista de restaurantes 
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 
                             'categoria': categoria_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista
        
        Outputs: 
        - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando os restaurantes\n')
    
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(22)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljus(20)} | {ativo_restaurante}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante
        
        Outputs: 
        - exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado: 
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção pelo usuário
        Outputs:
        -Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        # print(opcao_escolhida == 1)
        # print(type(opcao_escolhida))
        # print(type(1))

        if opcao_escolhida == 1 : 
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a função principal que inicia o programa'''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' : 
    main()

# Se decidirmos utilizar a instrução match nesse caso, obteríamos o seguinte resultado: 
# opcao_escolhida = int(input('Escolha uma opção: '))
# match opcao_escolhida:
    # case 1:
        # print('Adicionar restaurante')
    # case 2:
        # print('Listar restaurantes')
    # case 3:
        # print('Ativar restaurante')
    # case 4:
        # print('Finalizar app')
    # case _:
        # print('Opção inválida!')
