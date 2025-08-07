import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def download_data(ticker: str, start_date: str, end_date: str, raw_data_path: str) -> pd.DataFrame:
    """
    Baixa dados históricos de um ticker usando yfinance e salva em CSV.

    Args:
        ticker (str): Símbolo do ativo (ex: 'PETR4.SA').
        start_date (str): Data de início no formato 'YYYY-MM-DD'.
        end_date (str): Data de fim no formato 'YYYY-MM-DD'.
        raw_data_path (str): Caminho para salvar os dados brutos.

    Returns:
        pd.DataFrame: DataFrame com os dados históricos.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    print(f"Colunas do DataFrame baixado: {data.columns}")    
    if not os.path.exists(raw_data_path):
        os.makedirs(raw_data_path)
        
    file_path = os.path.join(raw_data_path, f'{ticker.replace(".SA", "")}_raw_data.csv')
    data.to_csv(file_path)
    print(f"Dados brutos de {ticker} salvos em {file_path}")
    return data

if __name__ == "__main__":
    # Exemplo de uso
    ticker = "PETR4.SA"
    start_date = "2023-01-01"
    end_date = datetime.now().strftime('%Y-%m-%d')
    raw_path = "../data/raw"

    df_raw = download_data(ticker, start_date, end_date, raw_path)
    print(df_raw.head())


