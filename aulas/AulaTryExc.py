try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10/numero
    print("Resultado: ", resultado)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except Exception as e:
    print("Ocorreu um erro:", e)

#* Usando Raise
idade = int(input("Digite sua idade: "))
if idade < 0:
    raise ValueError("Idade não pode ser negativa.")
else:
    print("Sua idade é:", idade)

#todo Exercicio de fixação
def dividir(a_param, b_param):
    if b_param == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a_param / b_param

try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    resultado = dividir(a, b)
    print("Resultado:", resultado)
except ValueError as e:
    print("Erro:", e)

#* Implementando Else e Finally
try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    resultado = a/b
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Divisão realizada com sucesso.")
    print("O resultado é:", resultado)
finally: #Sempre será exibibido, apesar de erros ou não
    print("Fim do programa.")
