import os
import sys
from datetime import datetime
import newspaper
import requests

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from utilities.infoNews import NewsItem
from utilities.date import datetime_format

class News:
    def __init__(self, urls=[]):
        self.news_items = []
        
        for url in urls:
            if is_valid_url(url):
                title, description, unformatted_time = self.info(url)

                try:
                    time = datetime_format(unformatted_time)
                except Exception:
                    time = None

                # Only append the news item if both title and time are not None
                if description is not None and time is not None and time.strip() != '':
                    news_item = NewsItem(url, title, description, time)
                    self.news_items.append(news_item)

    def info(self, url):
        try:
            article = newspaper.Article(url)
            article.download()
            article.parse()

            title = article.title
            description = article.meta_description
            time = article.publish_date

            return title, description, str(time)

        except newspaper.ArticleException as e:
            # print(f"Error extracting information: {e}")
            return None, None, None

    def __str__(self):
        if not self.news_items:
            return "No news items available."
        else:
            result = ""
            for idx, news_item in enumerate(self.news_items, start=1):
                result += f"News {idx}:\n{news_item}\n"
            return result
    
    def sort(self):
        valid_items = [item for item in self.news_items if item._time is not None]
        sorted_items = sorted(valid_items, key=lambda x: x._time, reverse=True)
        self.news_items = sorted_items
    
    def to_dict(self, n=None):
        valid_items = [item for item in self.news_items if item._time is not None]
        sorted_items = sorted(valid_items, key=lambda x: x._time)

        if n is None or n >= len(sorted_items):
            n = len(sorted_items)

        result = []
        for item in sorted_items[-n:]:
            item_dict = {
                "title": item._title,
                "description": item._description,
                "time": item._time,
                "link": item._link
            }
            result.append(item_dict)

        return result

def is_valid_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False
