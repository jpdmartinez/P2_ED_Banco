import Clientes

# Conjunto que armazena os números de contas já criadas para evitar duplicidade
contas_cadastradas = set()

# Função para criar uma nova conta bancária para um cliente já cadstrado
def criarConta(cpf=None):
    if cpf == None:
        cpf = Clientes.verificaCPF()
        

        if cpf not in Clientes.cpfs_cadastrados:
            print("CPF não cadastrado!")
            return
        
        senha = input("Digite sua senha:")
        verificaSenha = Clientes.verificar_senha(senha, Clientes.clientes[cpf]['senha'])
    else:
        cpf = cpf
        verificaSenha = True
    # Se a senha for válida (ou a verificação for ignorada)
    if verificaSenha:
        opcao = input("Tipo de conta (1 - corrente ou 2 - poupança):")
        if opcao == "1":
            tipo_conta = "corrente"
        elif opcao == "2":
            tipo_conta = "poupança"
        else:
            print("Opção inválida!")
            return

        # Gera um número único para a conta nova
        numero_conta = len(contas_cadastradas) + 1

        # Adiciona a nova conta ao cliente no dicionário de clientes
        Clientes.clientes.get(cpf)["contas"].append({
            "numero": numero_conta,
            "tipo": tipo_conta,
            "agencia": 250,
            "saldo": 0
        })

        # Armazena o número da conta no conjunto
        contas_cadastradas.add(numero_conta)
        print(f"Conta {numero_conta} criada com sucesso para o cliente {Clientes.clientes[cpf]['nome']}!\n")
    else:
        print("Senha incorreta!")

# Função pra buscar uma conta existente 
def buscar_numero(numero_conta):
    for cpf, dados in Clientes.clientes.items():
        for conta in dados['contas']:
            if conta['numero'] == numero_conta:
                return conta, cpf
    return None
