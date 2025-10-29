def soma(a, b):
    soma = a + b
    print(soma)

soma(4, 5)
soma(8, 9)
soma(2, 1)

def mensagem():
    print("Minha segunda função")

mensagem()

def saudacao(nome, idade):
    print(f"Olá, {nome}!\nVocê tem {idade} anos!")

saudacao("Felipe", 19)

def soma_com_return (a, b):
    return a + b

x = soma_com_return(5, 7)
print("Resultado:", x)

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))

def quadrado(n_parm):
    if n_parm == 1:
        return 1
    else:
        return pow(n_parm, 2)

print(f"O quadrado de 1 é {quadrado(5)}")
for i in range(1, 6):
    resultado = quadrado(i)
    print(f"O quadrado de {i} é {quadrado(i)}")
    