
#* 1. Crie um conjunto com os elementos 'maçã', 'banana', 'uva', 'maçã' e exiba o conjunto. (Observe o que acontece com o elemento repetido.)
print("\n", "-" * 30, "Atvidade 1", "-" * 30)
frutas = {'maçã', 'banana', 'uva', 'maçã'}
print(frutas) #! Elementos repetidos não são inseridos

#* 2. Crie dois conjuntos: 
#* a = {1, 2, 3, 4, 5} e b = {4, 5, 6, 7, 8} 
#* Mostre: 
#* ∙ A união dos dois conjuntos. 
#* ∙ A interseção dos dois conjuntos. 
#* ∙ A diferença entre a e b. 
print("\n", "-" * 30, "Atvidade 2", "-" * 30)
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"União: {a.union(b)}")
print(f"Interseção: {a.intersection(b)}")
print(f"Diferença entre a e b: {a.difference(b)}")

#* 3. Crie um conjunto com os números pares de 0 a 10 e verifique se o número 6 pertence a ele. 
print("\n", "-" * 30, "Atvidade 3", "-" * 30)
num_par = {0, 2, 4, 6, 8, 10}
print("O número 6 pertence ao conjunto!" if 6 in num_par else "O número 6 não pertence ao conjunto!")

#* 4. Crie um conjunto vazio e adicione três nomes de alunos usando o comando add(). Em seguida, remova um nome com remove() e exiba o conjunto atualizado. 
print("\n", "-" * 30, "Atvidade 4", "-" * 30)
alunos = set()
alunos.add("Felipe")
alunos.add("Clésio")
alunos.add("Carlos")

alunos.remove("Carlos")

print(alunos)

#* 5. Crie um conjunto com letras do alfabeto ({'a','b','c','d'}) e use um laço for para imprimir  cada elemento do conjunto. 
print("\n", "-" * 30, "Atvidade 5", "-" * 30)
letras = {'a','b','c','d'}

for letra in letras:
    print(letra)

#* 6. Crie um conjunto com os números {1,2,3} e outro {3,4,5}. 
#* Exiba: 
#* ∙ A união (|) 
#* ∙ A interseção (&) 
#* ∙ A diferença simétrica (^) 
print("\n", "-" * 30, "Atvidade 6", "-" * 30)
x = {1,2,3}
y = {3,4,5}

print(f"União: {x | y}")
print(f"Interseção: {x & y}")
print(f"Diferença: {x ^ y}")