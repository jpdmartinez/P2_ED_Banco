import bcrypt
import contas

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
    
    senha = criptografar_senha(input("Digite uma senha: "))
    
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "contas": []
    }
    clientes[cpf] = cliente

    contas.criarConta(cpf=cpf)

    print("Cliente cadastrado com sucesso!")
    
def criptografar_senha(senha):
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    return hash_senha

def verificar_senha(senha_digitada, hash_senha_armazenado):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_senha_armazenado)