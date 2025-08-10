import pandas as pd
from datetime import datetime, timedelta
from typing import Literal
import os

from black_scholes import black_scholes_call, black_scholes_put
from greeks import delta_call, delta_put, gamma, vega, theta_call, theta_put, rho_call, rho_put
from data_loader import download_data
from utils import calc_annualized_volatility, get_time_to_maturity, save_to_csv

class OptionSimulator:
    def __init__(self, ticker: str, start_date: str, end_date: str, 
                 raw_data_path: str, processed_data_path: str, exports_path: str,
                 r: float = 0.08, maturity_days: int = 90):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path
        self.exports_path = exports_path
        self.r = r
        self.maturity_days = maturity_days
        self.df_raw = None
        self.df_processed = None

    def load_and_process_data(self) -> pd.DataFrame:
        print(f"Baixando dados para {self.ticker}...")
        self.df_raw = download_data(self.ticker, self.start_date, self.end_date, self.raw_data_path)
        if self.df_raw.empty:
            raise ValueError("Não foi possível baixar dados para o ticker especificado.")
        print(f"Colunas do DataFrame raw: {self.df_raw.columns}")

        self.df_raw.index = pd.to_datetime(self.df_raw.index)
        self.df_raw.sort_index(inplace=True)
        
        # Calcular volatilidade anualizada
        self.sigma = calc_annualized_volatility(self.df_raw[("Close", self.ticker)])
        print(f"Volatilidade anualizada calculada: {self.sigma:.4f}")

        processed_data = []
        for index, row in self.df_raw.iterrows():
            current_date = index.strftime("%Y-%m-%d")
            S = row[("Close", self.ticker)]
            
            # Definir strike K como preço atual + 5%
            K = S * 1.05 
            
            # Definir data de vencimento
            maturity_date = (index + timedelta(days=self.maturity_days)).strftime("%Y-%m-%d")
            T = get_time_to_maturity(current_date, maturity_date)

            if T <= 0: # Opções vencidas ou no dia do vencimento, ignorar
                continue

            # Calcular preços e gregas
            call_price = black_scholes_call(S, K, T, self.r, self.sigma)
            put_price = black_scholes_put(S, K, T, self.r, self.sigma)
            
            delta_c = delta_call(S, K, T, self.r, self.sigma)
            delta_p = delta_put(S, K, T, self.r, self.sigma)
            gamma_val = gamma(S, K, T, self.r, self.sigma)
            vega_val = vega(S, K, T, self.r, self.sigma)
            theta_c = theta_call(S, K, T, self.r, self.sigma)
            theta_p = theta_put(S, K, T, self.r, self.sigma)
            rho_c = rho_call(S, K, T, self.r, self.sigma)
            rho_p = rho_put(S, K, T, self.r, self.sigma)

            processed_data.append({
                "Date": current_date,
                "Stock_Price": S,
                "Strike_Price": K,
                "Time_to_Maturity_Years": T,
                "Risk_Free_Rate": self.r,
                "Volatility": self.sigma,
                "Call_Price": call_price,
                "Put_Price": put_price,
                "Delta_Call": delta_c,
                "Delta_Put": delta_p,
                "Gamma": gamma_val,
                "Vega": vega_val,
                "Theta_Call": theta_c,
                "Theta_Put": theta_p,
                "Rho_Call": rho_c,
                "Rho_Put": rho_p
            })
        
        self.df_processed = pd.DataFrame(processed_data)
        
        # Salvar dados processados
        processed_file_path = os.path.join(self.processed_data_path, f"{self.ticker.replace('.SA', '')}_processed_data.csv")
        save_to_csv(self.df_processed, processed_file_path)
        print(f"Dados processados salvos em {processed_file_path}")

        # Salvar dados para exportação (Power BI)
        exports_file_path = os.path.join(self.exports_path, f"{self.ticker.replace('.SA', '')}_options_data.csv")
        save_to_csv(self.df_processed, exports_file_path)
        print(f"Dados para exportação salvos em {exports_file_path}")

        return self.df_processed

if __name__ == "__main__":
    # Exemplo de uso
    ticker = "PETR4.SA"
    start_date = "2023-01-01"
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Caminhos relativos para os diretórios de dados
    base_dir = "../../data"
    raw_path = os.path.join(base_dir, "raw")
    processed_path = os.path.join(base_dir, "processed")
    exports_path = os.path.join(base_dir, "exports")

    simulator = OptionSimulator(ticker, start_date, end_date, raw_path, processed_path, exports_path)
    df_final = simulator.load_and_process_data()
    print(df_final.head())
    print(df_final.info())


