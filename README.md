# Stock Sentinel

Stock Sentinel is a web application designed for stock market investors to gain insights into stock sentiment and news aggregation. It leverages sentiment analysis to provide users with a better understanding of market trends and news related to specific stocks.

## Features
- **Sentiment Analysis**: Utilizes the Hugging Face FinBERT API to analyze the sentiment of news articles related to a specific stock ticker symbol. This allows users to gauge market sentiment and make informed decisions.
- **Stock Information**: Provides users with basic information about the selected stock, including its sector and key financial metrics. This information helps users understand the company's position in the market.
- **Similar Stocks**: Offers a list of stocks that are similar to the selected stock. This feature helps users discover new investment opportunities and diversify their portfolio.
- **Summary**: Generates a summary of the selected stock, including its business description and key financials. This summary provides users with a comprehensive overview of the company.
- **News Stories**: Aggregates and displays the latest news stories related to the selected stock. This helps users stay updated with the latest developments and news affecting the stock.

## Technologies Used
- **Streamlit**: Used for creating the web application user interface, making it interactive and easy to use.
- **Python**: Programming language used for backend development and data analysis.
- **Hugging Face FinBERT API**: Utilized for sentiment analysis of news articles, providing accurate sentiment scores.
- **Google News API**: Used for fetching news articles related to the selected stock, ensuring the availability of up-to-date news.
- **Yahoo Finance API**: Utilized for fetching stock information and summary data, providing users with comprehensive stock information.

## Advantages
- **Real-time Insights**: Stock Sentinel provides real-time sentiment analysis and news aggregation, enabling users to make timely investment decisions.
- **Comprehensive Information**: By aggregating news stories and providing stock summaries, Stock Sentinel offers users a comprehensive view of the stock market and specific stocks.
- **Ease of Use**: With its user-friendly interface, Stock Sentinel makes it easy for users to access and understand complex stock market data.
- **Decision Support**: The sentiment analysis provided by Stock Sentinel serves as a valuable decision support tool, helping users gauge market sentiment and make informed investment decisions.

## Installation
```sh
# Clone the repository
git clone https://github.com/your-username/stock-sentinel.git

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
