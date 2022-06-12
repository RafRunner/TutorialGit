def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    if b == 0:
        return 1
    
    return a * potencia(a, b - 1)

def resto(a, b):
    return a % b
