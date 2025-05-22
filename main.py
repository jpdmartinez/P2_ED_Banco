import Clientes
import contas
from historico import mostrar_historico
from Operacao import Operacao

operacao = Operacao(numero_conta=1) 

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
                Clientes.cadastraCliente()
            case 2:
                contas.criarConta()
            case 3:
                Operacao.depositar(operacao)
            case 4:
                Operacao.sacar()
            case 5:
                mostrar_historico(operacao)
            case 6:
                operacao.consultar()
            case 99: 
                for cliente in Clientes.clientes:
                    print(Clientes.clientes[cliente])
            case 0: executando = False

if __name__ == "__main__":
    mostraMenu()
