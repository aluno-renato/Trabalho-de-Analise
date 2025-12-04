import random
import time

# ===============================================================
#  ALGORITMO 1: GULOSO POR RAZÃO VALOR/PESO (GREEDY)
# ===============================================================

def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    items = list(range(n))

    # ordena itens por razão valor/peso
    items.sort(key=lambda i: values[i] / weights[i], reverse=True)

    total_value = 0
    total_weight = 0
    chosen = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            chosen.append(i)
            total_weight += weights[i]
            total_value += values[i]

    return total_value, total_weight, chosen



# ===============================================================
#  ALGORITMO 2: PROGRAMAÇÃO DINÂMICA PARA KNAPSACK 0/1
# ===============================================================

def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    # Construção da tabela DP
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Recuperação dos itens usados
    chosen = []
    w = capacity
    total_value = dp[n][capacity]
    total_weight = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(i-1)
            w -= weights[i-1]
            total_weight += weights[i-1]

    return total_value, total_weight, chosen



# ===============================================================
#  GERAÇÃO DE INSTÂNCIA GRANDE (100 itens)
# ===============================================================

def gerar_instancia(n_itens=100):
    weights = [random.randint(1, 50) for _ in range(n_itens)]
    values  = [random.randint(10, 300) for _ in range(n_itens)]
    capacity = int(sum(weights) * 0.3)  # 30% do peso total → problema difícil

    return weights, values, capacity



# ===============================================================
#  TESTE E COMPARAÇÃO ENTRE OS DOIS ALGORITMOS
# ===============================================================

if __name__ == "__main__":
    # Gerando exemplo difícil
    weights, values, capacity = gerar_instancia(100)

    print("=======================================================")
    print("        INSTÂNCIA GERADA")
    print("=======================================================")
    print(f"Total de itens: {len(weights)}")
    print(f"Capacidade da mochila: {capacity}")
    print()

    # Execução Greedy com tempo
    t0 = time.perf_counter()
    greedy_value, greedy_weight, greedy_items = knapsack_greedy(weights, values, capacity)
    t1 = time.perf_counter()
    greedy_time = t1 - t0

    # Execução DP com tempo
    t0 = time.perf_counter()
    dp_value, dp_weight, dp_items = knapsack_dp(weights, values, capacity)
    t1 = time.perf_counter()
    dp_time = t1 - t0

    print("=======================================================")
    print("        COMPARAÇÃO: GREEDY vs PROGRAMAÇÃO DINÂMICA")
    print("=======================================================")

    print("\n--- RESULTADO GREEDY (razão valor/peso) ---")
    print("Valor total :", greedy_value)
    print("Peso total  :", greedy_weight)
    print("Itens escolhidos:", len(greedy_items))
    print(f"Tempo: {greedy_time:.6f} segundos")

    print("\n--- RESULTADO DP (exato) ---")
    print("Valor total :", dp_value)
    print("Peso total  :", dp_weight)
    print("Itens escolhidos:", len(dp_items))
    print(f"Tempo: {dp_time:.6f} segundos")

    # Comparação percentual
    diff = ((dp_value - greedy_value) / dp_value) * 100
    print("\n--- DESEMPENHO RELATIVO ---")
    print(f"Greedy atingiu {100 - diff:.2f}% do valor ideal (DP)")
