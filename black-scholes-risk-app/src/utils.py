import pandas as pd
import os
from datetime import datetime

def calc_annualized_volatility(prices: pd.Series) -> float:
    """
    Calcula a volatilidade anualizada a partir de uma série de preços.

    Args:
        prices (pd.Series): Série de preços do ativo.

    Returns:
        float: Volatilidade anualizada.
    """
    returns = prices.pct_change().dropna()
    daily_volatility = returns.std()
    annualized_volatility = daily_volatility * (252**0.5) # 252 dias úteis no ano
    return annualized_volatility

def get_time_to_maturity(current_date_str: str, maturity_date_str: str) -> float:
    """
    Calcula o tempo até o vencimento em anos.

    Args:
        current_date_str (str): Data atual no formato 'YYYY-MM-DD'.
        maturity_date_str (str): Data de vencimento no formato 'YYYY-MM-DD'.

    Returns:
        float: Tempo até o vencimento em anos.
    """
    current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
    maturity_date = datetime.strptime(maturity_date_str, '%Y-%m-%d')
    time_diff = (maturity_date - current_date).days
    return time_diff / 365.0

def save_to_csv(df: pd.DataFrame, path: str) -> None:
    """
    Salva um DataFrame em um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        path (str): Caminho completo para o arquivo CSV (incluindo o nome do arquivo).
    """
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_csv(path, index=False)
    print(f"DataFrame salvo em {path}")

if __name__ == "__main__":
    # Exemplo de uso
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'Price': [100, 102, 101]
    }
    df_example = pd.DataFrame(data)
    df_example.set_index('Date', inplace=True)

    vol = calc_annualized_volatility(df_example['Price'])
    print(f"Volatilidade anualizada: {vol:.4f}")

    time_to_mat = get_time_to_maturity("2023-01-01", "2024-01-01")
    print(f"Tempo até o vencimento: {time_to_mat:.2f} anos")

    output_path = "../../data/exports/example_data.csv"
    save_to_csv(df_example, output_path)


