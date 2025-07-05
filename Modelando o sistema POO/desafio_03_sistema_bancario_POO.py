def menu(separador, espacos):
    msg_boas_vindas = "Olá! Seja bem-vindo Digite a opção corresponde a sua operação:".center(100," ")
    CABECALHO = " MENU ".center(104,"#")
    inicio = f"{espacos}{CABECALHO}\n\n{msg_boas_vindas}\n\n{espacos}{separador}"
    print(inicio)
    opcoes = ("Criar Usuário", "Criar Conta Corrente", "Depositar", "Sacar", "Extrato", "Sair")
    for i, opcao in enumerate(opcoes):
        msg_f = []
        msg_f =  (f"{i + 1}. {opcao}")
        print(f"{espacos}{msg_f}")
    print(f"{espacos}{separador}")
    escolha = input(f"{espacos}Selecione uma opção (digite o número): ")

    return escolha

def criar_usuario(*,contador,nome, dt_nascimento, cpf, endereco):

    if len(endereco) == 5:
        logradouro, numero, bairro, cidade, estado = endereco
    else:
        print("Aviso: A lista de endereço não está completa.")
    
    
    usuario = {
        "contador":str(contador),
        "nome": nome,
        "data_nascimento": dt_nascimento,
        "cpf": cpf,
        "endereco": { 
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
    }
    return usuario

def filtrar_usuario(cpf,usuarios):
    usuario_filtrados =  [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None


def verifica_cpf (cpf,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False 

def exibe_usuario(cpf,usuarios,separador,espacos):
    if usuarios:
        print(espacos,separador)
        print(f"{(espacos*11)}Dados do usuário")
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                dados = f"""
    Usuário:    {usuario['contador']}
    Nome :      {usuario['nome']}
    CPF:        {usuario['cpf']}
                        """
                print(dados)               

def sacar(*,saldo , valor, extrato,limite, numero_saques, limite_saque, espacos): 
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print(f"\n{espacos}Operação falhou! você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"\n{espacos}Operação falhou! o valor do saque excede o limite de RS:{limite:.2f} por saque.")
        elif excedeu_saques:
            print(f"\n{espacos}Operação falhou! Número máximo de saques permitido foi excedido.")

        elif valor >0:
            saldo -= valor
            extrato += f"{espacos}Saque:       R${valor:.2f}\n"
            numero_saques += 1
            print(f"{espacos} Saque realizado com sucesso!")

        else:
            print(f"\n{espacos}Operação falhou! O valor informado é inválido.")

        return saldo, extrato, numero_saques

def depositar(saldo,valor,extrato,/,espacos):  

    if valor > 0:
        saldo += valor
        extrato += f"{espacos}Depósito: \t R${valor:.2F}\n"
    else:
        print(f"Operação falhou! o valor informado é invalido")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato,sepador,espacos):
    c1 = "Extrato".center(104," ")
    estrutura_p = f"""\n{espacos}{sepador}\n{c1}\n{espacos}{sepador}\n"""
    if not extrato:
        estrutura_p += f"\n\n{espacos}Não foram realizadas movimentações! Seu saldo é de {saldo}\n\n{espacos}{sepador}\n\n"
    else:
        estrutura_p += f"{extrato}\n{espacos}Saldo final  R$:{saldo}\n{espacos}{sepador}"
    return estrutura_p

def criar_conta(*,agencia, usuarios, contador):
    for usuario in usuarios:
        if not usuario["cpf"]:
            print(f"não existe um usuario com o cpf {usuario['cpf']} cadastrado!\n")
        else:
            conta = {
                "agencia":agencia,
                "conta": contador ,
                "contador":usuario['contador']
            }
        if not conta:
            conta = f"não existem usuários"
        else:
            conta
            
        return conta
    
def main (): 
    LIMITE_SAQUE = 3
    AGENGIA = "0001"
    SEPARADOR = "#" * 104
    ESPACOS = " " * 4


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    contador = 0 
    contador2 = 0 
    while True:

        opcao = menu(SEPARADOR,ESPACOS)

        if opcao == '1':
            print(f"{ESPACOS}{SEPARADOR}\n")
            print(f"{ESPACOS}Criando usuario: {contador + 1} ")

            cpf = input("Digite o CPF: ")
            usuario = filtrar_usuario(cpf,usuarios)
            nm_usario = input("Digite o nome do usuário: ")
            dt_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")

            if verifica_cpf(cpf, usuarios):
                print("Erro: CPF já cadastrado! Por favor, digite um CPF diferente.")
                return
            
            elif not usuario:

                logradouro = input("Logradouro: ")
                numero     = input("Número: ")
                bairro     = input("Bairro: ")
                cidade     = input("Cidade: ")
                estado     = input("Estado (UF): ")

                endereco_completo = [
                    logradouro, 
                    numero,
                    bairro,
                    cidade,
                    estado]
                
                novo_usuario = criar_usuario(
                                contador=contador,
                                nome=nm_usario,
                                dt_nascimento=dt_nascimento,
                                cpf=cpf,
                                endereco=endereco_completo)

                usuarios.append(novo_usuario)
                exibe_usuario(cpf,usuarios,SEPARADOR,ESPACOS)

                contador += 1

        elif opcao == '2':

            contas = criar_conta(
                agencia=AGENGIA,
                usuarios=usuarios, 
                contador=contador2
            )
            if contas == None:
                print(f"{ESPACOS}Não possuímos usuário registrado !")
            else:
                print(f"{ESPACOS}Agência: {contas['agencia']}{ESPACOS}Conta: {contas['conta']}{ESPACOS}Usuário: {contas['contador']} criada com Sucesso!\n")
                print(f"{ESPACOS}{SEPARADOR}")
            
            contador2 += 1
        elif opcao == '3':
            valor = float(input(f"{ESPACOS}Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo,valor,extrato,ESPACOS)

        elif opcao == '4':
            valor = float(input(f"{ESPACOS}Informe o valor do saque: "))
            saldo, extrato,numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques, 
                limite_saque=LIMITE_SAQUE, 
                espacos=ESPACOS
            )
        elif opcao == '5':
            print(exibir_extrato(saldo,extrato=extrato,sepador=SEPARADOR,espacos=ESPACOS))
            
        elif opcao == '6':
            break

main()