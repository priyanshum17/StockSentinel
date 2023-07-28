import os
import sys
import copy

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class NewsItem:
    def __init__(self, link=None, title=None, description=None, time=None):
        self._link = link
        self._title = title
        self._description = description
        self._time = time

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def copy(self):
        return NewsItem(self._link, self._title, self._description, self._time)

    def deepcopy(self):
        return copy.deepcopy(self)
    
    def __eq__(self, other):
        if not isinstance(other, NewsItem):
            return False
        return (
            self._link == other._link
            and self._title == other._title
            and self._description == other._description
            and self._time == other._time
        )
    def __str__(self):
        result = f"Title: {self._title}\n"
        result += f"Link: {self._link}\n"
        result += f"Description: {self._description}\n"
        result += f"Time: {self._time}\n"
        return result