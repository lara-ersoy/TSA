import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preparing_AR2_data(log_returns):
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

def estimating_AR2_ols(log_returns):
    """
    Estimating the AR(2) parameters phi0, phi1, phi2 using OLS-estimation
    """
    X, y = prepare_ar2_data(log_returns)

    # OLS formula: beta = (X^T*X)^{-1}*(X^T*y)
    beta = np.linalg.inv(X.T @ X) @ (X.T @ y)
    phi0, phi1, phi2 = beta
    return phi0, phi1, phi2

def forecasting_AR2(phi0, phi1, phi2, log_returns, steps=5):
    """
    Forecasting using AR(2) model
    """
    r_T = log_returns.iloc[-1]       # r_T
    r_T_lagged = log_returns.iloc[-2]  # r_{T-1}
    forecasts = []

    for _ in range(steps):
        r_new = phi0 + phi1*r_T + phi2*r_T_lagged
        forecasts.append(r_next)
        # Shift for next iteration
        r_T_lagged, r_T = r_T, r_new

    return np.array(forecasts)

def main():

    # Read data
    df = pd.read_csv("FVX_data.csv", index_col=0, parse_dates=True)
    df.columns = ["Price"]  

    df["log_ret"] = np.log(df["Price"] / df["Price"].shift(1))
    df.dropna(inplace=True)

    # Estimating AR(2) using OLS estimation
    phi0, phi1, phi2 = estimate_AR2_ols(df["log_ret"])
    print(f"AR(2) OLS Estimates:")
    print(f"phi0 = {phi0:.5f}, phi1 = {phi1:.5f}, phi2 = {phi2:.5f}")

    # Forecast next 5 steps
    steps_ahead = 5
    forecast_vals = forecast_ar2(phi0, phi1, phi2, df["log_ret"], steps=steps_ahead)
    print(f"\nForecasted log-returns for the next {steps_ahead} days:")
    for i, val in enumerate(forecast_vals, start=1):
        print(f"Day {i}: {val:.5f}")