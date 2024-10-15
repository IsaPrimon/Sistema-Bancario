import os, datetime, textwrap

def menu():
    menu = ''' \n    
    ****************************
               MENU
    ****************************
    [0]\t Depositar
    [1]\t Sacar
    [2]\t Extrato
    [3]\t Sair
    ****************************
    -> '''
    return int(input(textwrap.dedent(menu))) 
    


def op_deposito(saldo, deposito, extrato, qtde_transacoes, /):         
        while deposito <= 0:
            deposito = float(input('Valor inválido! Digite novamente: '))
        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"Depósito: R$ {deposito:.2f}  \tData: {horario}\n"
        saldo += deposito
        qtde_transacoes += 1
        print('\n=== Depósito realizado com sucesso ===')

        return saldo, extrato, qtde_transacoes


def op_saque(*, saldo, saque, extrato, limite, qtde_transacoes, numero_saques):
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
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'\nSaldo atual: R$ {saldo:.2f}', end='\n=================================================\n')


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    qtde_transacoes = 0
    LIMITE_SAQUES = 3   
    LIMITE_TRANSACOES = 5

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
            break
        else:
            print('\n@@@ Opção inválida! @@@')

        input("\nPressione ENTER para continuar...")

main()
print('\nTenha um bom dia!')
