#calcular o desconto no financiamento
import math

def calcular_valor_presente(pmt, taxa_mensal, num_parcelas):
    """Calcula o valor presente de uma anuidade com juros compostos."""
    r = taxa_mensal / 100
    n = num_parcelas
    pv = pmt * ((1 - (1 + r) ** -n) / r)
    return pv

def main():
    print("== Simulador de Desconto de Venda com Juros ==")

    # Entrada de dados
    total_pedido = float(input("Valor total do pedido: R$ "))
    entrada = float(input("Valor da entrada: R$ "))
    num_parcelas = int(input("Quantidade de parcelas: "))
    valor_parcela = float(input("Valor da parcela: R$ "))

    # Tabela de taxas (em % ao mês)
    taxas = [7.00, 6.99, 6.99, 6.97, 7.02, 7.95, 7.99, 8.00, 7.99, 8.00, 7.99, 8.04]
    taxa = taxas[num_parcelas - 1] if 1 <= num_parcelas <= 12 else taxas[-1]

    # Cálculos
    valor_financiado = total_pedido - entrada
    valor_presente = calcular_valor_presente(valor_parcela, taxa, num_parcelas)

    # Arredondamento para cima
    valor_presente = math.ceil(valor_presente * 100) / 100
    desconto = math.ceil((valor_financiado - valor_presente) * 100) / 100

    # Exibição dos resultados
    print("\n--- Resultado ---")
    print(f"Taxa aplicada: {taxa:.2f}% ao mês")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Valor presente (à vista): R$ {valor_presente:.2f}")
    print(f"Desconto por pagamento à vista: R$ {desconto:.2f}")

if __name__ == "__main__":
    main()
