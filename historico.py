from datetime import datetime

class Node: 
    def __init__(self, data: tuple):
        self.data = data  
        self.prev = None
        self.next = None

class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, tipo: str, valor: float):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        tupla = (tipo, valor, data_hora)
        novo_no = Node(tupla)  
        
        if self.head is None:
            self.head = self.tail = novo_no
        else:
            self.tail.next = novo_no
            novo_no.prev = self.tail
            self.tail = novo_no

    def listar(self):
        atual = self.head
        print("Histórico de transações:")
        while atual:
            tipo, valor, data = atual.data
            print(f"{data} - {tipo}: R$ {valor:.2f}")
            atual = atual.next
    
def mostrar_historico(operacao):
    operacao.transacoes.listar()
