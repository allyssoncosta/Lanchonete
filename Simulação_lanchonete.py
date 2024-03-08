import time
import random

def print_com_atraso(palavra, atraso=0.07):
    """
    Imprime uma string com atraso entre cada caractere.

    Parameters:
    palavra (str): A string a ser impressa.
    atraso (float): O atraso entre os caracteres.

    Returns:
    None
    """
    for letra in palavra:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()

# Lista de números de 1 a 100
numeros = list(range(1, 101))
numero_pedido = random.choice(numeros)

# Mensagem de boas-vindas
print('>>>  Olá, seja bem-vindo à Hamburgueria X. O que você gostaria de comer hoje?\n\n')

# Cardápio
cardapio = [['Hamburguer Simples', ['pão brioche', 'queijo', 'mussarela', 'hamburguer artesanal\n']],
            ['Hamburguer Supremo', ['pão brioche', 'queijo', 'mussarela', 'cheddar', '3UN de hamburgueres', 'bacon\n']],
            ['Combo Casal', ['2 Hamburguer supremo', 'coca-cola de lata', '2 barras de chocolate D.negro\n\n']]
            ]

# Apresentação do cardápio
for item in cardapio:
    print(f'{item[0]}: {", ".join(item[1])}')

# Obtenção das escolhas do cliente
escolha_do_cliente = input('Escolha o que deseja comer: ')
nome_cliente = input('Digite seu nome: ')
tel = int(input('Telefone: '))
endereco = input('Endereço: ')
forma_de_pagamento = input('Sua forma de pagamento será:\n "CC" para cartão de crédito automático\n "D" para dinheiro\n')

# Processamento do pagamento
if forma_de_pagamento.upper() == 'CC':
    numero_cartao = input('Nº do cartão: ')
    data_validade = input('Data: ')
    cvv = input('CVV: ')
    if len(numero_cartao) == 16:
        print('Cartão autorizado')
    else:
        print('Digite um número de cartão válido!')

# Mensagem de confirmação do pedido
print('Seu pedido está sendo gerado, aguarde')
print_com_atraso(' *')
print_com_atraso('   *')
print_com_atraso('     *')
print_com_atraso('       *')
print_com_atraso('        *')
print('Seu pedido já foi gerado')
print(f'Parabéns {nome_cliente}!! Seu pedido já foi gerado, é o pedido de número {numero_pedido}\n{endereco}\nLanche: {escolha_do_cliente}')
