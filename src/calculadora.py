import operacoes

while True:
    primeiro_numero = int(input('Entre com o primeiro número: '))

    operacao = input('Entre com a operação: ')

    segundo_numero = int(input('Entre com o segundo número: '))

    # Aqui usamos a funcionalidade do python de poder guardar funções em variáveis
    funcao = None

    if operacao == 'soma' or operacao == '+':
        funcao = operacoes.soma
    elif operacao == 'subtração' or operacao == '-':
        funcao = operacoes.subtracao
    elif operacao == 'multiplicação' or operacao == '*':
        funcao = operacoes.multiplicacao
    elif operacao == 'divisão' or operacao == '/':
        funcao = operacoes.divisao
    else:
        break

    print('Resultado:', funcao(primeiro_numero, segundo_numero))