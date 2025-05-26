from historico import DoublyLinkedList
import bcrypt
import contas

# Dicionário para armazenar os dados dos clientes
clientes = {}
# Conjunto para registrar todos os CPFs cadastrados
cpfs_cadastrados = set()

# Função para solicitar e validar o CPF do usuário
def verificaCPF():
    while True:
        cpf = input("Digite o CPF (somente números): ")
        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        print("CPF inválido! Digite exatamente 11 números.")

# Função para cadastrar um novo cliente no sistema
def cadastraCliente():
    nome = input("Nome do Cliente:")
    cpf = verificaCPF()

    if cpf in cpfs_cadastrados:
        print("CPF já cadastrado!")
        return

    cpfs_cadastrados.add(cpf)
    
    # Criptografa a senha
    senha = criptografar_senha(input("Digite uma senha: "))
    
    # Cria um dicionário com os dados do novo cliente
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "contas": [],                   # Lista de contas associadas ao cliente
        "historico": DoublyLinkedList() # Histórico de transações
    }
    clientes[cpf] = cliente

    contas.criarConta(cpf=cpf)

    print("Cliente cadastrado com sucesso!")

# Função para criptografar a senha utilizando o bcrypt
def criptografar_senha(senha):
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    return hash_senha

# Função para verificar se a senha digitada corresponde ao hash armazenado
def verificar_senha(senha_digitada, hash_senha_armazenado):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_senha_armazenado)