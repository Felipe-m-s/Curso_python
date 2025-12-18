from abc import ABC, abstractmethod

class ProcessadorPagamento(ABC):   # Classe abstrata para processadores de pagamento
    @abstractmethod
    def processar(self, valor):   # Método abstrato para processar pagamentos
        pass

class PayPalProcessador(ProcessadorPagamento):   # Classe concreta para processar pagamentos via PayPal
    def processar(self, valor):
        return f"Processando pagamento de {valor} via PayPal."

class StripeProcessador(ProcessadorPagamento):    # Classe concreta para processar pagamentos via Stripe
    def processar(self, valor):
        return f"Processando pagamento de {valor} via Stripe."

class MercadoPagoProcessador(ProcessadorPagamento):  # Classe concreta para processar pagamentos via MercadoPago
    def processar(self, valor):
        return f"Processando pagamento de {valor} via MercadoPago."
    
#! Fábrica de Processadores de Pagamento
class ProcessadorPagamentoFactory:
    @staticmethod
    def criarProcessador(tipo):
        if tipo.strip().lower() == "paypal":
            return PayPalProcessador()
        elif tipo.strip().lower() == "stripe":
            return StripeProcessador()
        elif tipo.strip().lower() == "mercadopago":
            return MercadoPagoProcessador()
        else:
            raise ValueError("Tipo de processador de pagamento invalido.")

#todo Uso do Factory Method
