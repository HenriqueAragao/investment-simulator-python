🏦 Projeto: Simulador de Investimento Bancário (Renda Fixa)

Este projeto simula um sistema real de investimentos em Renda Fixa (como CDB ou Tesouro Direto), focado na precisão financeira exigida pelo setor bancário brasileiro.

🛠️ Diferenciais Técnicos e Regras de Negócio

Equivalência de Juros Compostos: O sistema utiliza a fórmula de conversão de taxa anual para mensal via regime composto: $taxa\_mensal = (1 + taxa\_anual / 100)^{1/12} - 1$.
Simulação de Aportes Mensais: Implementação de laço for para calcular o rendimento acumulado de depósitos recorrentes ao longo do tempo.
Tabela Regressiva de IR: Aplicação automática da alíquota de Imposto de Renda (22.5% a 15%) de acordo com o prazo do investimento.
Base de Cálculo de Imposto Real: O cálculo do IR é realizado exclusivamente sobre o Lucro Bruto (Rendimento), preservando o capital investido pelo usuário conforme a legislação vigente.

💻 Demonstração de Resultados
Ao final da execução, o programa gera um extrato detalhado contendo:
1 - Total Investido: Soma de todos os aportes realizados.

2 - Lucro Bruto: Valor total acumulado menos o capital investido.

3 - Imposto Retido: Valor deduzido apenas sobre o rendimento.

4 - Valor Líquido Total: Saldo final disponível para resgate.

