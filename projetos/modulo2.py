import mysql.connector

def exibeMenu ():
    
    print("-------- MENU --------")
    print("1 - Cadastrar aluno\n2 - Listar aluno\n3 - Buscar aluno (ID)\n4 - Atualizar Telefone\n5 - Excluir Aluno\n0 - Sair")
    try:
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    except ValueError:
        print("Digite uma opção válida!")
    
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sistema_academico"
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")
    
    cnn = conexao.cursor()
    
        
    while True:
        match exibeMenu():
            case 1:
                print("Cadastrando aluno...\n")
                nome = input("Digite o nome: ").strip()
                email = input("Informe o email: ").strip().lower()
                telefone = input("Informe o telefone: ").strip()
                sql = ("INSERT INTO ALUNO (NOME, EMAIL, TELEFONE) VALUES (%s, %s, %s)")
                dados = (nome, email, telefone)
                cnn.execute(sql, dados)
                conexao.commit()
                print("Aluno cadastrado com sucesso!\n")
                continue
            case 2:
                print("Lista de Alunos:\n")
                cnn.execute("SELECT * FROM ALUNO")
                alunos = cnn.fetchall()
                
                for aluno in alunos:
                    print(f"ID: {aluno[0]} - Nome: {aluno[1]} - Email: {aluno[2]} - Telefone: {aluno[3]}")
                continue
            case 3:
                id_busca = int(input("Digite o ID do aluno que deseja buscar: "))
                slq = "SELECT * FROM ALUNO WHERE ALUNO_ID = %s"
                cnn.execute(slq, (id_busca,))
                aluno = cnn.fetchone()
                if aluno:
                    print(f"ID: {aluno[0]} - Nome: {aluno[1]} - Email: {aluno[2]} - Telefone: {aluno[3]}")
                else:
                    print("Aluno não encontrado.")
                continue
            case 4:
                id_atualizacao = input("Digite o ID do aluno que deseja atualizar o telefone: ")
                novo_telefone = input("Digite o novo telefone: ").strip()
                sql = "UPDATE ALUNO SET TELEFONE = %s WHERE ALUNO_ID = %s"
                dados = (novo_telefone, id_atualizacao)
                cnn.execute(sql, dados)
                conexao.commit()
                print("Telefone atualizado com sucesso.")
                continue
            case 5:
                id_exclusao = int(input("Digite o ID do aluno a ser excluído: "))
                sql = "DELETE FROM ALUNO WHERE ALUNO_ID = %s"
                cnn.execute(sql, (id_exclusao,))
                conexao.commit()
                print("Aluno excluído com sucesso.")
                continue
            case 0:
                print("Saindo do sistema...")
                cnn.close()
                conexao.close()
                break
            case _:
                print("Opção inválida ou não implementada.")
                continue

except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")

