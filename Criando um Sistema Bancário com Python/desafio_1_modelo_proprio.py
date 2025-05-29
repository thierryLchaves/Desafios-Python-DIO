menu = """

[d] Depositar 
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

def depositar_dineiro(valor_deposito):
    global saldo 
    global extrato 

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor de depósito inválido. (Global)")

def sacar_dinheiro (valor_saque):
    global saldo
    global numero_saques
    global extrato

    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUE

    if excedeu_saldo:

        print(f"\n### Não foi possível sacar o dinheiro informado pois não tem saldo suficiente em conta ###")

    elif excedeu_limite:

        print(f"\n ### O valor de {valor_saque} solicitado no saque excede o limite de saques definido ###")

    elif excedeu_saques:
        print(f"\n ### Não foi possível realizar a transação pois foram o limite de saques no dia foi atingido ###")
    
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato += str(valor_saque)
        print(f"\n ### Realizando saque de R$ {valor_saque:.2f}")

    else:
        print(f"\n ### Operação falho! O valro informado para o valor de saque não é um valor valido")
        
def exibir_extrato():
    print("EXTRATO".center(14,"#"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("======================================\n")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))    
        depositar_dineiro(valor_deposito=valor_deposito)

    elif opcao == "s":

            valor_saque = float(input("Informe o valor do saque: "))
            sacar_dinheiro(valor_saque=valor_saque)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação.")