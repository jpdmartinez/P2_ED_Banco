clientes = {}
cpfs_cadastrados = set()
contas_cadastradas = set()
executando = True

def cadastraCliente():
    nome = input("Nome do Cliente:")
    cpf = input("CPF do cliente:")

    if cpf in cpfs_cadastrados:
        print("CPF já cadastrado!")
        return

    cpfs_cadastrados.add(cpf)
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "contas": []
    }
    clientes[cpf] = cliente
    print("Cliente cadastrado com sucesso!")


def criarConta():
    cpf = input("CPF do cliente:")

    if cpf not in cpfs_cadastrados:
        print("CPF não cadastrado!")
        return
    
    opcao = input("Tipo de conta (1 - corrente ou 2 - poupança):")
    if opcao == "1":
        tipo_conta = "corrente"
    elif opcao == "2":
        tipo_conta = "poupança"
    else:
        print("Opção inválida!")
        return

    numero_conta = len(contas_cadastradas) + 1
    clientes.get(cpf)["contas"].append({
        "numero": numero_conta,
        "tipo": tipo_conta,
        "agencia": 250,
        "saldo": 0
    })
    contas_cadastradas.add(numero_conta)
    print(f"Conta {numero_conta} criada com sucesso para o cliente {clientes[cpf]["nome"]}!")

while(executando):
    print("------------------MENU------------------------")
    print("1) Cadastrar cliente")
    print("2) Criar conta")
    print("99) Mostrar clientes")
    print("0) Sair")
    resposta = int(input("Selecione a operação que deseja realizar:"))

    match resposta:
        case 1: 
            cadastraCliente()
        case 2:
            criarConta()
        case 99: 
            for cliente in clientes:
                print(clientes[cliente])
        case 0: executando = False