# Resumo do Modelo Black-Scholes para Precificação de Opções

## Introdução

O modelo de Black-Scholes é uma das ferramentas mais fundamentais e amplamente utilizadas no mercado financeiro para precificar opções de estilo europeu. Desenvolvido por Fischer Black, Myron Scholes e Robert Merton (que estendeu o modelo), ele fornece uma estrutura matemática para estimar o preço justo de uma opção, considerando diversos fatores de mercado.

## Premissas do Modelo

Para que o modelo de Black-Scholes seja aplicável, algumas premissas são necessárias:

*   **Ativo Subjacente:** O preço do ativo subjacente segue um movimento browniano geométrico (log-normalmente distribuído).
*   **Volatilidade:** A volatilidade do ativo subjacente é constante e conhecida.
*   **Taxa de Juros:** A taxa de juros livre de risco é constante e conhecida.
*   **Dividendos:** O ativo subjacente não paga dividendos durante a vida da opção (ou dividendos contínuos e conhecidos).
*   **Opções Europeias:** As opções só podem ser exercidas na data de vencimento.
*   **Mercado Eficiente:** Não há custos de transação, impostos, e é possível operar vendido (short selling) sem restrições.
*   **Liquidez:** O mercado é perfeitamente líquido.

## Fatores de Entrada

O modelo de Black-Scholes utiliza os seguintes parâmetros para calcular o preço de uma opção:

1.  **S (Preço Atual do Ativo Subjacente):** O preço de mercado atual do ativo que a opção representa.
2.  **K (Preço de Exercício / Strike Price):** O preço pelo qual o titular da opção pode comprar (call) ou vender (put) o ativo subjacente.
3.  **T (Tempo até o Vencimento):** O tempo restante até a data de expiração da opção, expresso em anos.
4.  **r (Taxa de Juros Livre de Risco):** A taxa de juros anualizada de um investimento sem risco (ex: títulos do governo), usada para descontar fluxos de caixa futuros.
5.  **σ (Volatilidade):** Uma medida da magnitude das flutuações de preço do ativo subjacente. É o desvio padrão anualizado dos retornos logarítmicos do ativo.

## Fórmulas Principais

As fórmulas para o preço de uma opção de compra (Call) e de venda (Put) são:

### Preço da Opção de Compra (Call Option)

$C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)$

### Preço da Opção de Venda (Put Option)

$P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$

Onde:

*   $N(x)$ é a função de distribuição acumulada normal padrão.
*   $e$ é a base do logaritmo natural.

E $d_1$ e $d_2$ são calculados como:

$d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}$

$d_2 = d_1 - \sigma\sqrt{T}$

## As Gregas (Greeks)

As 


Gregas são medidas de sensibilidade do preço de uma opção em relação a mudanças nos parâmetros de entrada. Elas são cruciais para a gestão de risco e estratégias de hedge.

*   **Delta (Δ):** Mede a sensibilidade do preço da opção em relação a uma mudança no preço do ativo subjacente. Um Delta de 0.5 significa que, para cada R$1 de aumento no preço do ativo, o preço da opção aumenta R$0.50.

    *   **Call:** $N(d_1)$
    *   **Put:** $N(d_1) - 1$

*   **Gamma (Γ):** Mede a sensibilidade do Delta em relação a uma mudança no preço do ativo subjacente. É a segunda derivada do preço da opção em relação ao preço do ativo. Um Gamma alto indica que o Delta da opção mudará rapidamente.

    *   **Call/Put:** $\frac{N'(d_1)}{S \sigma \sqrt{T}}$

*   **Vega (ν):** Mede a sensibilidade do preço da opção em relação a uma mudança na volatilidade do ativo subjacente. Um Vega alto significa que o preço da opção é muito sensível a mudanças na volatilidade.

    *   **Call/Put:** $S \cdot N'(d_1) \cdot \sqrt{T}$

*   **Theta (Θ):** Mede a sensibilidade do preço da opção em relação à passagem do tempo (decaimento temporal). Geralmente é negativo para opções longas, indicando que o valor da opção diminui à medida que o tempo se aproxima do vencimento.

    *   **Call:** $-\frac{S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2)$
    *   **Put:** $-\frac{S \cdot N'(d_1) \cdot \sigma}{2\sqrt{T}} + r K e^{-rT} N(-d_2)$

*   **Rho (ρ):** Mede a sensibilidade do preço da opção em relação a uma mudança na taxa de juros livre de risco.

    *   **Call:** $K T e^{-rT} N(d_2)$
    *   **Put:** $-K T e^{-rT} N(-d_2)$

## Conclusão

O modelo de Black-Scholes, apesar de suas premissas simplificadoras, continua sendo uma ferramenta poderosa para a precificação de opções e para a compreensão dos fatores que influenciam seu valor. As Gregas, derivadas do modelo, são essenciais para a gestão de risco e para a construção de estratégias de investimento e hedge no mercado de derivativos. Este projeto visa demonstrar a aplicação prática desses conceitos em Python, com a visualização dos resultados no Power BI, oferecendo uma base sólida para estudos em análise de risco quantitativa.


