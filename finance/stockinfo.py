import yfinance as yf
import requests

class Stock:
    def __init__(self, stock_symbol):
        self.stock = yf.Ticker(stock_symbol)

    def stock_info(self):
        stock_data = self.stock.info
        try:
            return {
            'Market Cap': stock_data['marketCap'],
            # 'Dividend Yield': stock_data['dividendYield'],
            'Gross Profits': stock_data['grossProfits'],
            'Volume': stock_data['averageVolume'],
            # 'Trailing PE': stock_data['trailingPE'],
            # 'Total Debt': stock_data['totalDebt'],
            # 'EBITDA': stock_data['ebitda'],
            'Revenue Per Share': stock_data['revenuePerShare'],
            'Operating Margins': stock_data['operatingMargins'],
            # 'Debt to Equity': stock_data['debtToEquity']
        }
        except Exception:
            return stock_data
        

    def about(self):
        try:
            return self.stock.info['longBusinessSummary']
        except Exception:
            return 'Summary Not Available'
    
    def raw(self):
        return self.stock.info
    
    def stock_news(self):
        try:
            return self.stock.news
        except requests.exceptions.JSONDecodeError:
            return "No news data available for this stock."

print(Stock('F').stock_info())