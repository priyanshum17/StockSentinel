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

def get_tickers_by_sector(sector, exclude_ticker):

    connection = sqlite3.connect('/Users/priyanshumehta/StockSentinel/stock_data.db')
    cursor = connection.cursor()

    if sector is None or sector.strip() == "":
        cursor.execute(f"SELECT symbol FROM NYSEInfo WHERE symbol != ? ORDER BY market_cap DESC", (exclude_ticker,))
    else:
        cursor.execute(f"SELECT symbol FROM NYSEInfo WHERE sector = ? AND symbol != ? ORDER BY market_cap DESC", (sector, exclude_ticker))
    
    tickers = cursor.fetchall()

    connection.close()

    return [ticker[0] for ticker in tickers[:5]]  # 5 tickers

def similar_stocks(ticker):
    sector = get_sector(ticker)
    return get_tickers_by_sector(sector, ticker)
