import Clientes
import Operacao

contas_cadastradas = set()

def criarConta(cpf=None):
    if cpf == None:
        cpf = Clientes.verificaCPF()
        senha = input("Digite sua senha:")
        verificaSenha = Clientes.verificar_senha(senha, Clientes.clientes[cpf]['senha'])

        if cpf not in Clientes.cpfs_cadastrados:
            print("CPF não cadastrado!")
            return
    else:
        cpf = cpf
        verificaSenha = True

    if verificaSenha:
        opcao = input("Tipo de conta (1 - corrente ou 2 - poupança):")
        if opcao == "1":
            tipo_conta = "corrente"
        elif opcao == "2":
            tipo_conta = "poupança"
        else:
            print("Opção inválida!")
            return

        numero_conta = len(contas_cadastradas) + 1
        Clientes.clientes.get(cpf)["contas"].append({
            "numero": numero_conta,
            "tipo": tipo_conta,
            "agencia": 250,
            "saldo": 0
        })
        contas_cadastradas.add(numero_conta)
        print(f"Conta {numero_conta} criada com sucesso para o cliente {Clientes.clientes[cpf]['nome']}!\n")
    else:
        print("Senha incorreta!")

def buscar_numero(numero_conta):
    for cpf, dados in Clientes.clientes.items():
        for conta in dados['contas']:
            if conta['numero'] == numero_conta:
                return conta, cpf
    return None
