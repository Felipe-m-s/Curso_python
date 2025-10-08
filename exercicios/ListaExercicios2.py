
#todo Questão 1
# numero = int(input("Digite um numero: "))
# if numero > 20:
#     print(f"O numero digitado é {numero}")

#todo Questão 2
# numero1 = int(input("Digite o primeiro numero: "))
# numero2 = int(input("Digite o segundo numero: "))
# if (numero1 + numero2) > 10:
#     print (numero1 + numero2)

#todo Questão 3
# numero = int(input("Digite um numero: "))
# if numero%2 == 0:
#     print("O numero informado e par")
# else:
#     print("O numro informado e impar")

#todo Questão 4
# numero = int(input("Digite um numero: "))
# if numero > 0:
#     print("POSITIVO")
# elif numero < 0:
#     print("NEGATIVO")
# else:
#     print("NULO")

#todo Questão 5
# import math
# numero = int(input("Digite um numero: "))
# if numero >= 0:
#     print(math.sqrt(numero))
# else:
#     print(math.pow(numero,2))

#todo Questão 6
# numero = int(input("Digite um numero: "))
# if numero%3 == 0:
#     print("E multiplo de 3")
# else:
#     print("Nao e multiplo de 3")

#todo Questão 7
# numero = int(input("Digite um numero: "))
# if numero % 5 == 0:
#     print("E divisivel por 5")
# else:
#     print("Nao e divisivel por 5")

#todo Questão 8
# numero1 = int(input("Digite um numero: "))
# numero2 = int(input("Digite outro numero: "))
# if numero1 % numero2 == 0:
#     print(f"{numero1} e divisivel por {numero2}")
# else:
#     print(f"{numero1} nao e divisivel por {numero2}")

#todo Questão 9
# numero1 = int(input("Digite um numero: "))
# numero2 = int(input("Digite outro numero: "))
# if numero1 < numero2:
#     print(f"Maior: {numero2}\nMenor: {numero1}")
# else:
#     print(f"Maior: {numero1}\nMenor: {numero2}")

#todo Questão 10
# salario = float(input("Digite o salario bruto: "))
# prestacao = float(input("Digite o valor da prestacao: "))
# if(prestacao > (salario*0.3)):
#     print("Emprestimo nao pode ser concedido!")
# else:
#     print("Emprestimo pode ser concedido!")

#todo Questão 11
# A = int(input("Digite o primeiro numero: "))
# B = int(input("Digite o segundo numero: "))
# C = int(input("Digite o terceiro numero: "))

# if A <= B and A <= C:  # A é o menor
#     if B <= C:
#         print(f"Ordem ascendente: {A}, {B}, {C}")
#     else:
#         print(f"Ordem ascendente: {A}, {C}, {B}")
# elif B <= A and B <= C:  # B é o menor
#     if A <= C:
#         print(f"Ordem ascendente: {B}, {A}, {C}")
#     else:
#         print(f"Ordem ascendente: {B}, {C}, {A}")
# else:  # C é o menor
#     if A <= B:
#         print(f"Ordem ascendente: {C}, {A}, {B}")
#     else:
#         print(f"Ordem ascendente: {C}, {B}, {A}")

#todo Questão 12
# A = int(input("Digite o primeiro numero: "))
# B = int(input("Digite o segundo numero: "))
# C = int(input("Digite o terceiro numero: "))
# if A >= B and A >= C:
#     # A é o maior
#     if B >= C:
#         print(A, B, C)
#     else:
#         print(A, C, B)
# elif B >= A and B >= C:
#     # B é o maior
#     if A >= C:
#         print(B, A, C)
#     else:
#         print(B, C, A)
# else:
#     # C é o maior
#     if A >= B:
#         print(C, A, B)
#     else:
#         print(C, B, A)

#todo Questão 13
# peso = float(input("Digite o peso em KG: "))
# altura = float(input("Digite a altura em metros: "))
# imc = peso/(altura**2)
# if imc < 20:
#     print("Abaixo do peso")
# elif imc >= 20 and imc <25:
#     print("Peso normal")
# elif imc >= 25 and imc <30:
#     print("Sobre peso")
# elif imc >= 30 and imc <40:
#     print("Obeso")
# else:
#     print("Obeso Morbido")

#todo Questão 14
# idade = int(input("Digite a idade: "))
# if idade < 18:
#     print("Menor de idade")
# elif idade >=18 and idade < 65:
#     print("Maior de idade")
# else:
#     print("Idoso")

#todo Questão 15
# idade = int(input("Digite a idade: "))
# if idade < 16:
#     print("Nao eleitor")
# elif idade >=18 and idade < 65:
#     print("Eleitor obrigatorio")
# else:
#     print("Eleitor facultativo")

#todo Questão 16
# idade = int(input("Digite a idade: "))
# if idade < 10:
#     print("R$30,00")
# elif idade >= 10 and idade < 29:
#     print("R$60,00")
# elif idade >= 29 and idade < 45:
#     print("R$120,00")
# elif idade >= 45 and idade < 59:
#     print("R$150,00")
# elif idade >= 59 and idade < 65:
#     print("R$250,00")
# else:
#     print("R$400,00")

#todo Questão 17
mes = int(input("Digite o numero do mes (1 - 12): "))
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Marco")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Nao existe mes com esse numero")