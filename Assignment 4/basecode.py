import pandas as pd
import yfinance as yfin

def main():
    # Downloading data
    df = yfin.download("^FVX", start="2000-02-01", end="2024-01-31")

    # Fixing multi-index issue (flatten columns)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Ensuring column selection exists 
    if 'Adj Close' in df.columns:
        df = df[['Adj Close']].rename(columns={'Adj Close': 'FVX_Close'})
    elif 'Close' in df.columns:
        df = df[['Close']].rename(columns={'Close': 'FVX_Close'})
    else:
        raise ValueError("Neither 'Adj Close' nor 'Close' columns found in the dataset.")

    # Checking missing values before cleaning
    print("Missing values before cleaning:\n", df.isnull().sum())

    # Eliminating NaN values
    df.dropna(inplace=True)

    # Ensure all values are numerical (eliminate potential non-numeric entries)
    df = df[pd.to_numeric(df['FVX_Close'], errors='coerce').notna()]

    # Save cleaned data to CSV
    csv_filename = "FVX_data_cleaned.csv"
    df.to_csv(csv_filename, index=True)

    print(f"\nCleaned data saved as {csv_filename}")
    print("\nFirst 5 rows of cleaned data:\n", df.head())

if __name__ == "__main__":
    main()
