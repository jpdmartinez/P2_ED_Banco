from datetime import datetime
import Clientes

#Nó da lista duplamente encadeada
class Node: 
    def __init__(self, data: tuple):
        self.data = data  
        self.prev = None
        self.next = None

# Histórico de transações de um cliente
class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    # Função para realizar uma nova transação (inserção no final da lista)
    def push(self, tipo: str, valor: float, numero_conta: int):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        tupla = (tipo, valor, data_hora, numero_conta)
        novo_no = Node(tupla)  
        
        if self.head is None:
            self.head = self.tail = novo_no
        else:
            self.tail.next = novo_no
            novo_no.prev = self.tail
            self.tail = novo_no
    # Função para exibir todas as transações de um cliente
    def listar(self, nome_cliente):
        atual = self.head
        print(f"Histórico de transações do(a) {nome_cliente}:")
        if atual is None:
            print("Nenhuma transação registrada.")
            return
    
    # Percorre a lista imprimindo as transações
        while atual:
            tipo, valor, data, numero_conta = atual.data
            print(f"{data} - Conta {numero_conta} -{tipo}: R$ {valor:.2f}")
            atual = atual.next
    
    # Função para desfazer a última transação realizada
    def desfazer_ultima_transacao(self):
        if self.tail is None:
            print("Não há transaçõespara defazer.")
            return None
        
        tipo, valor, data, numero_conta = self.tail.data
        
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
        
        print(f"Última transação desfeita: {tipo} de R$ {valor:.2f} na conta {numero_conta}.")
        return tipo, valor, numero_conta 

# Função para exibir o histórico de um cliente auntenticando pelo CPF
def mostrar_historico():
    cpf = Clientes.verificaCPF()
    if cpf not in Clientes.clientes:
        print("Cliente não encontrado!")
        return
    nome = Clientes.clientes[cpf]['nome']
    historico = Clientes.clientes[cpf]['historico']
    historico.listar(nome)
    
