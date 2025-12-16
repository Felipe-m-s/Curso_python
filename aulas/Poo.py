# Classe mae (Veiculo)
class Veiculo:
    def __init__(self, marca, ano, cor):    # Construtor
        self.marca = marca                  # Atributo marca
        self._cor = cor                     # Atributo cor (protegido)
        self.__ano = ano                    # Atributo ano (privado)
        
    @property
    def ano(self):  # Getter para o atributo ano
        return self.__ano
        
    @ano.setter
    def ano(self, novo_ano):    # Setter para o atributo ano
        try:
            if novo_ano >= 1886:
                self.__ano = novo_ano
                print(f"Ano definido para {self.__ano}.")
            else:
                raise ValueError("Ano inválido para um veículo.")
        except ValueError as e:
                print(f"Erro ao alterar o ano: {e}")
        
    def exibir_informacoes(self):   # Método para exibir informações do veículo
        return f"Marca: {self.marca}, Ano: {self.ano}, Cor: {self._cor}"
        
# Classe filha (Carro)
class Carro(Veiculo):
    def __init__(self, marca, ano, cor, portas):
        super().__init__(marca, ano, cor)
        self.portas = portas
        
    def exibir_informacoes(self):
        print(f"Carro - Marca: {self.marca}, Ano: {self.ano}, Cor: {self._cor}, Portas: {self.portas}")

# Classe filha (Moto)
class Moto(Veiculo):
    def __init__(self, marca, ano, cor, tipo):
        super().__init__(marca, ano, cor)
        self.tipo = tipo
        
    def exibir_informacoes(self):
        print(f"Moto - Marca: {self.marca}, Ano: {self.ano}, Cor: {self._cor}, Tipo: {self.tipo}")

#Instanças e uso das classes
veiculo = Veiculo("Generico", 2020, "Vermelho")
carro = Carro("Toyota", 2021, "Azul", 4)
moto = Moto("Honda", 2019, "Preto", "Esportiva")

print(veiculo.exibir_informacoes())
carro.exibir_informacoes()
moto.exibir_informacoes()

# Testando o setter
veiculo.ano = 2022  # Alterando o ano do veículo
carro.ano = 1800   # Tentando definir um ano inválido
moto.ano = 2023   # Alterando o ano da moto

# Exibindo informações atualizadas
print(veiculo.exibir_informacoes())
carro.exibir_informacoes()
moto.exibir_informacoes()