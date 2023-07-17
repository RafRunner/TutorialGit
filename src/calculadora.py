import operacoes

operacao = input('Entre com a operação: ')

primeiro_numero = int(input('Entre com o primeiro número: '))

segundo_numero = int(input('Entre com o segundo número: '))

resultado = None

if operacao == 'soma':
    resultado = operacoes.soma(primeiro_numero, segundo_numero)
elif operacao == 'subtração':
    resultado = operacoes.subtracao(primeiro_numero, segundo_numero)
elif operacao == 'multiplicação':
    resultado = operacoes.multiplicacao(primeiro_numero, segundo_numero)
elif operacao == 'divisão':
    resultado = operacoes.divisao(primeiro_numero, segundo_numero)
elif operacao == 'potência':
    resultado = operacoes.potencia(primeiro_numero, segundo_numero)
elif operacao == 'resto':
    resultado = operacoes.resto(primeiro_numero, segundo_numero)
else:
    raise Exception(f"Operação '{operacao}' não reconhecida!")

print('Resultado:', resultado)
