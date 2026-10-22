import numpy as np

def IC(dados, z = 1.96):
    n = len(dados)
    s = np.std(dados, ddof=1)

    z = 1.96
    margem_erro = z * s / np.sqrt(n)
    return (np.mean(dados) - margem_erro,np.mean(dados) + margem_erro)