import contas
import Clientes
import historico

def autenticar_conta():
    try:
        numero = int(input("Digite o número da conta:"))
        
    except ValueError:
        print("Número da conta inválido!")
        return None
    
    resultado = contas.buscar_numero(numero)
    if resultado is None:
        print("Conta não existe")
        return None
        
    conta, cpf = resultado
        
    senha = input("Digite sua senha:")

    if not Clientes.verificar_senha(senha, Clientes.clientes[cpf]['senha']):
        print("Senha incorreta!")
        return None
        
    return conta, cpf

    
def depositar():
    resultado = autenticar_conta()
    if resultado is None:
        return
    
    conta, cpf = resultado

    valor = float(input("Digite o valor para depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        Clientes.clientes[cpf]['historico'].push("Depósito", valor, conta['numero'])
        print(f"""
deposito de R$ {valor:.2f} realizado com sucesso
conta {conta['numero']}
cliente {Clientes.clientes[cpf]['nome']}
""")
    else:
        print("valor de deposito inválido.")

def sacar():
    resultado = autenticar_conta()
    if resultado is None:
        return
    conta, cpf = resultado
    valor = float(input("Digite o valor para saque: "))
    if 0 < valor <= conta['saldo']:
        conta['saldo'] -= valor
        Clientes.clientes[cpf]['historico'].push("Saque", valor, conta['numero'])
        print(f"saque de R$ {valor:.2f} realizado com sucesso na conta {conta['numero']} do(a) cliente {Clientes.clientes[cpf]['nome']}")
    else:
        print("saldo insuficiente ou valor invalido.")

def transferir():
    print("Transferir")
    resultado_origem = autenticar_conta()
    if resultado_origem is None:
        return
    
    conta_origem, cpf_origem = resultado_origem
    
    try:
        numero_destino = int(input("Digite o número da conta de destino:"))
    except ValueError:
        print("Número da conta inválido!")
        return
    
    resultado_destino = contas.buscar_numero(numero_destino)
    if resultado_destino is None:
        print("Conta não encontrada!")
        return
    
    conta_destino, cpf_destino = resultado_destino
    
    valor = float(input("Digite o valor para transferir:"))
    if valor <= 0:
        print("Valor inválido para transferência")
        return
    
    if valor > conta_origem['saldo']:
        print("Saldo insuficiente para realizar transferência.")
        return
    
    conta_origem['saldo'] -= valor
    conta_destino['saldo'] += valor
    
    Clientes.clientes[cpf_origem]['historico'].push(
    f"Transferência enviada para: Conta {conta_destino['numero']} - Cliente {Clientes.clientes[cpf_destino]['nome']}",
    valor,
    conta_origem['numero']
    )

    
    Clientes.clientes[cpf_destino]['historico'].push(
    f"Transferência recebida de: Conta {conta_origem['numero']} - Cliente {Clientes.clientes[cpf_origem]['nome']}",
    valor,
    conta_destino['numero']
    )

    
    print(f"""
Transferência de R$ {valor:.2f} realizada com sucesso!
De: Conta {conta_origem['numero']} - Cliente {Clientes.clientes[cpf_origem]['nome']}
Para: Conta {conta_destino['numero']} - Cliente {Clientes.clientes[cpf_destino]['nome']}
""")
    
def desfazer_ultima_transacao():
    resultado = autenticar_conta()
    if resultado is None:
        return
    
    conta, cpf = resultado
    historico_cliente = Clientes.clientes[cpf]['historico']
    
    resultado_transacao = historico_cliente.desfazer_ultima_transacao()
    
    if resultado_transacao is None:
        return
    
    tipo, valor, numero_conta = resultado_transacao
    
    if tipo == "Depósito":
        conta['saldo'] -= valor
        print(f"Depósito de R$ {valor:.2f} desafio com sucesso.")
    
    elif tipo == "Saque":
        conta['saldo'] += valor
        print(f"Saque de R$ {valor:.2f} desfeito com sucesso.")

    elif "Transferência enviada para" in tipo:
        numero_conta_destino = int(tipo.split("Conta")[1].split("-")[0].strip())
        conta_destino, cpf_destino = contas.buscar_numero(numero_conta_destino)
        
        conta['saldo'] += valor
        conta_destino['saldo'] -=valor
        print(f"Tranferência enviada desfeita com sucesso")
        
    elif "Transferência recebida de" in tipo:
        numero_conta_origem, cpf_origem = int(tipo.split("Conta")[1].split("-")[0].strip())
        conta_origem = contas.buscar_numero(numero_conta_origem)
        
        conta['saldo'] -= valor
        conta_origem['saldo'] +=valor
        print(f"Tranferência recebida desfeita com sucesso")
    
    
def consultar():
    resultado = autenticar_conta()
    if resultado is None:
        return
        
    conta, cpf = resultado

    print(f"Saldo atual da conta {conta['numero']} do(a) cliente {Clientes.clientes[cpf]['nome']}: R$ {conta['saldo']:.2f}")