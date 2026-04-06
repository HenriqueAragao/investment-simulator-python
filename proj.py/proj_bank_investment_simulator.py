# Entradas principais
valor_inicial = float(input("Valor do aporte inicial: R$ "))
aporte_mensal = float(input("Valor do depósito mensal: R$ "))
taxa_anual = float(input("Taxa de juros anual (em %): "))
meses = int(input("Tempo do investimento (em meses): "))

# Convertendo taxa anual para mensal (Fórmula de equivalência)
taxa_mensal = (1 + taxa_anual / 100)**(1/12) - 1

saldo = valor_inicial
total_investido = valor_inicial

for mes in range(1, meses + 1):
    saldo = saldo * (1 + taxa_mensal) 
    saldo = saldo + aporte_mensal     
    total_investido += aporte_mensal
lucro_bruto = saldo - total_investido

# Lógica de Imposto de Renda Regressivo
dias = meses * 30
if dias <= 180:
    aliquota = 0.225  # 22.5%
elif dias <= 360:
    aliquota = 0.20   # 20%
elif dias <= 720:
    aliquota = 0.175  # 17.5%
else:
    aliquota = 0.15   # 15%
valor_imposto = (saldo - total_investido) * aliquota
saldo_liquido = saldo - valor_imposto
print(f"Imposto de Renda ({aliquota*100}%): - R$ {valor_imposto:.2f}")
print("-" * 30)
print(f"Total Investido: R$ {total_investido:.2f}")
print(f"Lucro Bruto: R$ {lucro_bruto:.2f}")
print(f"Imposto de Renda ({aliquota*100}%): - R$ {valor_imposto:.2f}")
print(f"VALOR LÍQUIDO TOTAL: R$ {saldo_liquido:.2f}")
print("-" * 30)