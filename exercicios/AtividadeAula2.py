# Atividade aula 1

#* Atividade 1
contador = 0
contador += 1
print(f"O valor da variável contador após de incrementar 1 é {contador}.")
contador -= 1
print(f"O valor da variável contador após decrementar 1 é {contador}.")

#* Atividade 2
preco_unitario = 2.50
quantidade = 4
total = preco_unitario * quantidade
print(f"O valor total é {total}.")

#* Atividade 3
a = 10
b = 20
a,b = 20,10
print(f"Os novos valores de A e B, respectivamente, são: {a, b}.")

#* Atividade 4
numero_str = input("Digite um numero: ")
numero_int = int(numero_str)
print(numero_int*2)

#* Atividade 5
numero_float = 15.75
numero_str5 = str(numero_float)
print(f"{numero_str5} é um número.")

#* Atividade 6
nome = input("Digite o teu nome completo: ")
idade = input("Qual é a tua idade: ")
altura = float(input("Digite a tua altura em metros (ex: 1.75): "))
print(f"{nome} tem {idade} anos e {altura:.2f} metros de altura.")