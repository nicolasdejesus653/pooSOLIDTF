# Exercício Prático: Refatorando com SOLID

## Objetivo

Aplicar os princípios SOLID para refatorar um sistema de processamento de pedidos, tornando-o mais robusto, flexível e manutenível.

## Descrição do Problema

Você recebeu um trecho de código de um sistema de e-commerce. Atualmente, a classe `ProcessadorDePedidos` é responsável por processar um pedido, realizar o pagamento e notificar o cliente. O sistema funciona, mas o código está se tornando difícil de manter e estender. Por exemplo, para adicionar uma nova forma de pagamento (como Pix) ou um novo método de notificação (como SMS), é necessário modificar a classe `ProcessadorDePedidos` diretamente.

Seu trabalho é refatorar o código para que ele siga os princípios SOLID.

## Código Inicial (Problemático)

```python
# sistema_pedidos.py

class ProcessadorDePedidos:
    def processar(self, pedido, tipo_pagamento):
        # 1. Lógica de processamento do pedido
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")

        # 2. Lógica de pagamento
        if tipo_pagamento == "cartao_credito":
            print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")
            # Lógica específica para pagamento com cartão
        elif tipo_pagamento == "boleto":
            print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")
            # Lógica específica para pagamento com boleto
        
        # 3. Lógica de notificação
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")
        # Lógica para enviar e-mail

        # 4. Finalização
        pedido['status'] = 'concluido'
        print("Pedido concluído!")


# --- Como o cliente usaria o código ---
if __name__ == "__main__":
    meu_pedido = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    processador = ProcessadorDePedidos()
    # Processando um pedido com cartão de crédito
    processador.processar(meu_pedido, "cartao_credito")

    print("-"*20)

    # Processando outro pedido com boleto
    meu_pedido_2 = meu_pedido.copy()
    meu_pedido_2['id'] = 456
    processador.processar(meu_pedido_2, "boleto")
```

## Sua Tarefa

1.  **Análise:** Identifique quais princípios SOLID estão sendo violados no código acima. Escreva uma breve explicação para cada violação encontrada.

2.  **Refatoração:** Refatore o código para que ele atenda aos 5 princípios SOLID. Crie as classes e interfaces (classes abstratas em Python) que julgar necessárias. O objetivo é que o novo sistema permita adicionar novas formas de pagamento e novos métodos de notificação **sem alterar o código existente**.
    -   **Dica:** Pense em separar as responsabilidades (SRP), criar abstrações para pagamentos e notificações (DIP) e permitir a extensão do sistema (OCP).

3.  **Explicação:** Junto ao código refatorado, adicione comentários ou um texto explicando as mudanças que você fez e como elas resolvem os problemas identificados, conectando cada mudança a um ou mais princípios SOLID.

## Bônus (Opcional)

Após a refatoração, demonstre a flexibilidade do seu novo design adicionando:

-   Um novo método de pagamento: **Pix**.
-   Um novo método de notificação: **SMS**.

Mostre como o sistema lida com essas novas funcionalidades sem a necessidade de modificar as classes de processamento de pedidos já existentes.

## Instruções de Entrega

1.  **Faça um Fork** deste repositório.
2.  Em seu repositório "forkado", crie uma nova pasta chamada `resolucao`.
3.  Dentro da pasta `resolucao`, adicione:
    *   Um arquivo Python (ex: `sistema_refatorado.py`) com o código final refatorado.
    *   Um arquivo `ANALISE.md` contendo a sua análise das violações dos princípios SOLID e a explicação das suas refatorações.
4.  Faça o commit e o push das suas alterações para o seu fork.
5.  **Abra um Pull Request (PR)** do seu fork para este repositório original. O sistema de integração contínua irá verificar sua solução.