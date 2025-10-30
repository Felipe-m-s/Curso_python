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
