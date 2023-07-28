import os
import sys
import copy

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class NewsLink:
    def __init__(self, title, link):
        self._title = title
        self._link = link

    def get_title(self):
        return self._title

    def get_link(self):
        return self._link

    def set_title(self, new_title):
        self._title = new_title

    def set_link(self, new_link):
        self._link = new_link

    # Shallow copy constructor
    def __copy__(self):
        new_copy = NewsLink(self._title, self._link)
        return new_copy

    # Deep copy constructor
    def __deepcopy__(self, memo):
        new_copy = NewsLink(copy.deepcopy(self._title, memo), copy.deepcopy(self._link, memo))
        return new_copy
    
    def __eq__(self, other):
        if not isinstance(other, NewsLink):
            return False
        return self._title == other._title and self._link == other._link
    
    def __str__(self):
        return f"Title: {self._title}\nLink: {self._link}"