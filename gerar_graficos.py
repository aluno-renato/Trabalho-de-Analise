"""
Script para gerar gráficos comparativos dos experimentos
Problema da Mochila 0/1: Greedy vs Programação Dinâmica
"""

import csv

import matplotlib.pyplot as plt
import numpy as np

# Configuração de estilo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def carregar_dados(filename='resultados_experimentos.csv'):
    """Carrega dados do arquivo CSV"""
    dados = {
        'n_itens': [],
        'greedy_tempo': [],
        'dp_tempo': [],
        'fator_aproximacao': [],
        'gap_percentual': [],
        'speedup': []
    }
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dados['n_itens'].append(int(row['n_itens']))
            dados['greedy_tempo'].append(float(row['greedy_tempo']))
            dados['dp_tempo'].append(float(row['dp_tempo']))
            dados['fator_aproximacao'].append(float(row['fator_aproximacao']))
            dados['gap_percentual'].append(float(row['gap_percentual']))
            
            # Calcular speedup
            speedup = float(row['dp_tempo']) / float(row['greedy_tempo'])
            dados['speedup'].append(speedup)
    
    return dados

def criar_graficos(dados):
    """Cria todos os gráficos comparativos"""
    
    # ============================================================
    # GRÁFICO 1: Comparação de Tempo de Execução (Escala Log)
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(dados['n_itens'], dados['greedy_tempo'], 
            marker='o', linewidth=2, markersize=8, 
            label='Greedy O(n log n)', color='#2ecc71')
    
    ax.plot(dados['n_itens'], dados['dp_tempo'], 
            marker='s', linewidth=2, markersize=8,
            label='DP O(n·W)', color='#e74c3c')
    
    ax.set_xlabel('Número de Itens (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo de Execução (segundos)', fontsize=12, fontweight='bold')
    ax.set_title('Comparação de Tempo de Execução: Greedy vs DP\n(Escala Logarítmica)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_yscale('log')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('grafico_tempo_execucao.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico 1 salvo: grafico_tempo_execucao.png")
    plt.close()
    
    # ============================================================
    # GRÁFICO 2: Speedup do Greedy em relação ao DP
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(dados['n_itens'])))
    bars = ax.bar(range(len(dados['n_itens'])), dados['speedup'], 
                   color=colors, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Número de Itens (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Speedup (DP / Greedy)', fontsize=12, fontweight='bold')
    ax.set_title('Aceleração do Algoritmo Greedy\n(Quantas vezes mais rápido que DP)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(dados['n_itens'])))
    ax.set_xticklabels(dados['n_itens'])
    ax.grid(True, axis='y', alpha=0.3)
    
    # Adicionar valores sobre as barras
    for i, (bar, speedup) in enumerate(zip(bars, dados['speedup'])):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{speedup:.1f}x',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('grafico_speedup.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico 2 salvo: grafico_speedup.png")
    plt.close()
    
    # ============================================================
    # GRÁFICO 3: Fator de Aproximação (ρ)
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(dados['n_itens'], dados['fator_aproximacao'], 
            marker='D', linewidth=3, markersize=10,
            color='#3498db', markerfacecolor='#f39c12', 
            markeredgewidth=2, markeredgecolor='#3498db')
    
    # Linha de referência em ρ = 1.0 (ótimo)
    ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, 
               label='ρ = 1.0 (Ótimo)', alpha=0.7)
    
    ax.set_xlabel('Número de Itens (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Fator de Aproximação (ρ)', fontsize=12, fontweight='bold')
    ax.set_title('Qualidade da Solução Greedy\n(Fator de Aproximação ρ = Valor_Greedy / Valor_Ótimo)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim([0.95, 1.02])
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Adicionar anotações com os valores
    for x, y in zip(dados['n_itens'], dados['fator_aproximacao']):
        ax.annotate(f'{y:.4f}', 
                   xy=(x, y), 
                   xytext=(0, 10),
                   textcoords='offset points',
                   ha='center',
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('grafico_fator_aproximacao.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico 3 salvo: grafico_fator_aproximacao.png")
    plt.close()
    
    # ============================================================
    # GRÁFICO 4: Gap de Otimalidade (%)
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors_gap = ['#27ae60' if gap == 0 else '#e67e22' for gap in dados['gap_percentual']]
    bars = ax.bar(range(len(dados['n_itens'])), dados['gap_percentual'], 
                   color=colors_gap, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Número de Itens (n)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Gap de Otimalidade (%)', fontsize=12, fontweight='bold')
    ax.set_title('Distância da Solução Ótima\n(Gap = 0% indica solução ótima encontrada pelo Greedy)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(dados['n_itens'])))
    ax.set_xticklabels(dados['n_itens'])
    ax.grid(True, axis='y', alpha=0.3)
    
    # Adicionar valores sobre as barras
    for i, (bar, gap) in enumerate(zip(bars, dados['gap_percentual'])):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{gap:.2f}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('grafico_gap_otimalidade.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico 4 salvo: grafico_gap_otimalidade.png")
    plt.close()
    
    # ============================================================
    # GRÁFICO 5: Dashboard Completo (4 subplots)
    # ============================================================
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Subplot 1: Tempo de Execução
    ax1.plot(dados['n_itens'], dados['greedy_tempo'], 
            marker='o', linewidth=2, markersize=8, 
            label='Greedy', color='#2ecc71')
    ax1.plot(dados['n_itens'], dados['dp_tempo'], 
            marker='s', linewidth=2, markersize=8,
            label='DP', color='#e74c3c')
    ax1.set_xlabel('Número de Itens', fontweight='bold')
    ax1.set_ylabel('Tempo (s)', fontweight='bold')
    ax1.set_title('Tempo de Execução', fontsize=12, fontweight='bold')
    ax1.set_yscale('log')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Speedup
    ax2.bar(range(len(dados['n_itens'])), dados['speedup'], 
           color='#9b59b6', edgecolor='black', linewidth=1.5)
    ax2.set_xlabel('Número de Itens', fontweight='bold')
    ax2.set_ylabel('Speedup (x)', fontweight='bold')
    ax2.set_title('Aceleração do Greedy', fontsize=12, fontweight='bold')
    ax2.set_xticks(range(len(dados['n_itens'])))
    ax2.set_xticklabels(dados['n_itens'])
    ax2.grid(True, axis='y', alpha=0.3)
    
    # Subplot 3: Fator de Aproximação
    ax3.plot(dados['n_itens'], dados['fator_aproximacao'], 
            marker='D', linewidth=3, markersize=10,
            color='#3498db', markerfacecolor='#f39c12')
    ax3.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax3.set_xlabel('Número de Itens', fontweight='bold')
    ax3.set_ylabel('Fator ρ', fontweight='bold')
    ax3.set_title('Fator de Aproximação', fontsize=12, fontweight='bold')
    ax3.set_ylim([0.95, 1.02])
    ax3.grid(True, alpha=0.3)
    
    # Subplot 4: Gap de Otimalidade
    ax4.bar(range(len(dados['n_itens'])), dados['gap_percentual'], 
           color='#27ae60', edgecolor='black', linewidth=1.5)
    ax4.set_xlabel('Número de Itens', fontweight='bold')
    ax4.set_ylabel('Gap (%)', fontweight='bold')
    ax4.set_title('Gap de Otimalidade', fontsize=12, fontweight='bold')
    ax4.set_xticks(range(len(dados['n_itens'])))
    ax4.set_xticklabels(dados['n_itens'])
    ax4.grid(True, axis='y', alpha=0.3)
    
    fig.suptitle('Dashboard Comparativo: Greedy vs Programação Dinâmica\nProblema da Mochila 0/1', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    plt.tight_layout()
    plt.savefig('dashboard_completo.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico 5 salvo: dashboard_completo.png")
    plt.close()

def main():
    print("="*70)
    print(" GERAÇÃO DE GRÁFICOS COMPARATIVOS")
    print("="*70)
    print()
    
    try:
        dados = carregar_dados()
        print(f"✓ Dados carregados: {len(dados['n_itens'])} experimentos\n")
        
        print("Gerando gráficos...")
        print("-"*70)
        criar_graficos(dados)
        
        print("-"*70)
        print("\n✅ Todos os gráficos foram gerados com sucesso!")
        print("\nArquivos criados:")
        print("  1. grafico_tempo_execucao.png")
        print("  2. grafico_speedup.png")
        print("  3. grafico_fator_aproximacao.png")
        print("  4. grafico_gap_otimalidade.png")
        print("  5. dashboard_completo.png")
        print("\nUse esses gráficos no seu relatório técnico!")
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo 'resultados_experimentos.csv' não encontrado!")
        print("   Execute 'python algoritmos.py' primeiro.")
    except Exception as e:
        print(f"❌ Erro ao gerar gráficos: {e}")

if __name__ == "__main__":
    main()
