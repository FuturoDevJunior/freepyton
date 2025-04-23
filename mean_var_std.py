import numpy as np


def calculate(lst):
    """
    Calcula estatísticas (média, variância, desvio padrão, máximo, mínimo e soma)
    para linhas, colunas e matriz achatada de uma matriz 3x3.

    Parâmetros:
        lst (list): Lista de 9 números (int ou float).

    Retorna:
        dict: Dicionário com as estatísticas calculadas, conforme formato:
            {
              'mean': [colunas, linhas, total],
              'variance': [colunas, linhas, total],
              'standard deviation': [colunas, linhas, total],
              'max': [colunas, linhas, total],
              'min': [colunas, linhas, total],
              'sum': [colunas, linhas, total]
            }
    Lança:
        ValueError: Se a lista não contiver exatamente 9 elementos.
    """
    # Validação da entrada
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Conversão para matriz 3x3
    arr = np.array(lst).reshape(3, 3)

    def to_pylist(x):
        """Converte array numpy para lista Python de floats ou ints."""
        return [
            float(i) if isinstance(i, (np.floating, float)) else int(i)
            for i in x
        ]

    # Cálculo das estatísticas
    calculations = {
        'mean': [
            to_pylist(np.mean(arr, axis=0)),  # Por coluna
            to_pylist(np.mean(arr, axis=1)),  # Por linha
            float(np.mean(arr))               # Total
        ],
        'variance': [
            to_pylist(np.var(arr, axis=0)),
            to_pylist(np.var(arr, axis=1)),
            float(np.var(arr))
        ],
        'standard deviation': [
            to_pylist(np.std(arr, axis=0)),
            to_pylist(np.std(arr, axis=1)),
            float(np.std(arr))
        ],
        'max': [
            to_pylist(np.max(arr, axis=0)),
            to_pylist(np.max(arr, axis=1)),
            int(np.max(arr))
        ],
        'min': [
            to_pylist(np.min(arr, axis=0)),
            to_pylist(np.min(arr, axis=1)),
            int(np.min(arr))
        ],
        'sum': [
            to_pylist(np.sum(arr, axis=0)),
            to_pylist(np.sum(arr, axis=1)),
            int(np.sum(arr))
        ]
    }
    return calculations 