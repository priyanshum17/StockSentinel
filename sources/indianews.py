import certifi
import requests
from GoogleNews import GoogleNews

# Set the path to the Certifi CA bundle
requests.utils.DEFAULT_CA_BUNDLE_PATH = certifi.where()

class IndiaNews:
    def __init__(self):
        self.googlenews = GoogleNews(lang='en')  

    def get_relevant_news(self, query):
        self.googlenews.search(query)
        news = self.googlenews.results()
        return news

    def news_info(self, query):
        news_list = self.get_relevant_news(query)
        if not news_list:
            print("No relevant news found.")
            return []
        else:
            news_info_list = []
            for news_item in news_list:
                news_info = {
                    'title': news_item['title'],
                    'description': news_item['desc'],
                    'link': news_item['link'],
                    'datetime': news_item['datetime']  
                }
                news_info_list.append(news_info)

            sorted_news_info_list = sorted(news_info_list, key=lambda x: x['datetime'], reverse=True)
            return sorted_news_info_list

    def display_top_headlines(self):
        self.googlenews.clear()
        self.googlenews.get_top_news()
        news_list = self.googlenews.results()
        if not news_list:
            print("No top headlines found.")
        else:
            print("Top headlines:\n")
            for idx, news_item in enumerate(news_list, 1):
                print(f"{idx}. {news_item['title']}")
                print(news_item['link'])
                print()

    def set_language(self, lang):
        self.googlenews.set_lang(lang)

    def news(self, query, n):
        news_info_list = self.news_info(query)
        if not news_info_list:
            print("No relevant news found.")
            return []
        else:
            if n >= len(news_info_list):
                return news_info_list
            else:
                return news_info_list[:n]
    
    def get_title(self, query):
        news = self.news_info(query)
        titles = []
        for story in news:
            titles.append(story['title'])
        
        return titles

