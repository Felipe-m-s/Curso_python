
# * Escrever na Tela que estou aprendendo Python
print("Estou aprendendo Python!")

# * Declarar duas varias "nome" e "Idade" e exibir frase de apresentação
nome, idade = "Felipe", 19
print("Meu nome é", nome, "e eu tenho", idade, "anos.")

# * Criar duas variáveis e mostrar as 4 operações básicas
x, y = 10, 2

# Soma
print("Soma:", (x + y))

# Subtração
print("Subtracao:", (x - y))

# Multiplicacao
print("Multiplicacao:", (x * y))

#Divisao
print("Divisao:", (x / y))

# * Ler nome e idade e mostrar
nome = input('Digite o teu nome:')
idade = int(input('Digite a tua idade:'))
print("Olá,", nome, "!")
print("Voce tem", idade, "anos.")

# * Ler números e mostrar soma
x = int(input('Digite o primeiro numero:'))
y = int(input('Digite o segundo numero:'))
print("Soma: ",(x+y))

# * Mostrar o dobro, triplo e a metade de um número digitado
z = float(input('Digite um numero:'))
print("Dobro: ",(z*2))
print("Triplo: ",(z*3))
print("Metade: ",(z/2))

# * Conversor de dinheiro
din = float(input('Quantia de dinheiro guardado em dolar:'))
print("Valor em reias: ", din*5)

# * Armaernar informações do usuario e desejar boas-vindas
nome = input('Digite o teu nome:')
idade = int(input('Digite a tua idade:'))
cidade = input('Digite a tua cidade:')
print("Olá,", nome,"!")
print("Voce tem", idade, "anos e mora em", cidade)
print("Seja bem_vindo ao mundo da programação!")

# * Calcular nota
print("Insira tuas notas:")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))

media = (n1+n2)/2

if media >= 7:
    print("Aprovado!")
elif media >= 5 & media <= 6.9:
    print("Recuperacao!")
else:
    print("Reprovado!")

