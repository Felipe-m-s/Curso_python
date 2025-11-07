
#* 1. Soma de números pares
print("\n", "-" * 30, "Atvidade 1", "-" * 30)

# Com def
def soma_pares(a_param, b_param):
    return 0 if a_param % 2 != 0 or b_param % 2 != 0 else a_param + b_param

print(soma_pares(2, 4))
print(soma_pares(2, 3))

#Lambda
soma_pares_lambda = lambda a, b: 0 if a % 2 != 0 or b % 2 != 0 else a + b

print(soma_pares_lambda(2,4))
print(soma_pares_lambda(2,3))

#* 2. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 2", "-" * 30)

# Com def
def quadrado_lista(numeros_param) :
    lista_quadrado = []
    for n in numeros_param:
        lista_quadrado.append(n**2)
    return lista_quadrado

numeros = [2, 3, 4]
print(quadrado_lista(numeros))

# Com map e lambda
quadrado_lista_lambda = list(map(lambda n: n**2, numeros))
print(quadrado_lista_lambda)

#* 3. Cálculo da média e situação do aluno
print("\n", "-" * 30, "Atvidade 3", "-" * 30)

# Com def
def media_notas(n1_param, n2_param, n3_param):
    media = (n1_param+n2_param+n3_param)/3
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Em recuperação"
    else:
        return "Reprovado"

print(media_notas(10, 7, 8))

# Com lambda
def media_notas_lambda(n1_param, n2_param, n3_param):
    media = (lambda a, b, c: (a+b+c)/3)(n1_param, n2_param, n3_param)
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Em recuperação"
    else:
        return "Reprovado"

print(media_notas_lambda(10, 7, 8))

#* 4. Filtragem de maiores de idade
print("\n", "-" * 30, "Atvidade 4", "-" * 30)

idades = [17, 18, 19, 15, 13, 20]

# Com def
def maior_idade(idades_param):
    maiores = []
    for i in idades_param:
        maiores.append(i) if i >= 18 else None
    return maiores

print(maior_idade(idades))

# Com filter e lambda
maior_idade_lambda = list(filter(lambda i: i >= 18, idades))
print(maior_idade_lambda)

#* 5. Conversor de temperatura
print("\n", "-" * 30, "Atvidade 5", "-" * 30)

def celsius_to_fahrenheit(temp_param):
    return temp_param * 1.8 + 32

print(f"{celsius_to_fahrenheit(21):.1f}")

celsius_to_fahrenheit_lambda = lambda temp: temp * 1.8 + 32
print(f"{celsius_to_fahrenheit_lambda(21):.1f}")

#* 6. Maior entre três números
print("\n", "-" * 30, "Atvidade 6", "-" * 30)

# Com def
def max_num(num1_param, num2_param, num3_param):
    nums = [num1_param, num2_param, num3_param]
    maior = -999999999999999999
    for i in nums:
        if i > maior:
            maior = i
    return maior

print(max_num(5, -10, 8))

# Com lambda e max
max_num_lambda = lambda a, b, c: max(a, b, c)
print(max_num_lambda(5, -10, 8))
