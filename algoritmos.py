import csv
import random
import time
from typing import List, Tuple

# Seed fixa para reprodutibilidade dos experimentos
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# ===============================================================
#  ALGORITMO 1: GULOSO POR RAZÃO VALOR/PESO (GREEDY)
# ===============================================================
# COMPLEXIDADE: O(n log n)
#   - Ordenação dos itens: O(n log n)
#   - Iteração pelos itens: O(n)
#   - Complexidade dominante: O(n log n)
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
# COMPLEXIDADE: O(n * W)
#   - n = número de itens
#   - W = capacidade da mochila
#   - Dois loops aninhados: n iterações × W iterações
#   - Espaço: O(n * W) para a tabela DP
# 
# NOTA: Este é um algoritmo EXATO (não aproximativo)
#       Serve como BASELINE para avaliar a qualidade do Greedy
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
#  GERAÇÃO DE INSTÂNCIAS DE TESTE
# ===============================================================
# Gera instâncias aleatórias com seed fixa para reprodutibilidade
# A capacidade é definida como 30% do peso total para criar
# instâncias desafiadoras onde escolhas gulosas podem falhar
# ===============================================================

def gerar_instancia(n_itens=100, seed=None):
    """
    Gera uma instância aleatória do problema da mochila.
    
    Args:
        n_itens: Número de itens a gerar
        seed: Seed para geração aleatória (None usa a seed global)
    
    Returns:
        tuple: (weights, values, capacity)
    """
    if seed is not None:
        random.seed(seed)
    
    weights = [random.randint(1, 50) for _ in range(n_itens)]
    values  = [random.randint(10, 300) for _ in range(n_itens)]
    capacity = int(sum(weights) * 0.3)  # 30% do peso total → problema difícil

    return weights, values, capacity


def executar_experimento(n_itens: int, seed: int = RANDOM_SEED) -> dict:
    """
    Executa um experimento completo com ambos os algoritmos.
    
    Args:
        n_itens: Número de itens na instância
        seed: Seed para geração da instância
    
    Returns:
        dict: Resultados do experimento
    """
    weights, values, capacity = gerar_instancia(n_itens, seed)
    
    # Execução Greedy
    t0 = time.perf_counter()
    greedy_value, greedy_weight, greedy_items = knapsack_greedy(weights, values, capacity)
    greedy_time = time.perf_counter() - t0
    
    # Execução DP
    t0 = time.perf_counter()
    dp_value, dp_weight, dp_items = knapsack_dp(weights, values, capacity)
    dp_time = time.perf_counter() - t0
    
    # Cálculo do Fator de Aproximação
    # ρ = valor_obtido / valor_ótimo
    fator_aproximacao = greedy_value / dp_value if dp_value > 0 else 0
    gap_percentual = ((dp_value - greedy_value) / dp_value) * 100 if dp_value > 0 else 0
    
    return {
        'n_itens': n_itens,
        'capacidade': capacity,
        'greedy_valor': greedy_value,
        'greedy_peso': greedy_weight,
        'greedy_itens': len(greedy_items),
        'greedy_tempo': greedy_time,
        'dp_valor': dp_value,
        'dp_peso': dp_weight,
        'dp_itens': len(dp_items),
        'dp_tempo': dp_time,
        'fator_aproximacao': fator_aproximacao,
        'gap_percentual': gap_percentual
    }


def exportar_resultados(resultados: List[dict], filename: str = 'resultados.csv'):
    """
    Exporta resultados dos experimentos para arquivo CSV.
    
    Args:
        resultados: Lista de dicionários com resultados
        filename: Nome do arquivo de saída
    """
    if not resultados:
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)
    
    print(f"\n✓ Resultados exportados para '{filename}'")



# ===============================================================
#  EXPERIMENTOS COMPARATIVOS COM MÚLTIPLOS TAMANHOS
# ===============================================================

if __name__ == "__main__":
    print("="*70)
    print(" PROBLEMA DA MOCHILA 0/1: GREEDY vs PROGRAMAÇÃO DINÂMICA")
    print("="*70)
    print(f"Seed fixa para reprodutibilidade: {RANDOM_SEED}")
    print("="*70)
    print()
    
    # Tamanhos de instâncias a testar (conforme exigido na rubrica)
    tamanhos = [50, 100, 200, 500]
    resultados = []
    
    for n in tamanhos:
        print(f"\n{'='*70}")
        print(f" EXPERIMENTO: {n} ITENS")
        print(f"{'='*70}")
        
        resultado = executar_experimento(n, seed=RANDOM_SEED + n)
        resultados.append(resultado)
        
        print(f"\nCapacidade da mochila: {resultado['capacidade']}")
        print("\n{:<25} {:>20} {:>20}".format("Métrica", "GREEDY", "DP (ÓTIMO)"))
        print("-"*70)
        print("{:<25} {:>20} {:>20}".format("Valor Total", resultado['greedy_valor'], resultado['dp_valor']))
        print("{:<25} {:>20} {:>20}".format("Peso Total", resultado['greedy_peso'], resultado['dp_peso']))
        print("{:<25} {:>20} {:>20}".format("Itens Escolhidos", resultado['greedy_itens'], resultado['dp_itens']))
        print("{:<25} {:>20.6f}s {:>20.6f}s".format("Tempo de Execução", resultado['greedy_tempo'], resultado['dp_tempo']))
        print("-"*70)
        print(f"\n📊 ANÁLISE DE QUALIDADE:")
        print(f"   • Fator de Aproximação (ρ): {resultado['fator_aproximacao']:.4f}")
        print(f"   • Gap de Otimalidade: {resultado['gap_percentual']:.2f}%")
        print(f"   • Greedy atingiu {100 - resultado['gap_percentual']:.2f}% do valor ótimo")
        
        # Análise de speedup
        if resultado['dp_tempo'] > 0:
            speedup = resultado['dp_tempo'] / resultado['greedy_tempo']
            print(f"\n⚡ ANÁLISE DE TEMPO:")
            print(f"   • Speedup do Greedy: {speedup:.2f}x mais rápido que DP")
    
    # Resumo final
    print(f"\n\n{'='*70}")
    print(" RESUMO COMPARATIVO - TODOS OS EXPERIMENTOS")
    print(f"{'='*70}")
    print("\n{:<12} {:>12} {:>12} {:>15} {:>15}".format(
        "N Itens", "Greedy (s)", "DP (s)", "Gap (%)", "Fator ρ"))
    print("-"*70)
    
    for r in resultados:
        print("{:<12} {:>12.6f} {:>12.6f} {:>15.2f} {:>15.4f}".format(
            r['n_itens'], r['greedy_tempo'], r['dp_tempo'], 
            r['gap_percentual'], r['fator_aproximacao']))
    
    print("\n" + "="*70)
    print(" OBSERVAÇÕES:")
    print("="*70)
    print("• Greedy: O(n log n) - Rápido mas sem garantia de otimalidade")
    print("• DP: O(n·W) - Solução exata, usado como baseline")
    print("• Fator ρ: Quanto mais próximo de 1.0, melhor a aproximação")
    print("• Gap: Diferença percentual entre Greedy e solução ótima")
    print("="*70)
    
    # Exportar resultados para análise posterior
    exportar_resultados(resultados, 'resultados_experimentos.csv')
    
    print("\n✓ Experimentos concluídos com sucesso!")
    print("  Use os resultados exportados para gráficos no relatório.\n")
