# Importa a biblioteca locale para formatar valores monetários
import locale

# Configura o locale para o formato brasileiro de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def calcular_percentual(faturamento_estados):
    """
    Calcula o percentual de representação de cada estado com base no faturamento mensal.
    
    Args:
    faturamento_estados (dict): Dicionário com os estados e seus respectivos valores de faturamento.

    Returns:
    dict: Dicionário com estados como chaves e seus percentuais de representação como valores.
    """
    # Calcula o faturamento total
    faturamento_total = sum(faturamento_estados.values())
    
    # Verifica se o faturamento total é zero para evitar divisão por zero
    if faturamento_total == 0:
        raise ValueError("O faturamento total não pode ser zero.")
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

def exibir_percentuais(percentuais, faturamento_estados):
    """
    Exibe o percentual de cada estado com o formato de moeda e percentual.

    Args:
    percentuais (dict): Dicionário com estados e seus percentuais de representação.
    faturamento_estados (dict): Dicionário com estados e valores de faturamento.
    """
    print("Percentual de representação de cada estado dentro do faturamento total:")
    for estado, percentual in percentuais.items():
        valor_formatado = locale.currency(faturamento_estados[estado], grouping=True)
        print(f"{estado}: {valor_formatado} representa {percentual:.2f}% do total")

# Dados de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

try:
    # Calcula os percentuais
    percentuais = calcular_percentual(faturamento_estados)
    
    # Exibe os percentuais formatados
    exibir_percentuais(percentuais, faturamento_estados)

except ValueError as e:
    print(f"Erro: {e}")
