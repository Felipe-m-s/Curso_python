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
