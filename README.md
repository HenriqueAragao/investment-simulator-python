# 🏦 Projeto: Simulador de Investimento Bancário (Renda Fixa)

Este projeto simula um sistema real de investimentos...

## 🛠️ Diferenciais Técnicos e Regras de Negócio

* **Equivalência de Juros Compostos**: O sistema utiliza a fórmula de conversão de taxa anual para mensal via regime composto:

$$taxa\_mensal = (1 + \frac{taxa\_anual}{100})^{\frac{1}{12}} - 1$$

* **Simulação de Aportes Mensais**: Implementação de laço `for`...
* **Tabela Regressiva de IR**: Aplicação automática...
* **Base de Cálculo de Imposto Real**: O cálculo do IR é realizado...

## 💻 Demonstração de Resultados

Ao final da execução, o programa gera um extrato detalhado contendo:

1. **Total Investido**: Soma de todos os aportes realizados.
2. **Lucro Bruto**: Valor total acumulado menos o capital investido.
3. **Imposto Retido**: Valor deduzido apenas sobre o rendimento.
4. **Valor Líquido Total**: Saldo final disponível para resgate.

## 🛠️ Tecnologias Utilizadas
* Python 3.x
* Markdown para Documentação

## 🚀 Como Executar
1. Clone o repositório.
2. Execute o arquivo: `python proj_bank_investment_simulator.py`
3. Insira os dados solicitados (Aporte, Taxa anual, Prazo).