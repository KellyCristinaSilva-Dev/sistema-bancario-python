# Módulo: sistema_bancario.py

# --- Início da Configuração do Sistema ---

# Define o menu de opções que será exibido ao usuário.
# Usar """ (aspas triplas) permite escrever um texto em múltiplas linhas.
menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Inicializa as variáveis que controlarão o estado da conta.
saldo = 0.0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

# --- Fim da Configuração do Sistema ---


# --- Início do Loop Principal do Programa ---

# O loop 'while True' cria um ciclo infinito que só será quebrado
# quando o usuário decidir sair (opção 'q').
while True:

    # Exibe o menu e aguarda a entrada do usuário.
    # O .lower() converte a entrada para minúscula para evitar problemas
    # se o usuário digitar 'D' em vez de 'd'.
    opcao = input(menu).lower()

    # --- Lógica da Operação de Depósito ---
    if opcao == "d":
        print("\n--- Depósito ---")
        try:
            valor_deposito = float(input("Informe o valor do depósito: R$ "))

            # Verifica se o valor do depósito é positivo.
            if valor_deposito > 0:
                saldo += valor_deposito  # Adiciona o valor ao saldo.
                # Adiciona a transação ao extrato.
                # A formatação ':.2f' garante que o valor seja exibido com duas casas decimais.
                extrato += f"Depósito:\t+ R$ {valor_deposito:.2f}\n"
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado deve ser positivo.")

        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    # --- Lógica da Operação de Saque ---
    elif opcao == "s":
        print("\n--- Saque ---")
        try:
            valor_saque = float(input("Informe o valor do saque: R$ "))

            # Verifica as várias condições para o saque ser válido.
            excedeu_saldo = valor_saque > saldo
            excedeu_limite_por_saque = valor_saque > limite_por_saque
            excedeu_saques_diarios = numero_saques >= LIMITE_SAQUES_DIARIO

            if excedeu_saldo:
                print(f"Operação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo:.2f})")
            
            elif excedeu_limite_por_saque:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por operação.")

            elif excedeu_saques_diarios:
                print(f"Operação falhou! Você já atingiu o limite de {LIMITE_SAQUES_DIARIO} saques diários.")
            
            # Se o valor for positivo e nenhuma condição de falha for atendida.
            elif valor_saque > 0:
                saldo -= valor_saque  # Subtrai o valor do saldo.
                extrato += f"Saque:\t\t- R$ {valor_saque:.2f}\n" # Adiciona ao extrato.
                numero_saques += 1  # Incrementa o contador de saques.
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    # --- Lógica da Operação de Extrato ---
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        # Se a string 'extrato' estiver vazia, significa que não houve movimentação.
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        
        # O saldo é exibido em ambos os casos (com ou sem movimentação).
        print(f"\nSaldo Atual:\t  R$ {saldo:.2f}")
        print("=====================================")

    # --- Lógica da Opção de Sair ---
    elif opcao == "q":
        print("\nObrigado por usar nosso sistema bancário. Volte sempre!")
        break  # O comando 'break' encerra o loop 'while True'.

    # --- Lógica para Opção Inválida ---
    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")

# --- Fim do Loop Principal do Programa ---