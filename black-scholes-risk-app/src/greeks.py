import math
from scipy.stats import norm
from black_scholes import d1, d2

def delta_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Delta de uma opção de compra (call).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Delta da call.
    """
    _d1 = d1(S, K, T, r, sigma)
    return norm.cdf(_d1)

def delta_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Delta de uma opção de venda (put).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Delta da put.
    """
    _d1 = d1(S, K, T, r, sigma)
    return norm.cdf(_d1) - 1

def gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Gamma de uma opção (call ou put).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Gamma.
    """
    _d1 = d1(S, K, T, r, sigma)
    return norm.pdf(_d1) / (S * sigma * math.sqrt(T))

def vega(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Vega de uma opção (call ou put).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Vega.
    """
    _d1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(_d1) * math.sqrt(T)

def theta_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Theta de uma opção de compra (call).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Theta da call.
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return (-S * norm.pdf(_d1) * sigma / (2 * math.sqrt(T))) - (r * K * math.exp(-r * T) * norm.cdf(_d2))

def theta_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Theta de uma opção de venda (put).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Theta da put.
    """
    _d1 = d1(S, K, T, r, sigma)
    _d2 = d2(S, K, T, r, sigma)
    return (-S * norm.pdf(_d1) * sigma / (2 * math.sqrt(T))) + (r * K * math.exp(-r * T) * norm.cdf(-_d2))

def rho_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Rho de uma opção de compra (call).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Rho da call.
    """
    _d2 = d2(S, K, T, r, sigma)
    return K * T * math.exp(-r * T) * norm.cdf(_d2)

def rho_put(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Calcula o Rho de uma opção de venda (put).

    Args:
        S (float): Preço atual do ativo subjacente.
        K (float): Preço de exercício da opção.
        T (float): Tempo até o vencimento (em anos).
        r (float): Taxa de juros livre de risco anualizada.
        sigma (float): Volatilidade anualizada do ativo subjacente.

    Returns:
        float: Valor do Rho da put.
    """
    _d2 = d2(S, K, T, r, sigma)
    return -K * T * math.exp(-r * T) * norm.cdf(-_d2)

if __name__ == "__main__":
    # Exemplo de uso
    S = 100  # Preço do ativo subjacente
    K = 100  # Preço de exercício
    T = 1    # Tempo até o vencimento (1 ano)
    r = 0.05 # Taxa de juros livre de risco (5%)
    sigma = 0.2 # Volatilidade (20%)

    print(f"Delta Call: {delta_call(S, K, T, r, sigma):.4f}")
    print(f"Delta Put: {delta_put(S, K, T, r, sigma):.4f}")
    print(f"Gamma: {gamma(S, K, T, r, sigma):.4f}")
    print(f"Vega: {vega(S, K, T, r, sigma):.4f}")
    print(f"Theta Call: {theta_call(S, K, T, r, sigma):.4f}")
    print(f"Theta Put: {theta_put(S, K, T, r, sigma):.4f}")
    print(f"Rho Call: {rho_call(S, K, T, r, sigma):.4f}")
    print(f"Rho Put: {rho_put(S, K, T, r, sigma):.4f}")


