
# # #todo Questão 1
# for i in range(51):
#     print(i, " ")

# #todo Questão 2
# for i in range(100, 0, -1):
#     print(i, " ")

# #todo Questão 3
# for i in range(100, 201):
#     print(i, " ")

# #todo Questão 4
# for i in range(200, 99, -1):
#     print(i, " ")

# #todo Questão 5
# for i in range(0, 501):
#     if i % 5 != 0:
#         continue
#     print(i, " ")

# #todo Questão 6
# for i in range(1, 101):
#     if i % 2 == 0:
#         continue
#     print(i, " ")

# #todo Questão 7
# for i in range(10):
#     num = float(input(f"Digite o {i+1}º número: "))
#     print("A metade é:", num / 2)
# print()

# #todo Questão 8
# for i in range(10):
#     num = float(input(f"Digite o {i+1}º número: "))
#     print("O quadrado é:", num ** 2)
# print()

# #todo Questão 9
# NUM = int(input("Quantos números deseja digitar? "))
# maior = 0
# for i in range(NUM):
#     n = int(input(f"Digite o {i+1}º número: "))
#     if n > maior:
#         maior = n
# print("O maior número é:", maior)
# print()

# #todo Questão 10
# soma_positivos = 0
# total_negativos = 0
# for i in range(20):
#     n = int(input(f"Digite o {i+1}º número: "))
#     if n > 0:
#         soma_positivos += n
#     elif n < 0:
#         total_negativos += 1
# print("Soma dos positivos:", soma_positivos)
# print("Total de negativos:", total_negativos)
# print()

# #todo Questão 11

# A = int(input("Digite o valor de A (base): "))
# B = int(input("Digite o valor de B (expoente): "))
# resultado = 1
# for i in range(B):
#     resultado *= A
# print(f"{A} elevado a {B} é {resultado}")
# print()

# #todo Questão 12
# N = int(input("Digite o valor de N: "))
# print("Números ímpares de 1 até N:")
# for i in range(1, N+1):
#     if i % 2 != 0:
#         print(i, end=" ")
# print("\n")

# #todo Questão 13
# N = int(input("Digite um número: "))
# print(f"Divisores de {N}:")
# for i in range(1, N+1):
#     if N % i == 0:
#         print(i, end=" ")
# print("\n")

# #todo Questão 14
# soma = 0
# num1 = int(input("Digite o 1º número: "))
# num2 = int(input("Digite o 2º número: "))

# for i in range(num1, (num2+1)):
#     soma += i
# print("Soma dos números:", soma)
# print()

# #todo Questão 15
# num = int(input("Digite um número: "))
# eh_primo = True
# if num <= 1:
#     eh_primo = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             eh_primo = False
#             break
# if eh_primo:
#     print(f"{num} é primo")
# else:
#     print(f"{num} não é primo")
# print()

# #todo Questão 16
# num = int(input("Digite um número: "))
# fatorial = 1
# for i in range(1, num + 1):
#     fatorial *= i
# print(f"O fatorial de {num} é {fatorial}")
# print()

# #todo Questão 17
# contador = 0
# for i in range(10):
#     num = int(input(f"Digite o {i+1}º número: "))
#     if num % 5 == 0 and num % 2 == 0:
#         contador += 1
# print(f"Quantidade de números pares múltiplos de 5: {contador}")

#todo Questão 18

#todo Questão 19
#todo Questão 20
#todo Questão 21
#todo Questão 22
#todo Questão 23










