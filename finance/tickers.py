import yfinance as yf

def get_company_info(ticker_symbol):
    try:
        company = yf.Ticker(ticker_symbol)
        company_name = company.info['longName']
        sector = company.info['sector']
        return company_name, sector
    except Exception as e:
        return None, None

def sector(ticker_symbol):
    try:
        company_name, sector_name = get_company_info(ticker_symbol) 
        return sector_name  
    except Exception as e:
        return ''

