from stocksymbol import StockSymbol

api_key = 'ENTER-API-KEY'
ss = StockSymbol(api_key)

symbol_list_us = ss.get_symbol_list(market="US") 
symbol_list_spx = ss.get_symbol_list(index="SPX")
market_list = ss.market_list
index_list = ss.index_list