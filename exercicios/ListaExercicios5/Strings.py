
#* 13. Formatação de nome completo
print("\n", "-" * 30, "Atvidade 13", "-" * 30)
nomeSobrenome = input("Digite o nome e o sobrenome: ")

#Tudo maiúsculo
print(nomeSobrenome.upper())

#Tudo minúsculo
print(nomeSobrenome.lower())

#Cada nome iniciando maiúsculo
print(nomeSobrenome.title())

#* 14. Contagem de letras e palavras
print("\n", "-" * 30, "Atvidade 14", "-" * 30)
frase = input("Digite uma frase: ")
print(f"Há {frase.count('a')} letras 'a' na frase e há {len(frase.split())} palavras")

#* 15. Inversão de texto
print("\n", "-" * 30, "Atvidade 15", "-" * 30)
texto = input("Digite uma palavra ou frase: ")
print(f"O que foi digitado: {texto}")
print(f"Texto inverdito {texto[::-1]}")

#* 16. Comparação de palavras
print("\n", "-" * 30, "Atvidade 16", "-" * 30)
palavra1 = input("Digite uma palavra: ").lower()
palavra2 = input("Digite outra palavra: ").lower()

if palavra1 == palavra2:
    print("As palavras digitadas são iguais!")
elif sorted(palavra1) == sorted(palavra2):
    print("As palavras digitadas são anagramas!")
else:
    print("As palavras digitadas são completamente diferentes!")

#* 17. Substituição de palavras
print("\n", "-" * 30, "Atvidade 17", "-" * 30)
oracao = input("Digite uma frase sobre python: ")
oracaoR = oracao.replace("Python", "Linguagem Python")

print(f"Texto Original: {oracao}")
print(f"Texto Modificado: {oracaoR}")

#* 18. Separação de palavras em linhas
print("\n", "-" * 30, "Atvidade 18", "-" * 30)
textoInteriro = input("Digite uma frase: ")
palavras = textoInteriro.split()

for palavras in palavras:
    print(palavras)
