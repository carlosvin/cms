import datetime

__author__ = 'carlos'


class Piece:
    
    def __init__(self, data):
        if isinstance(data, Content):
            self.content = data
            self.text = None
        elif isinstance(data, str):
            self.content = None
            self.text = data
            

class Content:
    def __init__(self, identif, title):
        """
        :param identif: content identifier
        :param title: content title
        :param data: the content data
        """
        self.id = id
        self.title = title
        self.created = datetime.datetime.now()
        self.pieces = {}


class Category(Content):

    def __init__(self):
        self.contents = set()
        
    def add(self, content):
        self.contents.add(content)
        