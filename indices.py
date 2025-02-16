import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def load_data(file_path):
    """Loads the S&P 500 historical data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """Cleans and processes the S&P 500 dataset."""
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

    # Convert numerical columns to float (removing commas)
    numerics = ["Price", "Open", "High", "Low"]
    df[numerics] = df[numerics].replace(",", "", regex=True).astype(float)

    # Convert 'Change %' to float after removing the percentage sign
    df["Change %"] = df["Change %"].str.replace("%", "", regex=True).astype(float)

    # Sort data in ascending order (older dates first)
    df = df.sort_values("Date")

    return df

def plot_data(df):
    """Plots the S&P 500 closing prices."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Price"], label="S&P 500 Price", color="blue")

    # Formatting
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("S&P 500 Historical Closing Prices")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

def check_stationarity(df):
    """Performs Augmented Dickey-Fuller (ADF) test for stationarity."""
    result = adfuller(df["Price"])
    print("ADF Test Results:")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    print("Stationary" if result[1] < 0.05 else "Non-Stationary")

def plot_acf_pacf(df):
    """Plots ACF and PACF for time series analysis."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    plot_acf(df["Price"], ax=axes[0], lags=40)
    axes[0].set_title("Autocorrelation (ACF)")

    plot_pacf(df["Price"], ax=axes[1], lags=40)
    axes[1].set_title("Partial Autocorrelation (PACF)")

    plt.show()

def rolling_statistics(df):
    """Plots rolling mean and standard deviation to assess volatility."""
    df["Rolling_Mean"] = df["Price"].rolling(window=30).mean()
    df["Rolling_Std"] = df["Price"].rolling(window=30).std()

    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Price"], label="Original Price", color="blue", alpha=0.6)
    plt.plot(df["Date"], df["Rolling_Mean"], label="30-Day Rolling Mean", color="red")
    plt.plot(df["Date"], df["Rolling_Std"], label="30-Day Rolling Std Dev", color="green")

    plt.title("Rolling Statistics of S&P 500 Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

def decompose_time_series(df):
    """Performs time series decomposition (trend, seasonality, residuals)."""
    df.set_index("Date", inplace=True)
    decomposition = sm.tsa.seasonal_decompose(df["Price"], model="additive", period=30)

    fig, axes = plt.subplots(4, 1, figsize=(12, 8))
    decomposition.observed.plot(ax=axes[0], title="Observed")
    decomposition.trend.plot(ax=axes[1], title="Trend")
    decomposition.seasonal.plot(ax=axes[2], title="Seasonality")
    decomposition.resid.plot(ax=axes[3], title="Residuals")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = r"C:\Users\BRAILER\Downloads\S&P 500 Historical Data.csv"

    # Load and clean the data
    df = load_data(file_path)
    df = clean_data(df)
    plot_data(df)

    # Time Series Analysis
    check_stationarity(df)  # ADF test
    plot_acf_pacf(df)  # Autocorrelation and Partial Autocorrelation
    rolling_statistics(df)  # Rolling mean and standard deviation
    decompose_time_series(df)  # STL decomposition
