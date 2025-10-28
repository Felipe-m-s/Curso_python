
#* 1. Faça um programa que leia uma matriz 2×2 de números inteiros e exiba todos os  valores na tela. 
print("\n", "-" * 30, "Atvidade 1", "-" * 30)
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

for i in range(2):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()

#* 2. Faça um programa que leia uma matriz 3×3 de números inteiros e imprima o conteúdo  organizado em forma de tabela. 
print("\n", "-" * 30, "Atvidade 2", "-" * 30)
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" | ")
    print()


#* 3. Escreva um algoritmo que leia uma matriz 3×3 e exiba a soma dos elementos de cada  linha. 
print("\n", "-" * 30, "Atvidade 3", "-" * 30)
matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        soma += matriz[i][j]
    print(f"Soma linha {i+1}: {soma}")
    soma = 0

#* 4. Escreva um algoritmo que leia uma matriz 3×3 e exiba a soma dos elementos de cada  coluna. 
print("\n", "-" * 30, "Atvidade 4", "-" * 30)
matriz = []
soma = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

for j in range(3):
    for i in range(3):
        soma += matriz[i][j]
    print(f"Soma linha {i+1}: {soma}")
    soma = 0

#* 5. Faça um programa que calcule a soma das diagonais principal e secundária de uma  matriz 3×3.
print("\n", "-" * 30, "Atvidade 5", "-" * 30)
matriz = []
somaDP = 0
somaDS = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if i == j:
            somaDP += matriz[i][j]
        if i + j == 2:
            somaDS += matriz[i][j]

print(f"Soma da diagonal principal: {somaDP}")
print(f"Soma da diagonal secundaria: {somaDS}")

#* 6. Faça um programa que verifique se uma matriz 3×3 forma um quadrado mágico (ou  seja, se as somas das linhas, colunas e diagonais são iguais). 
print("\n", "-" * 30, "Atvidade 6", "-" * 30)
matriz, somaLinhas, somaColunas = [], [], []
somaDP, somaDS = 0, 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o numero da posição [{i}][{j}]"))
        linha.append(valor)
    matriz.append(linha)

# Somando diagonais
for i in range(3):
    for j in range(3):
        if i == j:
            somaDP += matriz[i][j]
        if i + j == 2:
            somaDS += matriz[i][j]

# Somando as linhas e armazendo em um outro vetor
for linha in matriz:
    somaLinhas.append(sum(linha))

# Somando as colunas e armazendo em um outro vetor
for j in range(3):
    somaColunas.append(sum(matriz[i][j] for i in range(3)))

# Verificando se é quadro mágico
referencia = somaDP
print("A matriz informada forma um quadro mágico" if (all(soma == referencia for soma in somaColunas)
                                                    and all(soma == referencia for soma in somaLinhas)
                                                    and referencia == somaDP and referencia == somaDS)
                                                else "A matriz informada não forma um quadro mágico")

#* 7. Escreva um programa que leia uma matriz 2×3 de Strings (nomes ou letras) e exiba seu  conteúdo. 
print("\n", "-" * 30, "Atvidade 7", "-" * 30)
matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        a = input("Digite nomes ou letras: ")
        linha.append(a)
    matriz.append(linha)

for i in range(2):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()

#* 8. Crie um programa que leia uma matriz 2×2 de números reais e exiba seus valores.
print("\n", "-" * 30, "Atvidade 8", "-" * 30)
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        a = float(input("Digite numeros reais: "))
        linha.append(a)
    matriz.append(linha)

for i in range(2):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()

#* 9. Realize a soma das duas matrizes 2×2 e exiba o resultado. 
print("\n", "-" * 30, "Atvidade 9", "-" * 30)
print("Lendo matriz 1...\n")
matriz1 = []
for i in range(2):
    linhaM1 = []
    for j in range(2):
        a = float(input("Valor: "))
        linhaM1.append(a)
    matriz1.append(linhaM1)

print("Lendo matriz 2...\n")
matriz2 = []
for i in range(2):
    linhaM2 = []
    for j in range(2):
        b = float(input("Valor: "))
        linhaM2.append(b)
    matriz2.append(linhaM2)

print("Resultado da soma das matrizes\n")
matrizR = []
for i in range(2):
    linhaR = []
    for j in range(2):
        c = matriz1[i][j] + matriz2[i][j]
        linhaR.append(c)
    matrizR.append(linhaR)

for i in range(2):
    for j in range(2):
        print(matrizR[i][j], end=" ")
    print()

#* 10.Realize a multiplicação das duas matrizes 2×2 e exiba o resultado 
print("\n", "-" * 30, "Atvidade 10", "-" * 30)
print("Lendo matriz 1...\n")
matriz1 = []
for i in range(2):
    linhaM1 = []
    for j in range(2):
        a = float(input("Valor: "))
        linhaM1.append(a)
    matriz1.append(linhaM1)

print("Lendo matriz 2...\n")
matriz2 = []
for i in range(2):
    linhaM2 = []
    for j in range(2):
        b = float(input("Valor: "))
        linhaM2.append(b)
    matriz2.append(linhaM2)

print("Resultado da multiplicação entre as matrizes\n")
matrizR = []
for i in range(2):
    linhaR = []
    for j in range(2):
        c = (matriz1[i][0]*matriz2[0][j]) + (matriz1[i][1]*matriz2[1][j])
        linhaR.append(c)
    matrizR.append(linhaR)

for i in range(2):
    for j in range(2):
        print(matrizR[i][j], end=" ")
    print()
