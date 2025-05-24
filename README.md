# Sistema Bancário CLI - Python

**Integrantes do Grupo:**

* João Pedro Duarte Martinez (RA: 1993686)

---

## Descrição Geral

Este é um sistema bancário com interface de linha de comando (CLI), desenvolvido em Python. O sistema permite o cadastro de clientes, criação de contas, operações de saque, depósito, controle de transações e histórico. Os dados são armazenados e manipulados utilizando diversas estruturas de dados clássicas, conforme os critérios propostos.

O objetivo do projeto é demonstrar, na prática, a aplicação de estruturas de dados aprendidas em aula no contexto de um sistema funcional.

---

## Requisitos para Execução

### 1. Pré-requisitos

* Python 3.10 ou superior instalado no sistema

### 2. Como executar o sistema

1. Clone este repositório ou baixe os arquivos `.py` com o código.

2. Execute o terminal ou prompt de comando.

3. Navegue até o diretório onde está salvo o arquivo do sistema:

```bash
cd caminho/do/arquivo
```
4. Realize a instalação da biblioteca externa Bcrypt:
```bash
!pip install bcrypt
```
5. Execute o sistema com o comando:

```bash
python main.py
```
---
## Fluxograma do sistema 
![fluxograma_P2_estrutura2 drawio](https://github.com/user-attachments/assets/9c87917c-0ac0-49d7-83ee-07a9f63e233b)


---

## Funcionalidades do Sistema

### Área do cliente

* Cadastro de clientes com o nome, CPF e senha;
* Login com CPF e senha  para ter acesso às operações;
* Criação de múltiplas contas bancárias por cliente;
* Visualização de dados do cliente e de todas as suas contas cadastradas.

### Operações bancárias
* Depósito em conta com atualização de saldo;
* Saque em conta com verificação de saldo;
* Transferência entre contas do mesmo ou entre clientes diferentes;
* Visualização do saldo em conta.

### Histórico e gerenciamento
* Registro detalhado de transações com tipo, valor, data/hora e conta envolvida;
* Visualização do histórico de transações com todas as movimentações realizadas;
* Desfazer a última transação (apenas a mais recente), restaurando os saldos anteriores.
  
---

## Estruturas de Dados Utilizadas

### 1. **Listas**

* Utilizadas para armazenar a lista geral de clientes e contas.
* Estrutura simples e eficiente para acesso sequencial e armazenamento dinâmico.

### 2. **Pilha (com lista)**

* Utilizada para registrar as transações recentes e permitir desfazer a última.
* Utilizada para exibir o histórico de transações
* Ideal para controle de operações reversíveis (último a entrar, primeiro a sair - LIFO).

### 3. **Tuplas**

* Foram utilizadas para armazenar os dados imutáveis das transações, como número da conta, tipo e valor.
* Justificativa: Estrutura imutável e leve, ideal para agrupamento simples de dados.

### 4. **Sets (conjuntos)**

* Utilizados para garantir unicidade de CPFs cadastrados.
* Operações de verificação de existência são rápidas (O(1)).

### 5. **Dicionários**

* Mapeamento de CPF → Cliente e Conta → Dados da conta.
* Acesso rápido e direto aos dados usando chaves únicas.

### 6. **Lista duplamente encadeada**

* Cada conta possui uma lista encadeada de transações.
* Utilizada para mostrar o histórico de transações.

---

## Exemplos de Uso

### Criar um cliente:

```
1. Cadastrar cliente
2. Informar nome: Gustavo Mattos
3. CPF: 12345678910
4: Senha: 12345
5: Escolher tipo de conta: 1 - Corrente
```

### Cadastrar nova conta:

```
1: Criar conta
2: Informar CPF já cadastrado
3: Informar senha do cliente
4: Escolher tipo de conta: 2 - Poupança
```

### Realizar transações:

```
3. Depositar
4. Sacar
```

### Ver informações:

```
5. Ver saldo
6. Ver histórico de transações
```

### Cancelar última operação:

```
7. Desfazer transação
```
