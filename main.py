from clientes import clientes
from contas import criarConta
from clientes import cadastraCliente
from Operacao import Operacao
from historico import mostrar_historico

operacao = Operacao(numero_conta=1) 

def depositar():
    valor = float(input("Digite o valor para depósito: "))
    operacao.depositar(valor)

def sacar():
    valor = float(input("Digite o valor para saque: "))
    operacao.sacar(valor)

def mostraMenu():
    executando = True

    while(executando):
        print("------------------MENU------------------------")
        print("1) Cadastrar cliente")
        print("2) Criar conta")
        print("3) Depositar")
        print("4) Sacar")
        print("5) Mostrar historico")
        print("6) Consultar saldo")
        print("99) Mostrar clientes")
        print("0) Sair")
        resposta = int(input("Selecione a operação que deseja realizar:"))

        match resposta:
            case 1: 
                cadastraCliente()
            case 2:
                criarConta()
            case 3:
                depositar()
            case 4:
                sacar()
            case 5:
                mostrar_historico(operacao)
            case 6:
                operacao.consultar()
            case 99: 
                for cliente in clientes:
                    print(clientes[cliente])
            case 0: executando = False

if __name__ == "__main__":
    mostraMenu()
