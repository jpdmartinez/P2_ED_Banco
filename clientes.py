clientes = {}
cpfs_cadastrados = set()

def verificaCPF():
    while True:
        cpf = input("Digite o CPF (somente números): ")
        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        print("CPF inválido! Digite exatamente 11 números.")


def cadastraCliente():
    nome = input("Nome do Cliente:")
    cpf = verificaCPF()

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