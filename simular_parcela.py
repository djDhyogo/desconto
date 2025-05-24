# Calculadora de venda com entrada, desconto e parcelamento

# Fatores de juros por quantidade de parcelas
fatores = {
    1: 1.070,
    2: 0.553,
    3: 0.381,
    4: 0.295,
    5: 0.244,
    6: 0.216,
    7: 0.192,
    8: 0.174,
    9: 0.160,
    10: 0.149,
    11: 0.140,
    12: 0.133
}

# Coleta de dados
valor_produto = float(input("Valor do produto: R$ "))
entrada = float(input("Valor da entrada: R$ "))
desconto_percentual = float(input("Percentual de desconto (%): "))

# Cálculos
valor_desconto = round(valor_produto * (desconto_percentual / 100), 2)
valor_com_desconto = round(valor_produto - valor_desconto, 2)
valor_a_financiar = round(valor_com_desconto - entrada, 2)

print(f"\nDesconto aplicado: R$ {valor_desconto:.2f} ({desconto_percentual}%)")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
print(f"Valor a financiar: R$ {valor_a_financiar:.2f}")

# Parcelamento
parcelas = int(input("Número de parcelas (1 a 12): "))
fator = fatores.get(parcelas)

if fator:
    valor_parcela = round(valor_a_financiar * fator, 2)
    print("\n--- RESUMO ---")
    print(f"Produto: R$ {valor_produto:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Com desconto: R$ {valor_com_desconto:.2f}")
    print(f"Entrada: R$ {entrada:.2f}")
    print(f"Financiado: R$ {valor_a_financiar:.2f}")
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")
else:
    print("Quantidade de parcelas inválida.")
