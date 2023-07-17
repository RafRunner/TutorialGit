import operacoes

operacao = input('Entre com a operação: ')

primeiro_numero = int(input('Entre com o primeiro número: '))

segundo_numero = int(input('Entre com o segundo número: '))

resultado = None

if operacao == 'soma':
    resultado = operacoes.soma(primeiro_numero, segundo_numero)
if operacao == 'subtração':
    resultado = operacoes.subtracao(primeiro_numero, segundo_numero)
if operacao == 'multiplicação':
    resultado = operacoes.multiplicacao(primeiro_numero, segundo_numero)
if operacao == 'divisão':
    resultado = operacoes.divisao(primeiro_numero, segundo_numero)

print('Resultado:', resultado)
