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
    
def cadastrar_novo_restaurante():
    '''  Função para cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    Outputs:
    - Adiciona o restaurante à lista de restaurantes
    '''
    os.system('cls')
    exibir_subtitulo('----- Cadastro de Novos Restaurante -----')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante "{nome_do_restaurante}": ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}  # Cria um dicionário com os dados do restaurante
    restaurantes.append(dados_do_restaurante)  # Adiciona o dicionário à lista de restaurantes
    print(f'Restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    print('------------------------------------------\n')
    voltar_ao_menu()
    
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    os.system('cls')
    exibir_subtitulo('----- Lista de Restaurantes -----')

    print(f'NOME DO RESTAURANTE'.ljust(23) + '| CATEGORIA'.ljust(23) + '| STATUS')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    print('-------------------------------------------------------------------')
    voltar_ao_menu()
    
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu()
    
def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()   
        
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()