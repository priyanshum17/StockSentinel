import streamlit as st
from analysis import analysis 
from finance.stockinfo import Stock
from finance.tickers import get_company_info
from sources.indianews import IndiaNews
from sources.linkFetcher import NewsFetcher
from sources.newsFetcher import News
from database.similarstocks import similar_stocks

def main():
    st.title("Stock Sentinel")
 
    ticker_symbol = st.sidebar.text_input("Enter Ticker Symbol:", "AAPL")

    info = get_sentiment(ticker_symbol)
    st.sidebar.subheader(f"Sentiment: {info}")
    
    # Right section for stock info
    st.sidebar.subheader("Information")
    stock_info = get_stock_info(ticker_symbol)
    st.sidebar.table(stock_info)

    # Right section for similar stocks
    st.sidebar.subheader("Similar Stock")
    similar_stocks_data = get_similar_stocks_data(ticker_symbol)
    st.sidebar.table(similar_stocks_data)

    # Center section with Summary and Similar Stocks side by side
    st.subheader("Summary")
    summary = get_summary(ticker_symbol)
    max_summary_length = 500  
    if len(summary) > max_summary_length:
        with st.expander("Company Information"):
            st.write(summary)
    else:
        with st.expander("Company Information"):
            st.write(summary)
    

    # News Stories
    st.subheader("News Stories")
    news_type = st.selectbox("News Type:", ("Real Time News", "Latest News"))
    if news_type == "Latest News":
        news_data = get_latest_news_data(ticker_symbol)
        for news in news_data:
            with st.container():
                st.markdown(f"<a href='{news['link']}' style='font-size: 18px; font-weight: bold; color: white;'>{news['title']}</a>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 8px; border-radius: 10px; background-color: black; padding: 10px; color: white;'>{news['description']}</p>", unsafe_allow_html=True)

    elif news_type == "Real Time News":
        archived_news_data = get_archived_news_data(ticker_symbol)
        for news in archived_news_data:
            with st.container():
                st.markdown(f"<a href='{news['link']}' style='font-size: 18px; font-weight: bold; color: white;'>{news['title']}</a>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 8px; border-radius: 10px; background-color: black; padding: 10px; color: white;'>{news['description']}</p>", unsafe_allow_html=True)

def get_latest_news_data(ticker_symbol):
    name, sector = get_company_info(ticker_symbol)
    stories = NewsFetcher()
    stories.search(name, num_stories=25)
    urls = stories.urls()
    news = News(urls=urls)
    return news.to_dict(5)

def get_archived_news_data(ticker_symbol):
    name, sector = get_company_info(ticker_symbol)
    ticker_news = IndiaNews()
    return ticker_news.news(name, 5)

def get_similar_stocks_data(ticker_symbol):
    return similar_stocks(ticker_symbol)

def get_stock_info(ticker_symbol):
    stock = Stock(ticker_symbol)
    return stock.stock_info()

def get_summary(ticker_symbol):
    stock = Stock(ticker_symbol)
    return stock.about()

def get_sentiment(ticker_symbol):
    try:
        return analysis(ticker_symbol)
    except:
        return 'Undetermistic'

if __name__ == "__main__":
    main()
