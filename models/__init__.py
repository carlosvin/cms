import datetime

__author__ = 'carlos'


class Content:
    def __init__(self, identif, title, desc):
        """

        :param identif: content identifier
        :param title: content title
        """
        self._id, self._title = id, title
        self._created = datetime.datetime.now()
        self.description = desc


class Category(Content):

    def __init__(self):
        self.contents = set()
        
    def add(self, content):
        self.contents.add(content)
        
        
class Piece:
    
    def __init__(self, data):
        if isinstance(data, Content):
            self.content = data
            self.text = None
        else:
            self.content = None
            self.text = data