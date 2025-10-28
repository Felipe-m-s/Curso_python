
#* 11.Crie uma tupla com os números de 1 a 5 e exiba todos os seus elementos na tela.
print("\n", "-" * 30, "Atvidade 11", "-" * 30)
numeros = (1, 2, 3, 4, 5)
print(numeros)

#* 12.Crie uma tupla com os nomes de cinco cidades brasileiras e exiba apenas a primeira e  a última cidade da tupla. 
print("\n", "-" * 30, "Atvidade 12", "-" * 30)
cidades = ("São Paulo", "Belo Horizonte", "Curitiba", "Manaus", "Goiana")
print(f"Primeira cidade: {cidades[0]}")
print(f"Última cidade: {cidades[4]}")

#* 13.Crie uma tupla com dez números inteiros. 
#* ∙ Mostre o menor e o maior número da tupla. 
#* ∙ Mostre também a quantidade de elementos usando len(). 
print("\n", "-" * 30, "Atvidade 13", "-" * 30)
numerosInt = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"O menor numero da tupla: {min(numerosInt)}")
print(f"O maior numero da tupla: {max(numerosInt)}")
print(f"Quantidade de numeros na tupla: {len(numerosInt)}")

#* 14.Crie duas tuplas com números inteiros e gere uma nova tupla resultante da soma (concatenação) das duas. 
print("\n", "-" * 30, "Atvidade 14", "-" * 30) 
tupla1 = (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)
tuplaR = tupla1 + tupla2
print(f"Tupla resultante: {tuplaR}")

#* 15.Crie uma tupla com quatro elementos e repita-a três vezes usando o operador *. 
print("\n", "-" * 30, "Atvidade 15", "-" * 30) 
tupla = (1, 2, 3, 4)
tupla_repetida = tupla * 3
print(f"Tupla repetida: {tupla_repetida}")

#* 16.Crie uma tupla com os elementos (5, 10, 15, 10, 20, 10) e: 
#* ∙ Conte quantas vezes o número 10 aparece (count()). 
#* ∙ Mostre o índice da primeira ocorrência do número 15 (index()). 
print("\n", "-" * 30, "Atvidade 16", "-" * 30) 
tupla16 = (5, 10, 15, 10, 20, 10)
print(f"O número 10 aparece {tupla16.count(10)} vezes")
print(f"A primeira ocorrencia do número 15 foi na posição {tupla16.index(15)}")

#* 17.Crie uma tupla com os valores (10, 20, 30) e use desempacotamento para atribuir cada  valor a uma variável diferente (a, b, c). Depois, exiba as três variáveis separadamente. 
print("\n", "-" * 30, "Atvidade 17", "-" * 30) 
tupla17 = (10, 20, 30)
a, b, c = tupla17
print(f"Valor de a: {a}\nValor de b: {b}\nValor de c: {c}")

#* 18.Crie uma tupla aninhada, representando as notas de três alunos, sendo cada tupla  interna as três notas do aluno. Exemplo: ((7,8,6), (9,5,7), (8,8,10)) 
#* Mostre a primeira nota do segundo aluno e a média do terceiro aluno.
print("\n", "-" * 30, "Atvidade 18", "-" * 30)
tupla18 = ((7,8,6), (9,5,7), (8,8,10))
print(f"A primeira nota do segundo aluno é {tupla18[1][0]} pontos")
print(f"A media do terceiro aluno é {round(sum(tupla18[2])/len(tupla18[2]), 2)}")