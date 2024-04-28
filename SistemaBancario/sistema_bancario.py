import class_conta
import depositar
import sacar
import extrato
import menu
import usuario
import contas

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

if __name__ == '__main__':
    conta = class_conta.class_conta()

    while True:
        opcao = input(menu)

        match opcao:
            case 'd':
                print('Depósito: ')
                valor_depositar = 0

                if valor_depositar<0:
                    print('Valor inválido')

                while valor_depositar <= 0:
                    valor_depositar = float(input('Digite o valor a depositar: '))
                conta.saldo += valor_depositar
                print(f'O saldo atual é R$ {conta.saldo:.2f}')
                conta.extrato += f'Deposito: R$ {valor_depositar:.2f}'
            case 's':
                print('Sacar: ')
                valor_sacar = float(input('Digite o valor a sacar: '))

                if valor_sacar>conta.saldo:
                    print('O valor a sacar é maior que o saldo da conta.')
                elif conta.numero_saques>conta.LIMITE_SAQUES:
                    print('O número de saques chegou ao limite.')
                elif valor_sacar>conta.limite:
                    print('O valor digitado está acima do limite permitido de R$ 500,00.')
                else:
                    conta.saldo -= valor_sacar
                print(f'O saldo atual é R$ {conta.saldo:.2f}')
                conta.extrato += f'Saque: R$ {valor_sacar:.2f}'
            case 'e':
                print('\n=======================Extrato=======================')
                print('Não foram realizadas movimentações.' if not {conta.extrato} else {conta.extrato})
                print(f'Saldo: R$ {conta.saldo:.2f}')
            case 'q':
                print('Sair: ')
                break
            case _:
                print('Operação inválida, por favor selecione novamente a operação desejada.')