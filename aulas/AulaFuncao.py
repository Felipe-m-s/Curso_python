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



#* ----------------- Função com empacotamento (Quando eu não sei quanto paramentos a função vai receber) -----------------
def contador (*num_parm):
    tam = len(num_parm)
    print(f"Foram recebidos os valores {num_parm} e são, ao todo, {tam} números")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def somar (*args):
    print(f"Recebi os valores: ", args)
    print ("A soma é: ", sum(args))

somar(2, 4, 6)
somar(10, 20)
somar(10, 20, 30, 40, 50)


#* ----------------- Função com empacotamento, com agumentos nomeados (Quando eu não sei quanto paramentos a função vai receber) -----------------
def dados (**kwargs):
    print("Dados recebidos")
    for chave, valor in kwargs.items():
        print(f"{chave} : {valor}")

dados(nome = "Ana", idade = 25, cidade = "SJE")
dados(produto = "Notebook", preco = 3500)

#todo Crie uma função chamada "exibeMenu": 0 - sair; 1 - somar.
#todo A função deve ler a opção do usuario e retornar um valor inteiro

def exibeMenu ():
    
    print("-------- MENU --------")
    print("0 - Sair\n1 - Somar")
        
    opcao = int(input("Digite a opção desejada: "))
    return opcao


#todo Função para somar dois numeros
def somarDoisNum(num1_parm, num2_parm):
    return num1_parm + num2_parm

#todo Implementando o programa principal
while True:
    match exibeMenu():
        case 0:
            break
        case 1:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            print(f"A soma de {num1} + {num2} é igual à {somarDoisNum(num1, num2)}")
            continue
        case _:
            print("Opção invalida")
            continue


#* ----------------- Lambda -----------------

#Sem lambda
def dobro (x_parm):
    return x_parm * 2

print(dobro(4))

#Com lambda
dobroV = lambda x: x*2
print(dobro(4))

# ou

print((lambda x: x*2)(4))

#* -----------------Map com Lambda -----------------
#Sem map
numeros = [1, 2, 3]
quadrados = []

for x in numeros:
    quadrados.append(x ** 2)
print(quadrados)

#Com map
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)


#* ----------------- Filter com Lambda -----------------
#Sem filter 
nuns = [1, 8, 3, 10, 5]
pares = []

for num in nuns:
    if num % 2 == 0:
        pares.append(num)
print(pares)

#Com filter
pares = list(filter(lambda x: x % 2 == 0, nuns))
print(pares)


#* ----------------- Reduce com Lambda -----------------
#importando a função reduce  do módulo functools
from functools import reduce

vec_nuns = [1, 2, 3]
palavras = ['Phy','ton', ' ', 'é legal']
soma_total = reduce(lambda x, y: x + y, vec_nuns)
print(soma_total)
concatenacao = reduce (lambda x, y: x + y, palavras)
print(concatenacao)

#* ----------------- List Comprhession -----------------
#Sem list comprhession
quadrados = []
for i in range(1, 6):
    quadrados.append(i ** 2)
print(quadrados)

quadrados_pares = []
for i in range(1, 6):
    quadrados_pares.append(i ** 2) if i%2 == 0 else None

print(quadrados_pares)

#Com list comprhession
quadrados = [i ** 2 for i in range(1, 6)]
print(quadrados)

quadrados_pares = [i ** 2 for i in range(1, 6) if i % 2 == 0]
print(quadrados_pares)

#Extra
quadrados_pares_maior_que_3 = [i for i in range(1, 6) if i % 2 == 0 and i > 3]
print(quadrados_pares_maior_que_3)

num = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = [i for i in num if i < 3 or i > 10]
print(resultado)

