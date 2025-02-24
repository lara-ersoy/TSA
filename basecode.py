import pandas as pd
import yfinance as yfin

def main():
    # Downloading data
    df = yfin.download("^FVX", start="2000-02-01", end="2024-01-31")

    # Ensuring column selection exists 
    if 'Adj Close' in df.columns:
        df = df[['Adj Close']]
    elif 'Close' in df.columns:
        df = df[['Close']]
    else:
        raise ValueError("Neither 'Adj Close' nor 'Close' columns found in the dataset.")
    
    # Printing the number of missing values
    print("Missing values before cleaning:\n", df.isnull().sum())

    # Eliminating NaN values
    df.dropna(inplace=True)

    # Save cleaned data to CSV
    csv_filename = "FVX_data.csv"
    df.to_csv(csv_filename, index=True)

    # Skipping first two lines for the header
    df_read = pd.read_csv(csv_filename, skiprows=2, index_col=0, parse_dates=True)

    print("First 5 rows of the cleaned data:\n", df_read.head())
    print(f"\nSaved to {csv_filename}")
    print(df.head())

if __name__ == "__main__":
    main()
