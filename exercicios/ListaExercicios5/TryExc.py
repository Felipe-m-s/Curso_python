
#* 7. Divisão segura
print("\n", "-" * 30, "Atvidade 7", "-" * 30)
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    print(num1/num2)
except ValueError:
    print("Letra digitado, ao invés de número")
except ZeroDivisionError:
    print("Não é possivel divisão por zero")

#* 8. Validação de número inteiro
print("\n", "-" * 30, "Atvidade 8", "-" * 30)
while True:
    try:
        num = int(input("Digite um número interiro: "))
        print(f"{num} é o número inteiro que foi digitado")
        break
    except ValueError:
        print("Valor digitado não é inteiro! Tente novamente...")

#* 9. Abertura de arquivo com tratamento de erro
print("\n", "-" * 30, "Atvidade 9", "-" * 30)
def abrirArquivo(nome_arquivo_param):
    try:
        with open(nome_arquivo_param, "r") as arquivo:
            conteudo = arquivo.read()
            print("Arquivo aberto!")
            return conteudo
    except FileNotFoundError:
        print("Arquivo não encontrado")

nome_arquivo = input("Digite o nome do arquivo: ")
abrirArquivo(nome_arquivo)

#* 10. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 10", "-" * 30)
#* 11. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 11", "-" * 30)
#* 12. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 12", "-" * 30)
#* 13. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 13", "-" * 30)
#* 14. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 14", "-" * 30)
#* 15. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 15", "-" * 30)
#* 16. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 16", "-" * 30)
#* 17. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 17", "-" * 30)
#* 18. Quadrado dos números de uma lista
print("\n", "-" * 30, "Atvidade 18", "-" * 30)