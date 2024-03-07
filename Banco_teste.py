import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
Saldo = 0

for i in range(1, 10001):
    Saldo_atual = 0
    User = input('\n\nOlá, seja bem vindo ao banco XRONALDO, o que o senhor deseja fazer? \
          \n D: para Depositar \n S: para sacar \n E: para extrato \n X: para sair \n ')

    if User == 'S':
        valor_deseja_sacar = float(input(f"Seu saldo atual é de {locale.currency(Saldo, grouping=True)}. Quanto você deseja sacar:  "))
        if valor_deseja_sacar <= 500:
            valor_sacado_formatado = locale.currency(valor_deseja_sacar, grouping=True)
            saldo_após_saque = locale.currency(Saldo - valor_deseja_sacar, grouping=True)
            print(f"## Parabéns, você sacou: {valor_sacado_formatado}\n## Seu saldo agora é de: {saldo_após_saque} ") 
        elif valor_deseja_sacar > 500:     #limite de 500,00 por transação.
            print('Me desculpe, você excedeu o limite por transação.')
        else:
            print('Por favor, insira um valor válido.')

    elif User.upper() == 'D':
        Valor_deposito = float(input(f"Seu saldo atual é de {locale.currency(Saldo, grouping=True)}. Qual valor deseja depositar: "))
        if Valor_deposito <= 500:
            Valor_formatado = locale.currency(Valor_deposito, grouping=True)
            saldo_após_deposito = locale.currency(Saldo + Valor_deposito, grouping=True)
            print(f"## Parabéns, você depositou: {Valor_formatado}\n## Seu saldo agora é de: {saldo_após_deposito} ")
        elif Valor_deposito > 500:
            print('Me desculpe, você excedeu o limite por transação.')
        else:
            print('Por favor, insira um valor válido.')

    elif User.upper() == 'X':
        break



