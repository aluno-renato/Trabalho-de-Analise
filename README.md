# 🧠 Problema da Mochila 0/1 — Análise Comparativa de Algoritmos

**Trabalho de Análise de Algoritmos - Complexidade Computacional**

Este repositório apresenta a implementação e análise comparativa de dois algoritmos para o **Problema da Mochila 0/1 (0/1 Knapsack Problem)**, um problema clássico **NP-Difícil**:

1. **Algoritmo Guloso (Greedy)** — Heurística aproximativa por razão valor/peso
2. **Programação Dinâmica (DP)** — Solução exata (baseline para comparação)

---

## 📋 Sumário

- [Sobre o Problema](#-sobre-o-problema-da-mochila-01)
- [Algoritmos Implementados](#-algoritmos-implementados)
- [Como Executar](#-como-executar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Métricas e Análise](#-métricas-e-análise)
- [Resultados Esperados](#-resultados-esperados)
- [Requisitos](#-requisitos)

---

## 📌 Sobre o Problema da Mochila 0/1

O **Problema da Mochila 0/1** é um problema clássico de otimização combinatória classificado como **NP-Difícil**.

**Definição formal:**
- Dado um conjunto de `n` itens, onde cada item `i` possui:
  - `valor[i]`: valor associado
  - `peso[i]`: peso associado
- Uma mochila com capacidade máxima `W`
- **Objetivo:** Selecionar um subconjunto de itens que maximize o valor total sem exceder a capacidade `W`
- **Restrição:** Cada item pode ser incluído **no máximo uma vez** (0 ou 1)

**Relevância:**
- Pertence à classe **NP-Difícil** (versão de otimização do problema de decisão NP-Completo)
- Sem algoritmo polinomial conhecido que garanta solução ótima
- Amplamente usado em logística, alocação de recursos, finanças

---

## 🚀 Algoritmos Implementados

### 🔶 1. Algoritmo Guloso (Greedy) — Heurística Aproximativa

**Estratégia:** Ordena itens pela razão valor/peso (eficiência) e seleciona itens em ordem decrescente até preencher a capacidade.

**Complexidade de Tempo:** `O(n log n)`
- Ordenação: `O(n log n)`
- Seleção: `O(n)`
- Dominante: `O(n log n)`

**Vantagens:**
- ✅ Muito rápido
- ✅ Simples de implementar
- ✅ Uso eficiente de memória: `O(n)`

**Desvantagens:**
- ❌ Não garante solução ótima
- ❌ Sem fator de aproximação teórico garantido
- ❌ Pode ser arbitrariamente ruim em casos específicos

---

### 🔷 2. Programação Dinâmica (DP) — Solução Exata (Baseline)

**Estratégia:** Constrói tabela `dp[i][w]` onde cada célula representa o valor máximo possível usando os primeiros `i` itens com capacidade `w`.

**Complexidade de Tempo:** `O(n · W)`
- `n` = número de itens
- `W` = capacidade da mochila
- Pseudopolinomial (depende do valor numérico de `W`)

**Complexidade de Espaço:** `O(n · W)`

**Vantagens:**
- ✅ Garante solução ótima
- ✅ Determinístico

**Desvantagens:**
- ❌ Inviável para instâncias grandes (cresce com `W`)
- ❌ Alto uso de memória
- ❌ Não é verdadeiramente polinomial (pseudopolinomial)

**Uso neste projeto:** Serve como **baseline** para calcular o **fator de aproximação** do algoritmo Greedy.

---

## 🖥️ Como Executar

### Pré-requisitos

```bash
Python 3.7+
```

### Instalação

```bash
git clone https://github.com/aluno-renato/Trabalho-de-Analise.git
cd Trabalho-de-Analise
```

### Execução

```bash
python algoritmos.py
```

### Saída

O programa executa experimentos com **4 tamanhos diferentes** de instâncias (50, 100, 200, 500 itens) e exibe:

1. **Resultados detalhados** por experimento:
   - Valor total obtido (Greedy vs DP)
   - Peso total utilizado
   - Número de itens selecionados
   - Tempo de execução
   - Fator de aproximação (ρ)
   - Gap de otimalidade (%)

2. **Resumo comparativo** de todos os experimentos

3. **Exportação automática** para `resultados_experimentos.csv`

---

## 📁 Estrutura do Projeto

```
Trabalho-de-Analise/
│
├── algoritmos.py              # Código principal com implementações
├── README.md                  # Este arquivo
├── resultados_experimentos.csv # Resultados exportados (gerado após execução)
└── relatorio_tecnico.pdf      # Relatório técnico com análise teórica (a criar)
```

---

## 📊 Métricas e Análise

### Fator de Aproximação (ρ)

O **fator de aproximação** mede a qualidade da solução aproximada em relação à solução ótima:

```
ρ = valor_greedy / valor_ótimo (DP)
```

- **ρ = 1.0**: Solução ótima encontrada pelo Greedy
- **ρ < 1.0**: Greedy encontrou solução subótima
- **Quanto mais próximo de 1.0**, melhor a aproximação

### Gap de Otimalidade

Diferença percentual entre o valor obtido pelo Greedy e o valor ótimo:

```
Gap (%) = ((valor_ótimo - valor_greedy) / valor_ótimo) × 100
```

### Speedup

Aceleração do algoritmo Greedy em relação ao DP:

```
Speedup = tempo_DP / tempo_Greedy
```

---

## 📈 Resultados Esperados

### Padrões Observados

1. **Tempo de Execução:**
   - Greedy é **ordens de magnitude mais rápido** que DP
   - DP cresce rapidamente com o tamanho da instância

2. **Qualidade da Solução:**
   - Greedy tipicamente atinge **70-95%** do valor ótimo
   - Não há garantia teórica (pode ser arbitrariamente ruim em casos patológicos)

3. **Escalabilidade:**
   - Greedy escala bem para instâncias grandes (n > 1000)
   - DP torna-se impraticável para `n` ou `W` grandes

---

## 🔧 Requisitos

- Python 3.7+
- Bibliotecas padrão: `random`, `time`, `csv`, `typing`

**Nenhuma biblioteca externa é necessária.**

---

## 📚 Referências

Este projeto foi desenvolvido como parte do trabalho de **Análise de Algoritmos** com foco em:
- Teoria da Complexidade (P, NP, NP-Completo, NP-Difícil)
- Algoritmos de Aproximação
- Análise Assintótica (Big-O)
- Reprodutibilidade de experimentos

---

## 👥 Autores

**Equipe:** [Renato Xavier, Rafael Ferreira, Stênio do Carmo e Thiago Rosa]

**Data:** Dezembro 2025

---

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos.

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
