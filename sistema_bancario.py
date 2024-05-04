# 1 - Depósito: Somente valores inteiros positivos.

# 2 - Saque: Somente 3 saques diários, com limite máximo de R$ 500,00 por saque. 
#     se não tiver saldo em conta, exibir uma mensagem informando que não é possivel sacar o dinheiro por falta de saldo.
#     todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# 3 - Extrato: Deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
#     Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo 1500.45 = R$ 1500.45.

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair


  => """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
transacoes = []

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = int(input("Digite o valor que você deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            transacoes.append({'tipo': 'Depósito', 'valor': valor_deposito})
            print(f'Você depositou com sucesso R${valor_deposito:.2f}')
        else:
            print('Valor inválido, você só pode depositar números positivos!')

    elif opcao == 's':
        valor_saque = int(input('Digite o valor que você deseja sacar: '))
        if valor_saque > 0 and valor_saque <= limite:
            if numero_saques < LIMITE_SAQUES:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    numero_saques += 1
                    transacoes.append({'tipo': 'Saque', 'valor': -valor_saque})  # Armazenar saque como valor negativo
                    print(f'Saque realizado com sucesso. Saldo atual: R${saldo:.2f}')
                else:
                    print('Não é possivel sacar o dinheiro por falta de saldo')
            else:
                print('Você atingiu o limite máximo de saques diários permitidos')
        else:
            print('O valor do saque deve ser positivo e não pode exceder R$500.')

    elif opcao == 'e':
        print('Extrato de transações:')
        for transacao in transacoes:
            tipo = transacao['tipo']
            valor = transacao['valor']
            print(f'{tipo}: R${abs(valor):.2f}')
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

