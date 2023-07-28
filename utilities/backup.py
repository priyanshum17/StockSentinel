import streamlit as st

from finance.stockinfo import Stock
from finance.tickers import get_company_info
from sources.indianews import IndiaNews
from sources.linkFetcher import NewsFetcher
from sources.newsFetcher import News

def main():
    st.title("Stock News and Sentiment Analysis")
    
    # Input text box for entering the ticker symbol
    ticker_symbol = st.sidebar.text_input("Enter Ticker Symbol:", "AAPL")
    
    # Right section for stock info
    st.sidebar.subheader("Stock Info")
    stock_info = get_stock_info(ticker_symbol)
    st.sidebar.table(stock_info)
    
    # Input section for sentiment bar
    st.sidebar.subheader("Sentiment Analysis")
    sentiment = st.sidebar.radio("Sentiment:", ("Positive", "Negative"))
    st.sidebar.write(f"Sentiment: {sentiment}")
    
    # Center section with Summary and Similar Stocks side by side
    col1, col2 = st.columns(2)

    # Summary
    with col1:
        st.subheader("Summary")
        summary = get_summary(ticker_symbol)
        max_summary_length = 500  # Set your desired character limit for the summary
        if len(summary) > max_summary_length:
            st.write(summary[:max_summary_length])
            with st.expander("Read More"):
                st.write(summary)
        else:
            st.write(summary)

    # Similar Stocks (Displayed in a table)
    with col2:
        st.subheader("Similar Stocks")
        similar_stocks_data = get_similar_stocks_data(ticker_symbol)
        table_data = {"Similar Stocks": similar_stocks_data}
        st.table(table_data)
    
    # News Stories
    st.subheader("News Stories")
    news_type = st.selectbox("News Type:", ("Latest News", "Archived News"))
    if news_type == "Latest News":
        # Simulate fetching news data for the given ticker_symbol (Latest News)
        news_data = get_latest_news_data(ticker_symbol)
        for news in news_data:
            with st.container():
                st.markdown(f"<a href='{news['link']}' style='font-size: 18px; font-weight: bold; color: white;'>{news['title']}</a>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 8px; border-radius: 10px; background-color: black; padding: 10px; color: white;'>{news['description']}</p>", unsafe_allow_html=True)

    elif news_type == "Archived News":
        # Simulate fetching news data for the given ticker_symbol (Archived News)
        archived_news_data = get_archived_news_data(ticker_symbol)
        for news in archived_news_data:
            with st.container():
                st.markdown(f"<a href='{news['link']}' style='font-size: 18px; font-weight: bold; color: white;'>{news['title']}</a>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 8px; border-radius: 10px; background-color: black; padding: 10px; color: white;'>{news['description']}</p>", unsafe_allow_html=True)

def get_latest_news_data(ticker_symbol):
    # Simulate fetching latest news data based on the ticker_symbol
    # Replace this with your own code to fetch real latest news data
    name, sector = get_company_info(ticker_symbol)
    stories = NewsFetcher()
    stories.search(name, num_stories= 25)
    urls = stories.urls()
    print(urls)
    news = News(urls=urls)
    return news.to_dict(5)
    

    return [
        {
            "title": "Latest News 1",
            "description": "Description of Latest News 1.",
            "link": "https://www.example.com/news1"
        },
        {
            "title": "Latest News 2",
            "description": "Description of Latest News 2.",
            "link": "https://www.example.com/news2"
        },
        # Add more news items as needed
    ]

def get_archived_news_data(ticker_symbol):
    # Simulate fetching archived news data based on the ticker_symbol
    # Replace this with your own code to fetch real archived news data
    name, sector = get_company_info(ticker_symbol)
    ticker_news = IndiaNews()
    return ticker_news.news(name, 5)


    return [
        {
            "title": "Archived News 1",
            "description": "Description of Archived News 1.",
            "link": "https://www.example.com/archived1"
        },
        {
            "title": "Archived News 2",
            "description": "Description of Archived News 2.",
            "link": "https://www.example.com/archived2"
        },
        # Add more news items as needed
    ]

def get_similar_stocks_data(ticker_symbol):
    # Simulate fetching similar stocks data based on the ticker_symbol
    # Replace this with your own code to fetch real similar stocks data
    return [
        "Stock A",
        "Stock B",
        "Stock C",
        "Stock D",
        "Stock E",
    ]

def get_stock_info(ticker_symbol):
    # Simulate fetching stock info based on the ticker_symbol
    # Replace this with your own code to fetch real stock info
    stock = Stock(ticker_symbol)
    return stock.stock_info()

def get_summary(ticker_symbol):
    # Simulate fetching summary based on the ticker_symbol
    # Replace this with your own code to fetch real summary
    stock = Stock(ticker_symbol)
    return stock.about()

if __name__ == "__main__":
    main()
