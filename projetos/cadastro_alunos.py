alunos = []
#*Funções do projeto
def exibeMenu ():
    
    print("-------- MENU --------")
    print("1 - Cadastrar aluno\n2 - Listar aluno\n3 - Exibir estatística\n4 - Buscar aluno\n5 - Excluir aluno\n0 - Sair")
    try:
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    except ValueError:
        print("Digite uma opção válida!")

def cadastrar_aluno():
    try:
        notas = []
        nome = input("Digite o nome: ").strip()
        idade = int(input("Digite a idade: "))
        curso = input("Informe o curso: ").strip()
        for i in range (3):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)
        aluno = {
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "notas" : notas
            }
        alunos.append(aluno)
    except Exception as e:
        print("Error: ", e)

def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i in range(len(alunos)):
            print(f"{i+1}. {alunos[i]['nome']} - {alunos[i]['idade']} anos - Curso: {alunos[i]['curso']} - Média: {sum(alunos[i]['notas']) / len(alunos[i]['notas']):.2f}")

def exibir_estatisticas():
    print("total de alunos: ",len(alunos) )
    media = [sum(a['notas']) / len(a['notas']) for a in alunos]
    media_g = sum(media)/len(alunos)
    melhor_media = max(media)
    menor_media = min(media)
    print(f"Média geral da turma: {media_g:.2f}")
    print(f"Melhor média: {melhor_media:.2f}")
    print(f"Pior média: {menor_media:.2f}")

def buscar_aluno(nome_param):
    for a in alunos:
        if a['nome'] == nome_param:
            print(f"{alunos.index(a)+1}. {a['nome']} - {a['idade']} anos - Curso: {a['curso']} - Notas: {a['notas']}")
            break
    else :
        print("Aluno não encontrado.")

def excluir_aluno(nome_param):
    for a in alunos:
        if a['nome'] == nome_param:
            alunos.pop(alunos.index(a))
            print(f"Aluno {nome_param} removido com sucesso.")
            break
    else :
        print("Aluno não encontrado.")

#*Programa Principal
while True:
    match exibeMenu():
        case 0:
            print("Saindo do sistema... Até logo!")
            break
        case 1:
            cadastrar_aluno()
            continue
        case 2:
            listar_alunos()
            continue
        case 3:
            exibir_estatisticas()
            continue
        case 4:
            nome_procurado = input("Digite o nome do aluno procurado: ")
            buscar_aluno(nome_procurado)
            continue
        case 5:
            aluno_pop = input("Digite o anulo a ser removido: ")
            excluir_aluno(aluno_pop)
            continue
        case _:
            print("Digite uma opção válida!")
            continue

