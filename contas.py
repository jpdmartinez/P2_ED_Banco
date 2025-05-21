import bcrypt
import Clientes
from Operacao import Operacao

contas_cadastradas = set()

def criarConta(primeiraConta, cpf=None):
    if not primeiraConta:
        cpf = Clientes.verificaCPF()

        if cpf not in Clientes.cpfs_cadastrados:
            print("CPF não cadastrado!")
            return
    else:
        cpf = cpf

    opcao = input("Tipo de conta (1 - corrente ou 2 - poupança):")
    if opcao == "1":
        tipo_conta = "corrente"
    elif opcao == "2":
        tipo_conta = "poupança"
    else:
        print("Opção inválida!")
        return

    senha = criptografar_senha(input("Digite uma senha: "))

    numero_conta = len(contas_cadastradas) + 1
    Clientes.clientes.get(cpf)["contas"].append({
        "numero": numero_conta,
        "senha": senha,
        "tipo": tipo_conta,
        "agencia": 250,
        "saldo": 0
    })
    contas_cadastradas.add(numero_conta)
    print(f"Conta {numero_conta} criada com sucesso para o cliente {Clientes.clientes[cpf]["nome"]}!\n")

def criptografar_senha(senha):
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    return hash_senha

def verificar_senha(senha_digitada, hash_senha_armazenado):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_senha_armazenado)

def depositar():
    valor = float(input("Digite o valor para depósito: "))
    Operacao.depositar(valor)

def sacar():
    valor = float(input("Digite o valor para saque: "))
    Operacao.sacar(valor)