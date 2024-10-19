import os, datetime, textwrap

def menu():
    menu = ''' \n    
    ============== MENU ==============
    ==================================
    [0]\t Depositar
    [1]\t Sacar
    [2]\t Extrato
    [3]\t Criar usuário
    [4]\t Criar conta
    [5]\t Listar contas
    [6]\t Sair
    ==================================
    -> '''
    return int(input(textwrap.dedent(menu))) 
    #retorna o que o usuário digitou


def op_deposito(saldo, deposito, extrato, qtde_transacoes, /):  #os argumentos são passados apenas por posição    
        while deposito <= 0:
            deposito = float(input('Valor inválido! Digite novamente: '))

        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"Depósito: R$ {deposito:.2f}  \tData: {horario}\n"
        saldo += deposito
        qtde_transacoes += 1
        print('\n=== Depósito realizado com sucesso ===')

        return saldo, extrato, qtde_transacoes


def op_saque(*, saldo, saque, extrato, limite, qtde_transacoes, numero_saques): #os argumentos são passados apenas por nome
        while saque > saldo or saque > limite or saque <= 0:
            saque = float(input('Saque inválido! Digite outro valor: '))
        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"Saque: R$ {saque:.2f}  \tData: {horario}\n"
        numero_saques += 1
        saldo -= saque
        qtde_transacoes += 1
        print('\n=== Saque realizado com sucesso ===')       

        return saldo, extrato, qtde_transacoes, numero_saques

def op_extrato(saldo, extrato):
    os.system('clear')
    print('\n==================== EXTRATO ====================')
    print('=================================================')
    print('Não foram realizadas movimentações' if not extrato else extrato) #se o extrato estiver vazio, exibe a mensagem 'Não foram realizadas movimentações'
    print(f'\nSaldo atual: R$ {saldo:.2f}', end='\n=================================================\n')

def criar_usuario(lista_usuarios):
    cpf = int(input('Digite o CPF (somente números): '))
    usuario = filtrar_usuarios(cpf, lista_usuarios)

    if usuario:
        print('\n@@@ Já existe um usuário com esse CPF! @@@')
        return

    nome = input('Digite o nome: ')
    data_nasc = input('Digite a data de nascimento (dd-mm-aa): ')
    endereco = input('Digite o endereço (logradouro, número - bairro - cidade/sigla estado): ')
    lista_usuarios.append({"nome": nome, "data": data_nasc, "cpf": cpf, "endereco": endereco})
    print('\n=== Usuário criado com sucesso! ===')
    
    return lista_usuarios

def filtrar_usuarios(cpf, lista_usuarios): 
    #confere cada item na lista de usuarios, e se encontrar um CPF igual ao informado, retorna o usuário correspondente
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(lista_usuarios, lista_contas, agencia, conta):
    cpf = int(input('Informe o CPF do usuário: '))
    usuario = filtrar_usuarios(cpf, lista_usuarios)

    if usuario:
        lista_contas.append({"agencia": agencia, "conta": conta, "usuario": usuario}) #adiciona um dicionário na lista, sendo q 'usuario' também é um dicionário
        print('\n=== Conta criada com sucesso! ===')
        conta += 1
    else:
        print('\n@@@ Usuário não encontrado! @@@')

    return conta
    
def listar_contas(lista_contas):
    os.system('clear')

    menu = '''
    ============ LISTA DE CONTAS ============
    ========================================='''
    print(textwrap.dedent(menu))

    if not lista_contas:
        print('Não há contas cadastradas! \n') #se a lista estiver vazia, exibe isso
    else:
        for conta in lista_contas:
            print(f'Agência: \t\t{conta["agencia"]}') #procura a chave "agencia" em cada dicionário de lista_contas, e exibe o valor correspondente à chave
            print(f'Número da conta: \t{conta["conta"]}')
            print(f'Titular: \t\t{conta["usuario"]["nome"]}') #como "usuario" é um dicionário, procura a chave "nome" dentro de "usuario"
            print('========================================= ')

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    qtde_transacoes = 0
    conta = 1
    lista_usuarios = []
    lista_contas = []   
    LIMITE_SAQUES = 3   
    LIMITE_TRANSACOES = 10
    AGENCIA = "0001"

    while True:
        os.system('clear')
        opcao = menu() 

        if opcao == 0:   
            if qtde_transacoes == LIMITE_TRANSACOES:
                print('\n@@@ Limite diário de transações atingido! @@@')   
            else:
                deposito = float(input('Informe o valor do depósito: '))               
                saldo, extrato, qtde_transacoes = op_deposito(saldo, deposito, extrato, qtde_transacoes)
            

        elif opcao == 1:
            if saldo == 0: 
                print('\n@@@ Saldo insuficiente! @@@')  
            elif qtde_transacoes == LIMITE_TRANSACOES:
                print('\n@@@ Limite diário de transações atingido! @@@')  
            elif numero_saques == LIMITE_SAQUES:
                print('\n@@@ Limite de saques atingido! @@@') 
            else: 
                saque = float(input('Informe o valor do saque: '))
                saldo, extrato, qtde_transacoes, numero_saques = op_saque(
                    saldo = saldo,
                    saque = saque,
                    extrato = extrato, 
                    limite = limite,
                    qtde_transacoes = qtde_transacoes,
                    numero_saques = numero_saques)   

        elif opcao == 2:
            op_extrato(saldo, extrato)

        elif opcao == 3:
            criar_usuario(lista_usuarios)

        elif opcao == 4:
            conta = criar_conta(lista_usuarios, lista_contas, AGENCIA, conta)

        elif opcao == 5:
            listar_contas(lista_contas)

        elif opcao == 6:
            break

        else:
            print('\n@@@ Opção inválida! @@@')

        input("\nPressione ENTER para continuar...")

main()
print('\nTenha um bom dia!')
