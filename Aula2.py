# nome_usuario = input("Qual é o teu nome? ")
# print(f"Olá, {nome_usuario}!\nSeja bem-vindo(a)\n")

# idade_usuario = input("Quantos anos você tem? ")
# print(f"Você tem {idade_usuario} anos.")

idade_str = input("Digite sua idade: ")
idade_int = int(idade_str)
print(f"Você tem {idade_int} anos. Daqui um ano, você terá {idade_int + 1} anos.")
print(f"Tipo da idade_str: {type(idade_str)}")
print(f"Tipo da idade_int: {type(idade_int)}")

#* Recebendo um valor com casas decimais e convertendo para float
altura_str = input("Digite a tua altura em metros (ex: 1.75): ")
altura_float = float(altura_str)
print(f"Sua altura é {altura_float} metros")
print(f"Tipo da altura_str: {type(altura_str)}")
print(f"Tipo da altura_float: {type(altura_float)}")

#* Convertendo um número para string
numero = 100
numero_str = str(numero)
print(f"O número {numero} como string é {numero_str}")

#* Convertendo para booleando
valor_vazio = ""
valor_cheio = "Olá"
numero_zero = 0
numero_cinco = 5
print(f"")