from clientes import verificaCPF
from clientes import cpfs_cadastrados
from clientes import clientes

contas_cadastradas = set()

def criarConta():
    cpf = verificaCPF()

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
    print(f"Conta {numero_conta} criada com sucesso para o cliente {clientes[cpf]["nome"]}!\n")