import textwrap

def menu():
    sepador = "#" * 100
    msg_boas_vindas = "Olá! Seja bem-vindo Digite a opção corresponde a sua operação:".center(100," ")
    menu =f"""
    {sepador} \n
    {msg_boas_vindas}
    {sepador}\n
    [u] Criar Usuário 
    [d] Criar Conta corrente 
    [d] Depositar 
    [s] Sacar 
    [e] Extrato
    [q] Sair
    {sepador}
    => """
    return input(menu)

        
   
def sacar(*,saldo , valor, extrato,limite, numero_saques, limite_saque): 
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            
            print(f"Operação falhou! você não tem saldo suficiente.")

        elif excedeu_limite:
            
            print(f"Operação falhou! o valor do saque excede o limite.")

        elif excedeu_saques:

            print(f"Operação falhou! Número máximo de saque excedido.")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print(f"Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def depositar(saldo,valor,extrato,/):  

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \t R${valor:2F}\n"
    else:
        print(f"Operação falhou! o valor informado é invalido")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    sepador = "#" * 100
    msg_retorno_final= []
    msg_retorno_negativo = f"""
    {sepador}
                    EXTRATO
    {sepador}
        "Não foram realizadas movimentações, em sua conta"
    """
    msg_retorno_positivo = f"""
    {sepador}
    {sepador}
    Saldo: R$ {saldo:.2f}
    """
    if not extrato:
        msg_retorno_final = msg_retorno_negativo
    else:
        msg_retorno_final = msg_retorno_positivo
    
    return msg_retorno_final

def main ():
    LIMITE_SAQUE = 3
    AGENGIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 3
    usuario = []
    contas = []

    while True:
        opcao = menu().lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo,valor,extrato)

        if opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques, 
                limite_saque=LIMITE_SAQUE
            )
        elif opcao == 'e':
            print(exibir_extrato(saldo,extrato=extrato))
            
        elif opcao == "q":
            break

main()