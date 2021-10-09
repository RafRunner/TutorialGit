primeiro_numero = int(input('Entre com o primeiro número: '))

operacao = int(input('Entre com a operação: '))

segundo_numero = int(input('Entre com o segundo número: '))

resultado = None

if operacao == 1:
    resultado = primeiro_numero + segundo_numero
if operacao == 2:
    resultado = primeiro_numero - segundo_numero
if operacao == 3:
    resultado = primeiro_numero * segundo_numero
if operacao == 4:
    resultado = primeiro_numero / segundo_numero

print('Resultado:', resultado)
