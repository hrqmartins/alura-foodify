import os

restaurantes = [{'nome' : 'Sushien', 'categoria':'Japonesa', 'ativo':True}, 
                {'nome' : 'Burger King', 'categoria':'Fast Food', 'ativo':False},
                {'nome' : 'Pizza Hut', 'categoria':'Italiana', 'ativo':False}]  # Lista de restaurantes, cada restaurante é um dicionário

# Menu
def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("\033[38;5;124m"
"""
      
█▀▀ █▀█ █▀█ █▀▄ █ █▀▀ █▄█
█▀░ █▄█ █▄█ █▄▀ █ █▀░ ░█░

"""
    "\033[0m")

def exibir_opcoes():
    ''' Exibe as opções do menu principal '''
    print('-------------------------')
    print('\033[1;37m[1]\033[0m Cadastrar Restaurante')
    print('\033[1;37m[2]\033[0m Listar Restaurantes')
    print('\033[1;37m[3]\033[0m Modificar Status do Restaurante')
    print('\033[1;37m[4]\033[0m Sair')
    print('-------------------------\n')

# Função para encerrar o aplicativo
def encerrar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Encerrando o Foodify...')

def voltar_ao_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('Pressione ENTER para voltar ao menu principal...')
    main()
    
# Função para exibir mensagem de opção inválida
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida! Por favor, escolha uma opção válida.')
    voltar_ao_menu()