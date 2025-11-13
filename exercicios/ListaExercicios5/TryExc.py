
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

#* 10. Raiz quadrada segura
print("\n", "-" * 30, "Atvidade 10", "-" * 30)
def calcular_raiz_segura():
    try:
        entrada = input("Digite um número para calcular a raiz quadrada: ")
        numero = float(entrada)
        
        if numero < 0:
            raise ValueError("ERRO: Não é possível calcular a raiz quadrada de um número negativo).")
        
        raiz = numero**0.5
        print(f"\nA raiz quadrada de {numero} é: {raiz}")

    except ValueError as e:
        
        print(f"\nOcorreu um erro de valor: {e}")
        print("Por favor, certifique-se de digitar um número válido e não-negativo.")
    
    except Exception as e:
        print(f"\nUm erro inesperado ocorreu: {e}")

calcular_raiz_segura()

#* 11. Cadastro com validação de idade e nota
print("\n", "-" * 30, "Atvidade 11", "-" * 30)
def cadastrarAluno ():
    nome = input("Digite o nome do aluno: ")
    try:
        idade = input("Idade: ")
        idade = float(idade)
    except ValueError:
        print("Digite uma idade válida!")
        return
        
    
    try:
        nota = input("Nota Final: ")
        nota = float(nota)
        
        if nota < 0 or nota > 10:
            raise ValueError("Digite notas de 0 a 10")
    except ValueError:
        print("Digite uma nota válida")
        return
    
    print(f"Aluno cadastrado com sucesso!\nNome: {nome}\nIdade: {idade}\nNota final: {nota}")

cadastrarAluno()

#* 12. Soma com bloco finally
print("\n", "-" * 30, "Atvidade 12", "-" * 30)
def SomaFinally ():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        print(f"Soma: {num1+num2}")
    except ValueError:
        print("Digite somente números")
    finally:
        print("Operação concluída")

SomaFinally()