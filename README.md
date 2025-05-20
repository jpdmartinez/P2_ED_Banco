# Sistema Bancário CLI - Python

**Integrantes do Grupo:**

* João Pedro Duarte Martinez (RA: 1993686)

---

## 💡 Descrição Geral

Este é um sistema bancário com interface de linha de comando (CLI), desenvolvido em Python. O sistema permite o cadastro de clientes, criação de contas, operações de saque, depósito, controle de transações e atendimento em fila. Os dados são armazenados e manipulados utilizando diversas estruturas de dados clássicas, conforme os critérios propostos.

O objetivo do projeto é demonstrar, na prática, a aplicação de estruturas de dados aprendidas em aula no contexto de um sistema funcional.

---

## ▶️ Requisitos para Execução

### 1. Pré-requisitos

* Python 3.10 ou superior instalado no sistema

### 2. Como executar o sistema

1. Clone este repositório ou baixe o arquivo `.py` com o código.

2. Execute o terminal ou prompt de comando.

3. Navegue até o diretório onde está salvo o arquivo do sistema:

```bash
cd caminho/do/arquivo
```

4. Execute o sistema com o comando:

```bash
python nome_do_arquivo.py
```

Não há bibliotecas externas necessárias; todo o código utiliza apenas a biblioteca padrão do Python.

---

## ⚙️ Funcionalidades do Sistema

### 1. Cadastro de clientes

* Nome e CPF únicos
* Relacionamento com múltiplas contas bancárias

### 2. Criação de contas bancárias

* Geração automática de número de conta
* Conta associada a um cliente já cadastrado

### 3. Operações bancárias

* Depósito e saque com atualização de saldo
* Histórico individual de transações por conta
* Desfazer da última transação (pilha global)

### 4. Histórico de transações

* Cada conta possui seu próprio histórico usando lista encadeada

---

## 📚 Estruturas de Dados Utilizadas e Justificativas

### 1. **Listas**

* Utilizadas para armazenar a lista geral de clientes e contas.
* Justificativa: Estrutura simples e eficiente para acesso sequencial e armazenamento dinâmico.

### 2. **Pilha (com lista)**

* Utilizada para registrar as transações recentes e permitir desfazer a última.
* Justificativa: Ideal para controle de operações reversíveis (último a entrar, primeiro a sair - LIFO).

### 3. **Tuplas**

* Armazenamento de transações como (número da conta, tipo, valor).
* Justificativa: Estrutura imutável e leve, ideal para agrupamento simples de dados.

### 4. **Sets (conjuntos)**

* Utilizados para garantir unicidade de CPFs cadastrados.
* Justificativa: Operações de verificação de existência são rápidas (O(1)).

### 5. **Dicionários**

* Mapeamento de CPF → Cliente e Conta → Dados da conta.
* Justificativa: Acesso rápido e direto aos dados usando chaves únicas.

### 6. **Lista Encadeada**

* Cada conta possui uma lista encadeada de transações.
* Justificativa: Permite inserção eficiente no início, sem necessidade de realocação de memória.

---

## 🧪 Exemplos de Uso

### Criar um cliente e uma conta:

```
1. Cadastrar cliente
2. Criar conta
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

---

## ✅ Considerações Finais

O sistema demonstra a integração entre estruturas de dados fundamentais e um problema do mundo real (gestão bancária), promovendo aprendizado prático e aplicável. Todas as estruturas exigidas foram utilizadas de forma proposital para reforçar os conceitos teóricos vistos em aula.
