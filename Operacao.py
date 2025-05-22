from historico import DoublyLinkedList
import Clientes 
import contas


class Operacao:
    def __init__(self):
        self.transacoes = DoublyLinkedList()
        
    def autenticar_conta(self):
        numero = int(input("Digite o número da conta:"))
        conta, cpf = contas.buscar_numero(numero)

        if conta is None:
            print("Conta não existe")
            return None
        
        senha = input("Digite sua senha:")

        if not Clientes.verificar_senha(senha, Clientes.clientes[cpf]['senha']):
            print("Senha incorreta!")
            return None
        
        return conta, cpf

    
    def depositar(self):
        conta, cpf = self.autenticar_conta()
        if conta is None:
            return

        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            conta['saldo'] += valor
            self.transacoes.push("deposito", valor)
            print(f"deposito de R$ {valor:.2f} realizado com sucesso na conta {conta['numero']} do(a) cliente {Clientes.clientes[cpf]['nome']}.")
        else:
            print("valor de deposito inválido.")

    def sacar(self):
        conta, cpf = self.autenticar_conta()
        if conta is None:
            return

        valor = float(input("Digite o valor para saque: "))
        if 0 < valor <= self.saldo:
            conta['saldo'] -= valor
            self.transacoes.push("saque", valor)
            print(f"saque de R$ {valor:.2f} realizado com sucesso na conta {conta['numero']} do(a) cliente {Clientes.clientes[cpf]['nome']}")
        else:
            print("saldo insuficiente ou valor invalido.")
            
    def consultar(self):
        conta, _ = self.autenticar_conta()
        if conta is None:
            return

        print(f"Saldo atual da conta {conta['numero']}: R$ {conta['saldo']:.2f}")
