class Operacao:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.historico = []
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"deposito: R$ {valor:.2f}")
            self.transacoes.push(("deposito", valor))
            print(f"deposito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("valor de deposito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"saque: R$ {valor:.2f}")
            self.transacoes.push(("saque", valor))
            print(f"saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("saldo insuficiente ou valor invalido.")