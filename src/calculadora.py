import operacoes

primeiro_numero = int(input('Entre com o primeiro número: '))

operacao = input('Entre com a operação: ')

segundo_numero = int(input('Entre com o segundo número: '))

# Aqui usamos a funcionalidade do python de poder guardar funções em variáveis
funcao = None

if operacao == 'soma' or operacao == '+':
    funcao = operacoes.soma
if operacao == 'subtração' or operacao == '-':
    funcao = operacoes.subtracao
if operacao == 'multiplicação' or operacao == '*':
    funcao = operacoes.multiplicacao
if operacao == 'divisão' or operacao == '/':
    funcao = operacoes.divisao

print('Resultado:', funcao(primeiro_numero, segundo_numero))