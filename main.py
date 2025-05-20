from clientes import clientes
from contas import criarConta
from clientes import cadastraCliente

def mostraMenu():
    executando = True

    while(executando):
        print("------------------MENU------------------------")
        print("1) Cadastrar cliente")
        print("2) Criar conta")
        print("99) Mostrar clientes")
        print("0) Sair")
        resposta = int(input("Selecione a operação que deseja realizar:"))

        match resposta:
            case 1: 
                cadastraCliente()
            case 2:
                criarConta()
            case 99: 
                for cliente in clientes:
                    print(clientes[cliente])
            case 0: executando = False

if __name__ == "__main__":
    mostraMenu()