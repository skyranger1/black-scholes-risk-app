
# black-scholes-risk-app

Este projeto é uma calculadora de preço teórico de opções (call e put) usando o modelo Black-Scholes, com simulação de preços históricos, cálculo das gregas (Delta, Gamma, Vega etc) e visualização dos dados no Power BI. Foi desenvolvido como um pet project para o portfólio de João Gabriel Araujo

## Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/black-scholes-risk-app.git
    cd black-scholes-risk-app
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o notebook de simulação:**
    Abra o Jupyter Notebook na raiz do projeto e execute o `backtest.ipynb`.
    ```bash
    jupyter notebook
    ```
    O notebook irá baixar os dados, processá-los e gerar o arquivo `PETR4_options_data.csv` na pasta `data/exports/`.

## Como Importar no Power BI

1.  Abra o Power BI Desktop.
2.  Clique em `Obter Dados` -> `Texto/CSV`.
3.  Navegue até a pasta `data/exports/` e selecione o arquivo `PETR4_options_data.csv`.
4.  No Power Query Editor, revise os tipos de dados e aplique quaisquer transformações necessárias (ex: converter colunas de data para o tipo Data).
5.  Carregue os dados para o modelo.
6.  Crie suas visualizações e relatórios.

## Como Customizar os Parâmetros

Os principais parâmetros para customização estão no arquivo `src/simulator.py` e no notebook `notebooks/backtest.ipynb`:

-   **`ticker`**: Símbolo do ativo (ex: `PETR4.SA`, `VALE3.SA`).
-   **`start_date` / `end_date`**: Período para baixar os dados históricos.
-   **`r` (taxa de juros)**: Taxa de juros livre de risco anualizada (default: 0.11 para Selic anual).
-   **`maturity_days`**: Número de dias até o vencimento da opção (default: 90 dias).
-   **`K` (strike price)**: Atualmente definido como `preço atual + 5%` no `simulator.py`. Pode ser ajustado para um valor fixo ou outra lógica.

## Prints do Dashboard Final

(Adicionar prints do dashboard do Power BI aqui, após a criação do dashboard.)

