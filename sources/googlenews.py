import requests
from bs4 import BeautifulSoup

def get_news_headlines(search_query):
    base_url = "https://news.google.com/"
    url = f"{base_url}search?q={search_query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    news_articles = []
    for article in soup.select("article"):
        headline = article.select_one("h3").get_text()
        description_elem = article.select_one("div[jsname='sngebd']")
        description = description_elem.get_text().strip() if description_elem else "No description available"
        link = base_url + article.find("a")["href"][1:]

        news_articles.append({"headline": headline, "description": description, "link": link})

    return news_articles

if __name__ == "__main__":
    user_input = input("Enter a search query to get relevant news stories: ")
    news_articles = get_news_headlines(user_input)
    
    print("\nRelevant News Articles:")
    for index, article in enumerate(news_articles, 1):
        print(f"{index}. {article['headline']}")
        print(f"   Description: {article['description']}")
        print(f"   Link: {article['link']}\n")
