import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preparing_ar2_data(log_returns):
    """
    Creating base for the AR(2) model
    """
    r = log_returns.values
    n = len(r)

    # Base X & y
    X, y = [], []
    for t in range(2, n):
        X.append([1, r[t-1], r[t-2]]) 
        y.append(r[t])

    X = np.array(X)
    y = np.array(y)
    return X, y

