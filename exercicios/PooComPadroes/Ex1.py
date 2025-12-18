from abc import ABC, abstractmethod

#! Padrão Criacional - Factory Method

class Notificacao(ABC):     # Classe abstrata para notificações
    @abstractmethod
    def enviar(self, mensagem):     # Método abstrato para enviar notificações
        pass

class EmailNotificacao(Notificacao):   # Classe concreta para notificações por email
    def enviar(self, mensagem):
        return f"Enviando email com a mensagem: {mensagem}"

class SMSNotificacao(Notificacao):     # Classe concreta para notificações por SMS
    def enviar(self, mensagem):
        return f"Enviando SMS com a mensagem: {mensagem}"

class PushNotificacao(Notificacao):    # Classe concreta para notificações push
    def enviar(self, mensagem):
        return f"Enviando notificação push com a mensagem: {mensagem}"

#! Fábrica de Notificações
class NotificacaoFactory:
    @staticmethod
    def criarNotificacao (tipo):
        if tipo.strip().lower() == "email":
            return EmailNotificacao()
        elif tipo.strip().lower() == "sms":
            return SMSNotificacao()
        elif tipo.strip().lower() == "push":
            return PushNotificacao()
        else:
            raise ValueError("Tipo de notificação invalida.")

#! Decorator
class NotificacaoDecorator(Notificacao):
    def __init__(self, notificacao):
        self.notificacao = notificacao
    
    def enviar(self, mensagem):
        self.notificacao.enviar(mensagem)

class CriptografiaDecorator(NotificacaoDecorator):
    def enviar(self, mensagem):
        mensagem_criptografada = f"[CRIPTO] {mensagem}"
        self.notificacao.enviar(mensagem_criptografada)

class LogDecorator(NotificacaoDecorator):
    def enviar (self, mensagem):
        print(f"[LOG] enviando")
        self.notificacao.enviar(mensagem)
        print("[LOG] enviado com sucesso")

#! Observer
class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def receberNotificacao(self, mensagem):
        print(f"{self.nome} recebeu {mensagem}")

class SistemaNotificacao:
    def __init__(self):
        self.usuarios = []
        
    def adicionarUsuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nome} adicionado ao sistema de notificações.")
    
    def notificarUsuarios(self, mensagem):
        print(f"Notificando {len(self.usuarios)} usuários...")
        for usuario in self.usuarios:
            usuario.receberNotificacao(mensagem)

#Main
def main():
    print("="*50)
    print("Sistema de Notificações")
    print("="*50)
    
    # Criando sistema de notificações
    sistema = SistemaNotificacao()
    
    # Cadastrando usuários
    sistema.adicionarUsuario(Usuario("Alice"))
    sistema.adicionarUsuario(Usuario("Bob"))
    sistema.adicionarUsuario(Usuario("Charlie"))
    
    # Criando notificações usando a fábrica
    email = NotificacaoFactory.criarNotificacao("email")
    sms = NotificacaoFactory.criarNotificacao("sms")
    
    email.enviar("Bem-vindo!")
    sms.enviar("Seu código é 1234.")
    
    # Funcionalidades adicionais com Decorator
    print("\nUsando Decorators:")
    email_log = LogDecorator(email)
    sms_cripto = CriptografiaDecorator(sms)
    
    email_log.enviar("Notificação importante por email.")
    sms_cripto.enviar("Dados sensíveis por SMS.")
    
    # Notificando todos os usuários
    print("\nNotificando todos os usuários:")
    sistema.notificarUsuarios("Sistema em manutenção hoje às 22h.")
    
    # Juntando todos os padrões
    print("\nUsando todos os padrões juntos:")
    notificacaoAvancada = LogDecorator(CriptografiaDecorator(NotificacaoFactory.criarNotificacao("email")))
    notificacaoAvancada.enviar("Informações para deposito bancário.")
    

main()