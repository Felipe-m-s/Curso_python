class Tarefa:
    def __init__(self, id, descricao, data_criacao):
        self.id = id
        self.descricao = descricao
        self.concluida = False
        self.data_criacao = data_criacao