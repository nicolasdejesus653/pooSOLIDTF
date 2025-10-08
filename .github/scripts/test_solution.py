import importlib.util
import io
import os
import sys
from contextlib import redirect_stdout

def run_test():
    """
    Executa uma série de verificações na solução refatorada do aluno.
    """
    submission_path = None
    resolucao_dir = 'resolucao'

    if not os.path.isdir(resolucao_dir):
        print(f"❌ Erro: O diretório '{resolucao_dir}' não foi encontrado.")
        sys.exit(1)

    py_files = [f for f in os.listdir(resolucao_dir) if f.endswith('.py')]
    if not py_files:
        print(f"❌ Erro: Nenhum arquivo Python encontrado no diretório '{resolucao_dir}'.")
        sys.exit(1)
    
    # Heurística: encontrar um arquivo que não seja __init__.py, ou pegar o primeiro.
    submission_file = next((f for f in py_files if f != '__init__.py'), py_files[0])
    submission_path = os.path.join(resolucao_dir, submission_file)

    print(f"🐍 Encontrado arquivo de solução: {submission_path}")

    try:
        # Importa dinamicamente a solução do aluno.
        spec = importlib.util.spec_from_file_location("submission", submission_path)
        submission_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(submission_module)
        print("✅ Módulo da solução importado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao importar o módulo da solução: {e}")
        sys.exit(1)

    captured_output = ""
    stdout_capture = io.StringIO()
    with redirect_stdout(stdout_capture):
        try:
            print("▶️ Tentando executar o cenário de teste refatorado...")

            # Abstrações (o aluno deve tê-las criado)
            Pagamento = getattr(submission_module, 'Pagamento', None)
            Notificacao = getattr(submission_module, 'Notificacao', None)

            # Implementações Concretas
            PagamentoCartao = getattr(submission_module, 'PagamentoCartao', None)
            PagamentoBoleto = getattr(submission_module, 'PagamentoBoleto', None)
            PagamentoPix = getattr(submission_module, 'PagamentoPix', None) # Bônus
            NotificacaoEmail = getattr(submission_module, 'NotificacaoEmail', None)
            NotificacaoSMS = getattr(submission_module, 'NotificacaoSMS', None) # Bônus

            ProcessadorDePedidos = getattr(submission_module, 'ProcessadorDePedidos', None)

            if not all([ProcessadorDePedidos, PagamentoCartao, PagamentoBoleto, NotificacaoEmail]):
                 print("❌ Erro: Classes essenciais (ProcessadorDePedidos, PagamentoCartao, PagamentoBoleto, NotificacaoEmail) não encontradas na solução.")
                 sys.exit(1)

            pedido = {
                'id': 789,
                'valor': 250.00,
                'cliente_email': 'teste@exemplo.com',
                'cliente_telefone': '5511999998888',
                'status': 'pendente'
            }

            # Caso de teste 1: Cartão de Crédito + Email
            processador_cc = ProcessadorDePedidos(PagamentoCartao(), NotificacaoEmail())
            processador_cc.processar(pedido)

            # Caso de teste 2: Boleto + Email
            processador_boleto = ProcessadorDePedidos(PagamentoBoleto(), NotificacaoEmail())
            processador_boleto.processar(pedido)

            # Caso de teste 3 (Bônus): Pix + SMS
            if PagamentoPix and NotificacaoSMS:
                print("▶️ Testando funcionalidade bônus (Pix + SMS)...")
                processador_pix_sms = ProcessadorDePedidos(PagamentoPix(), NotificacaoSMS())
                processador_pix_sms.processar(pedido)

        except Exception as e:
            print(f"❌ Erro ao executar o cenário de teste: {e}")
            # Imprime a saída capturada até o momento para ajudar na depuração.
            print("\n--- SAÍDA CAPTURADA ATÉ O ERRO ---")
            print(stdout_capture.getvalue())
            print("------------------------------------")
            sys.exit(1)

    captured_output = stdout_capture.getvalue()
    print("\n--- SAÍDA COMPLETA CAPTURADA ---")
    print(captured_output)
    print("--------------------------------")


    # --- Verificação ---
    print("\n🔍 Verificando a saída...")
    checks = {
        "Processando o pedido": False,
        "com cartão de crédito": False,
        "Gerando boleto": False,
        "Enviando e-mail": False,
    }

    output_lower = captured_output.lower()
    
    if "processando o pedido" in output_lower:
        checks["Processando o pedido"] = True
    if "cartão de crédito" in output_lower:
        checks["com cartão de crédito"] = True
    if "boleto" in output_lower:
        checks["Gerando boleto"] = True
    if "e-mail" in output_lower:
        checks["Enviando e-mail"] = True

    # Verificações de bônus
    bonus_checks = {
        "Pagando com Pix": "pix" in output_lower,
        "Enviando SMS": "sms" in output_lower,
    }

    all_passed = True
    for check, passed in checks.items():
        if passed:
            print(f"✅ OK: '{check}'")
        else:
            print(f"❌ FALHA: A saída não contém '{check}'")
            all_passed = False

    if bonus_checks["Pagando com Pix"]:
        print("✅ OK (Bônus): 'Pagamento com Pix'")
    else:
        print("⚠️ AVISO (Bônus): A saída não contém 'Pagamento com Pix'")

    if bonus_checks["Enviando SMS"]:
        print("✅ OK (Bônus): 'Notificação via SMS'")
    else:
        print("⚠️ AVISO (Bônus): A saída não contém 'Notificação via SMS'")


    if not all_passed:
        print("\n🚫 Alguns testes falharam.")
        sys.exit(1)
    else:
        print("\n🎉 Todos os testes passaram!")
        sys.exit(0)

if __name__ == "__main__":
    run_test()