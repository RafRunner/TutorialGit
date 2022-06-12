import operacoes

primeiro_numero = int(input('Entre com o primeiro número: '))

operacao = input('Entre com a operação: ')

segundo_numero = int(input('Entre com o segundo número: '))

resultado = None

if operacao == 'soma' or operacao == '+':
    resultado = operacoes.soma(primeiro_numero, segundo_numero)
if operacao == 'subtração' or operacao == '-':
    resultado = operacoes.subtracao(primeiro_numero, segundo_numero)
if operacao == 'multiplicação' or operacao == '*':
    resultado = operacoes.multiplicacao(primeiro_numero, segundo_numero)
if operacao == 'divisão' or operacao == '/':
    resultado = operacoes.divisao(primeiro_numero, segundo_numero)

print('Resultado:', resultado)
