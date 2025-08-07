import math
from scipy.stats import norm

def d1(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o parâmetro d1 da fórmula de Black-Scholes.

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor de d1.
    """
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o parâmetro d2 da fórmula de Black-Scholes.

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor de d2.
    """
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o preço de uma opção de compra (call) usando o modelo de Black-Scholes.

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Preço teórico da opção de compra.
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(_d1) - K * math.exp(-r * T) * norm.cdf(_d2)

def black_scholes_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o preço de uma opção de venda (put) usando o modelo de Black-Scholes.

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Preço teórico da opção de venda.
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return K * math.exp(-r * T) * norm.cdf(-_d2) - S * norm.cdf(-_d1)

if __name__ == "__main__":
    # Exemplo de uso
    S = 100  # Preço do ativo subjacente
    K = 100  # Preço de exercício
    T = 1    # Tempo até o vencimento (1 ano)
    r = 0.05 # Taxa de juros livre de risco (5%)
    sigma = 0.2 # Volatilidade (20%)

    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print(f"Preço da Call: {call_price:.2f}")
    print(f"Preço da Put: {put_price:.2f}")


