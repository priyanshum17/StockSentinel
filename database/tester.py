import os
import sys
import sqlite3
import yfinance as yf

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from finance.tickers import sector as get_sector

def market_cap(ticker):
    stock = yf.Ticker(ticker)
    return stock.info['marketCap']

def similar_stocks(sector, exclude_ticker):
    connection = sqlite3.connect('/Users/priyanshumehta/StockSentinel/stock_data.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT symbol FROM NYSEInfo WHERE sector = ? AND symbol != ? ORDER BY market_cap DESC", (sector, exclude_ticker))
    tickers = cursor.fetchall()

    connection.close()

    return [ticker[0] for ticker in tickers[:5]]  # Return only the top 5 tickers

if __name__ == "__main__":
    ticker_symbol = 'AAPL'
    sector = get_sector(ticker_symbol)
    print(f"Sector for '{ticker_symbol}': {sector}")

    sorted_tickers = similar_stocks(sector, ticker_symbol)
    print(f"Top 5 tickers in sector '{sector}' sorted by market cap: {sorted_tickers}")
