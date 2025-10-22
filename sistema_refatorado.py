from abc import ABC, abstractmethod

# Pagamentos
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class CartaoCredito(Pagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com Cartão de Crédito...")

class Boleto(Pagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")

class Pix(Pagamento):
    def pagar(self, pedido):
        print(f"Realizando pagamento via PIX no valor de R$ {pedido['valor']:.2f}...")


# Notificações
class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass

class EmailNotificador(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")

class SmsNotificador(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para o cliente...")

# Processador de Pedidos
class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: Pagamento, notificador: Notificador):
        self.metodo_pagamento = metodo_pagamento
        self.notificador = notificador

    def processar(self, pedido):
        print(f"Processando pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.notificador.notificar(pedido)
        pedido['status'] = 'concluido'
        print("✅ Pedido concluído!")


# Exemplo de uso
if __name__ == "__main__":
    pedido1 = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    processador = ProcessadorDePedidos(CartaoCredito(), EmailNotificador())
    processador.processar(pedido1)

    print("-" * 30)

    pedido2 = pedido1.copy()
    pedido2['id'] = 456
    processador_pix_sms = ProcessadorDePedidos(Pix(), SmsNotificador())
    processador_pix_sms.processar(pedido2)
