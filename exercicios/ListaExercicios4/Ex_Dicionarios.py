
#* 1. Crie um dicionário com as chaves nome, idade e cidade, e preencha com seus próprios  dados. 
#* Depois, exiba apenas o valor associado à chave nome. 
print("\n", "-" * 30, "Atvidade 1", "-" * 30)
dicionario = {
    "nome" : "Felipe",
    "idade" : "19",
    "cidade" : "SJE"
}
print(dicionario["nome"])

#* 2. Crie um dicionário com três alunos, onde a chave é o nome e o valor é a nota. Exemplo: 
#* alunos = {'Ana':8.5, 'Bruno':7.0, 'Carlos':9.2} 
#* Exiba apenas os nomes dos alunos (keys()) e depois apenas as notas (values()). 
print("\n", "-" * 30, "Atvidade 2", "-" * 30)
alunos = {
    "Ana":8.5,
    "Bruno":7.0,
    "Carlos":9.2
}
print(f"Alunos: {alunos.keys()}")
print(f"Notas: {alunos.values()}")

#* 3. Crie um dicionário e adicione duas novas chaves manualmente. 
#* Em seguida, altere o valor de uma das chaves e exiba o dicionário atualizado. 
print("\n", "-" * 30, "Atvidade 3", "-" * 30)
clientes = {
    "nome" : "Cláudia",
    "status" : "não ativo"    
}
clientes["status"] = "Ativo"
print(clientes)

#* 4. Crie um dicionário representando um produto com as chaves: 
#* nome, preço, estoque. 
#* ∙ Exiba o nome e o preço formatado (R$). 
#* ∙ Aumente o estoque em +5 unidades e mostre o dicionário atualizado.
print("\n", "-" * 30, "Atvidade 4", "-" * 30)
produto = {
    "nome" : "Perfume",
    "preço" : 219.90,
    "estoque" : 3
}
print(f"Informações do produto:\nNome: {produto['nome']}\nPreço: R${produto['preço']:.2f}")

produto["estoque"] += 5
print(f"Informações atualizadas: {produto}")

#* 5. Crie um dicionário aninhado que armazene dois alunos, cada um com suas notas. Exemplo: 
#* alunos = { 
#*  "João": {"nota1": 8, "nota2": 7}, 
#*  "Maria": {"nota1": 9, "nota2": 10} 
#* } 
#* Exiba a nota2 de Maria. 
print("\n", "-" * 30, "Atvidade 5", "-" * 30)
alunos = { 
    "João": {"nota1": 8, "nota2": 7}, 
    "Maria": {"nota1": 9, "nota2": 10} 
}
print(alunos["Maria"]["nota2"])

#* 6. Crie uma lista de tuplas com pares de chave-valor, por exemplo: 
#* [("nome","Carlos"), ("idade",25), ("cidade","Contagem")] 
#* Converta essa lista em um dicionário usando dict() e exiba o resultado. 
print("\n", "-" * 30, "Atvidade 6", "-" * 30)
listaTupla = [("nome","Carlos"), ("idade",25), ("cidade","Contagem")]
d = dict(listaTupla)
print(d)

#* 7. Crie um dicionário que guarde os nomes de 3 alunos e seus conjuntos de disciplinas. Exemplo: 
#* alunos = { 
#*  "Ana": {"Matemática", "Física"}, 
#* "Bruno": {"Geografia", "História"}, 
#* "Carla": {"Matemática", "História"} 
#* } 
#* Mostre todas as disciplinas cursadas por Ana e Carla (união dos conjuntos). 
print("\n", "-" * 30, "Atvidade 7", "-" * 30)
alunos = { 
    "Ana": {"Matemática", "Física"}, 
    "Bruno": {"Geografia", "História"}, 
    "Carla": {"Matemática", "História"} 
}
print("Disciplinas cursadas por Ana e Carla são:")
print(alunos["Ana"].union(alunos["Carla"])) 

#* 8. Crie uma tupla com números de 1 a 10, converta-a para lista, adicione o número 11, e  depois converta novamente para tupla. 
#* Exiba o resultado final. 
print("\n", "-" * 30, "Atvidade 8", "-" * 30)
tupla8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lista8 = list(tupla8)
lista8.append(11)
tupla8 = tuple(lista8)
print(tupla8)

#* 9. Crie uma lista de nomes com repetições e converta-a em um conjunto para eliminar  duplicatas. 
#* Exiba a lista original e o conjunto resultante. 
print("\n", "-" * 30, "Atvidade 9", "-" * 30)
lista9 = ["Felipe", "Talita", "Felipe", "Romualdo", "Lara"]
conj9 = set(lista9)

print(lista9)
print(conj9)

#* 10. Crie um dicionário onde as chaves são os números de 1 a 5 e os valores são seus  quadrados. 
#* Exemplo: {1:1, 2:4, 3:9, ...} 
#* Exiba o dicionário completo. 
print("\n", "-" * 30, "Atvidade 10", "-" * 30)
dict10 = dict()
for i in range(1, 6):
    dict10[i] = pow(i, 2)

print(dict10)