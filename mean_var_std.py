import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("A lista deve conter nove números")
    
    #converte a lista em matrix 3x3
    matrix = np.array(list).reshape(3, 3)
    
    #dicionario
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # média por coluna
            matrix.mean(axis=1).tolist(),   # média por linha
            matrix.mean().item()            # média total
        ],

        'variance': [
            matrix.var(axis=0).tolist(),   # variância por coluna
            matrix.var(axis=1).tolist(),   # variância por linha
            matrix.var().item()            # variância total
        ],

        'standard deviation': [
            matrix.std(axis=0).tolist(),   # desvio padrão por coluna
            matrix.std(axis=1).tolist(),   # desvio padrão por linha
            matrix.std().item()            # desvio padrão total
        ],

        'max': [
            matrix.max(axis=0).tolist(),   # máximo por coluna
            matrix.max(axis=1).tolist(),   # máximo por linha
            matrix.max().item()            # máximo total
        ],

        'min': [
            matrix.min(axis=0).tolist(),   # mínimo por coluna
            matrix.min(axis=1).tolist(),   # mínimo por linha
            matrix.min().item()            # mínimo total
        ],

        'sum': [
            matrix.sum(axis=0).tolist(),   # soma por coluna
            matrix.sum(axis=1).tolist(),   # soma por linha
            matrix.sum().item()            # soma total
        ]
    }
    
    return calculations