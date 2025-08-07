# Instruções para o Dashboard no Power BI

Este documento detalha os passos necessários para importar os dados gerados pelo projeto Python `black-scholes-risk-app` no Power BI, realizar as transformações necessárias e configurar o modelo de dados e as medidas DAX para criar um dashboard de análise de risco de opções.

## 1. Importando os Dados no Power BI

O projeto Python gera um arquivo CSV (`PETR4_options_data.csv`) na pasta `data/exports/` que contém todos os dados processados, incluindo preços de ações, preços de opções (call e put) e as Gregas. Siga os passos abaixo para importar este arquivo no Power BI Desktop:

1.  **Abra o Power BI Desktop.**
2.  Na faixa de opções `Página Inicial`, clique em `Obter Dados`.
3.  Na janela `Obter Dados`, selecione `Texto/CSV` e clique em `Conectar`.
4.  Navegue até a pasta `black-scholes-risk-app/data/exports/` do seu projeto e selecione o arquivo `PETR4_options_data.csv`. Clique em `Abrir`.
5.  Uma janela de visualização dos dados será exibida. Verifique se o delimitador está correto (geralmente vírgula) e se os dados estão sendo exibidos corretamente. Clique em `Transformar Dados` para abrir o Power Query Editor.

## 2. Transformações no Power Query Editor (Linguagem M)

No Power Query Editor, é crucial garantir que os tipos de dados estejam corretos e que quaisquer transformações necessárias sejam aplicadas. A linguagem M é usada para essas transformações. Abaixo estão as transformações recomendadas:

1.  **Renomear a Tabela:** No painel `Configurações de Consulta` (à direita), em `Nome`, renomeie a tabela de `PETR4_options_data` para `options_data` (ou um nome de sua preferência).

2.  **Verificar Tipos de Dados:** Percorra todas as colunas e certifique-se de que o tipo de dado esteja correto. As colunas de data devem ser do tipo `Data`, as colunas numéricas (preços, gregas, taxas, volatilidade) devem ser do tipo `Número Decimal`.
    *   `Date`: `Data`
    *   `Stock_Price`: `Número Decimal`
    *   `Strike_Price`: `Número Decimal`
    *   `Time_to_Maturity_Years`: `Número Decimal`
    *   `Risk_Free_Rate`: `Número Decimal`
    *   `Volatility`: `Número Decimal`
    *   `Call_Price`: `Número Decimal`
    *   `Put_Price`: `Número Decimal`
    *   `Delta_Call`: `Número Decimal`
    *   `Delta_Put`: `Número Decimal`
    *   `Gamma`: `Número Decimal`
    *   `Vega`: `Número Decimal`
    *   `Theta_Call`: `Número Decimal`
    *   `Theta_Put`: `Número Decimal`
    *   `Rho_Call`: `Número Decimal`
    *   `Rho_Put`: `Número Decimal`

    Para alterar o tipo de dado, clique no ícone ao lado do nome da coluna e selecione o tipo apropriado.

3.  **Aplicar Alterações:** Após verificar e ajustar os tipos de dados, clique em `Fechar e Aplicar` na faixa de opções `Página Inicial` para carregar os dados no modelo do Power BI.

## 3. Modelo de Dados

Para este projeto, o modelo de dados será simples, consistindo em uma única tabela `options_data`. No entanto, é uma boa prática garantir que as colunas de data sejam marcadas como `Tabela de Data` se você planeja usar funções de inteligência de tempo no DAX.

1.  **Visualização de Modelo:** No Power BI Desktop, clique no ícone `Modelo` (o terceiro ícone na barra lateral esquerda) para ver a visualização do modelo.
2.  **Marcar como Tabela de Data (Opcional, mas Recomendado):** Se você planeja usar funções de inteligência de tempo (como `TOTALYTD`, `SAMEPERIODLASTYEAR`), clique na tabela `options_data`, vá para a guia `Ferramentas de Tabela` na faixa de opções, clique em `Marcar como Tabela de Data` e selecione a coluna `Date` como a coluna de data.

## 4. Criando Medidas DAX

As medidas DAX (Data Analysis Expressions) permitem criar cálculos dinâmicos que podem ser usados em seus relatórios. O arquivo `dax_measures.txt` que você criou contém várias medidas úteis. Siga os passos para adicioná-las ao seu modelo:

1.  **Abra o arquivo `dax_measures.txt`** que você gerou.
2.  No Power BI Desktop, na visualização `Relatório` ou `Dados`, selecione a tabela `options_data` no painel `Campos`.
3.  Clique com o botão direito na tabela `options_data` e selecione `Nova Medida`.
4.  Copie e cole o código DAX para cada medida do arquivo `dax_measures.txt` para a barra de fórmulas do Power BI. Pressione Enter para confirmar a medida.
5.  Repita este processo para todas as medidas listadas no arquivo `dax_measures.txt`.

**Exemplo de Medida DAX:**

```dax
Avg Stock Price = AVERAGE(
    'options_data'[Stock_Price]
)
```

## 5. Construindo o Dashboard

Com os dados importados e as medidas DAX criadas, você pode começar a construir seu dashboard. Aqui estão algumas sugestões de visualizações:

*   **Gráfico de Linhas:** Para visualizar a evolução do `Stock_Price`, `Call_Price` e `Put_Price` ao longo do tempo (`Date`).
*   **Gráfico de Linhas:** Para visualizar a evolução das Gregas (`Delta_Call`, `Delta_Put`, `Gamma`, `Vega`, `Theta_Call`, `Theta_Put`, `Rho_Call`, `Rho_Put`) ao longo do tempo.
*   **Cartões:** Para exibir os valores médios das Gregas e dos preços das opções (usando as medidas DAX criadas).
*   **Segmentação de Dados (Slicer):** Para filtrar os dados por `Date` ou outros parâmetros se você adicionar mais dimensões.

Lembre-se de que a criatividade é fundamental na criação de dashboards. Explore os diferentes tipos de visuais e as opções de formatação para criar um relatório claro e informativo.

## 6. Exportando Imagens do Dashboard (para o README)

Após criar seu dashboard no Power BI, você pode exportar imagens para incluir no `README.md` do seu projeto. Use a funcionalidade de captura de tela do seu sistema operacional ou a opção de `Exportar` -> `Relatório para PDF` no Power BI e, em seguida, extraia as imagens relevantes. Salve essas imagens na pasta `black-scholes-risk-app/powerbi/images/`.

Com estas instruções, você terá um guia completo para configurar e visualizar os dados de análise de risco de opções no Power BI, complementando o projeto Python.

