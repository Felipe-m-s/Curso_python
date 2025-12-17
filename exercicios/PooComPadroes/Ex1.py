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

#todo Uso do Factory Method

