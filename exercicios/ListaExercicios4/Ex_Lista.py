
#* 1. Escreva um algoritmo que armazene em um vetor (lista) todos os números inteiros de 1 a  50 e, em seguida, imprima todos os valores armazenados.
print("-" * 30, "Atvidade 1", "-" * 30)
vetor = []
for i in range(1, 51):
    vetor.append(i)

print(vetor)

#* 2. Escreva um algoritmo que armazene em um vetor todos os números inteiros de 100 a 1  (em ordem decrescente) e, em seguida, imprima todos os valores armazenados.
print("\n", "-" * 30, "Atvidade 2", "-" * 30)
vetor = []
for i in range(100, 0, -1):
    vetor.append(i)

print(vetor)

#* 3. Escreva um algoritmo que armazene em um vetor os 100 primeiros números ímpares e,  em seguida, imprima todos os valores armazenados. 
print("\n", "-" * 30, "Atvidade 3", "-" * 30)
vetor = []
i = 1
while True:
    if len(vetor) <= 100:
        if i % 2 != 0:
            vetor.append(i)
        i+=1
    else:
        break

print(vetor)

#* 4. Escreva um algoritmo que leia 10 números e armazene em um vetor a metade de cada  número. Depois, exiba todos os valores armazenados. 
print("\n", "-" * 30, "Atvidade 4", "-" * 30)
vetor = []

for i in range(10):
    valor = int(input(f"Digite {i+1}º numero: "))
    vetor.append(valor/2)

print(vetor)

#* 5. Escreva um algoritmo que leia 10 números e armazene em um vetor o quadrado de cada  número. Depois, exiba todos os valores armazenados. 
print("\n", "-" * 30, "Atvidade 5", "-" * 30)
vetor = []

for i in range(10):
    valor = int(input(f"Digite {i+1}º numero: "))
    vetor.append(valor**2)

print(vetor)

#* 6. Escreva um programa que leia 6 números inteiros representando o gabarito da Mega  Sena e, em seguida, leia 10 apostas com 6 números cada. 
print("\n", "-" * 30, "Atvidade 6", "-" * 30)
gabarito = []
chute = []
acertos = 0

for i in range(6):
    num = int(input(f"Digite o {i+1}º número da Mega: "))
    gabarito.append(num)

for aposta in range(10):
    print(f"Aposta {aposta+1}:")
    
    chute.clear()
    
    for j in range(6):
        numC = int(input(f"Digite o {j+1}º chute: "))
        chute.append(numC)
    
    for k in range(6):
        if gabarito[k] == chute[k]:
            acertos+=1
    
    print(f"Acertaste {acertos} números nessa aposta")

#* 7. O programa deve informar quantos acertos cada apostador obteve e se fez quadra (4  acertos), quina (5 acertos) ou sena (6 acertos). 
print("\n", "-" * 30, "Atvidade 7", "-" * 30)
gabarito = []
chute = []
acertos = 0

for i in range(6):
    num = int(input(f"Digite o {i+1}º número da Mega: "))
    gabarito.append(num)

for aposta in range(10):
    print(f"Aposta {aposta+1}:")
    
    chute.clear()
    
    for j in range(6):
        numC = int(input(f"Digite o {j+1}º chute: "))
        chute.append(numC)
    
    for k in range(6):
        if gabarito[k] == chute[k]:
            acertos+=1
    
    if acertos == 4:
        print(f"Acertaste {acertos} números nessa aposta. Uma quadra")
    elif acertos == 5:
        print(f"Acertaste {acertos} números nessa aposta. Uma quina")
    elif acertos == 6:
        print(f"Acertaste {acertos} números nessa aposta. Uma mega")
    else:
        print(f"Acertaste apenas {acertos} números nessa aposta.")
