import os
import sys
import asyncio
import requests
import feedparser
import pandas as pd
from utilities.linkNews import NewsLink

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from utilities.linkNews import NewsLink

class NewsFetcher:
    def __init__(self, query=None):
        self.news_stories = []
        self.hl = "en-US"
        self.gl = "US"
        self.ceid = "US:en"

        if query:
            self.fetch_news_stories(query, num_stories=20)  # Default to 20 stories

    async def fetch_news_stories(self, query, num_stories=20, timeframe=None):
        base_url = "https://news.google.com/rss/search"
        params = {
            "q": query,
            "hl": self.hl,
            "gl": self.gl,
            "ceid": self.ceid,
        }

        if timeframe:
            params["tbs"] = f"qdr:{timeframe}"

        try:
            response = await asyncio.to_thread(requests.get, base_url, params=params)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
        except (requests.RequestException, feedparser.FeedParserError) as e:
            print(f"Error fetching news stories: {e}")
            self.news_stories = []
            return

        self.news_stories = []
        tasks = [self.fetch_og_url(entry.link) for entry in feed.entries[:num_stories]]
        og_urls = await asyncio.gather(*tasks)

        for idx, entry in enumerate(feed.entries[:num_stories]):
            title = entry.title
            og_link = og_urls[idx]
            news_link = NewsLink(title, og_link)
            self.news_stories.append(news_link)

    async def fetch_og_url(self, url):
        try:
            response = await asyncio.to_thread(requests.head, url, allow_redirects=True)
            response.raise_for_status()
            return response.url
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None

    def to_dataframe(self):
        data = {
            "Title": [story.title for story in self.news_stories],
            "Link": [story.link for story in self.news_stories],
        }
        return pd.DataFrame(data)

    def urls(self):
        return [story._link for story in self.news_stories]

    def set_host_language(self, hl):
        self.hl = hl

    def set_geo_location(self, gl):
        self.gl = gl

    def set_content_edition(self, ceid):
        self.ceid = ceid

    def search(self, query, num_stories=20, timeframe=None):
        asyncio.run(self.fetch_news_stories(query, num_stories, timeframe))

    def __str__(self):
        if not self.news_stories:
            return "No news stories found."

        result = ""
        for idx, story in enumerate(self.news_stories, start=1):
            result += f"Story {idx}:\n"
            result += f"Title: {story.title}\n"
            result += f"Link: {story.link}\n"
            result += "\n"

        return result

