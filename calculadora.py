operacao = input('Entre com a operação: ')

primeiro_numero = int(input('Entre com o primeiro número: '))

segundo_numero = int(input('Entre com o segundo número: '))

resultado = None

if operacao == 'soma':
    resultado = primeiro_numero + segundo_numero
if operacao == 'subtração':
    resultado = primeiro_numero - segundo_numero
if operacao == 'multiplicação':
    resultado = primeiro_numero * segundo_numero
if operacao == 'divisão':
    resultado = primeiro_numero / segundo_numero

print('Resultado:', resultado)
