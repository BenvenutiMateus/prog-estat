import numpy as np

def neg_bin_via_geo(r,p,K):
    """
    Código para gerar uma binomial negativa através de uniforems sendo soma de geométricas.
    - r: número de sucessos
    - p: probabilidade de sucessos
    - K: número de amostras
    """
    unis = np.random.uniform(size = (K,r))
    geos = np.ceil(np.log(unis)/np.log(1-p))
    bin_neg = np.sum(geos, axis=1)
    return bin_neg

def exp(lamb = 1, M = 100_000):
    """
    Código para gerar uma amostra de exponenciais através de uniformes.
    - lamb: Parâmetro da função
    - M: Tamanho da amostra
    """
    uniformes = np.random.uniform(size=M)
    return -np.log(uniformes)/lamb