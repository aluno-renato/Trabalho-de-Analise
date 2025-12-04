# Trabalho-de-Analise
# 🧠 Problema da Mochila 0/1 — Comparação entre Greedy e Programação Dinâmica

Este repositório apresenta a implementação de dois algoritmos clássicos usados para resolver o **Problema da Mochila 0/1 (0/1 Knapsack Problem)**:

1. **Algoritmo Guloso por razão valor/peso (Greedy)**
2. **Programação Dinâmica (DP)** — solução exata

O código também realiza uma **comparação de desempenho**, medindo:
- Tempo de execução de cada algoritmo  
- Valor total obtido  
- Peso total usado  
- Número de itens escolhidos  
- Percentual do valor ótimo atingido pelo Greedy

Além disso, a instância do problema usada é **grande (100 itens)**, permitindo observar claramente as diferenças entre velocidade e qualidade de solução.

---

## 📌 Sobre o Problema da Mochila 0/1

No problema da mochila, cada item possui:
- **valor**
- **peso**

A mochila possui uma **capacidade máxima**.  
O objetivo é selecionar um conjunto de itens que maximize o valor total **sem exceder a capacidade**, e cada item pode ser usado **no máximo uma vez** (por isso é 0/1).

---

## 🚀 Algoritmos implementados

### 🔶 1. Greedy (aproximado)
O algoritmo guloso ordena os itens pela razão:

\[
\text{eficiência} = \frac{valor}{peso}
\]

E adiciona os itens mais eficientes até a mochila encher.  
É **rápido**, mas **não garante a solução ótima**.

### 🔷 2. Programação Dinâmica (exato)
O algoritmo DP monta uma tabela `dp[i][w]`, onde cada posição representa:

> o melhor valor possível usando os primeiros `i` itens com capacidade `w`.

Ele sempre encontra a **melhor solução possível**, porém com maior custo de tempo e memória.

---

## 🧪 Instância Gerada

O código gera automaticamente uma instância com:

- **100 itens**
- Pesos variando de **1 a 50**
- Valores variando de **10 a 300**
- Capacidade = **30% da soma dos pesos**

Essa escolha torna o problema **desafiante** e exige boa performance dos algoritmos.

---

## ⏱️ Medição de Tempo

Para cada algoritmo é calculado o tempo real de execução usando:

```python
time.perf_counter()
