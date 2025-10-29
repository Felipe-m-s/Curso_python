
#todo Função para somar
def soma(a, b):
    return a + b

#todo Função para subtrair
def subtrair(a, b):
    return a - b

#todo Função para multiplicar
def multiplicar(a, b):
    return a * b

#todo Função para dividir
def dividir(a, b):
    if b == 0:
        return "Error!! Divisão por zero"
    return a / b

#todo Função para calcular media
def media(a, b):
    return soma(a, b)/2

print(f"Soma: {soma(5, 2)}") 
print(f"Subtração: {subtrair(5, 2)}")
print(f"Multiplicação: {multiplicar(5, 2)}")
print(f"Divisão: {dividir(5, 2)}")
print(f"Média: {media(5, 2)}")