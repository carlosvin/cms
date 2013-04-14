import datetime

__author__ = 'carlos'


class Piece:
    
    def __init__(self, data):
        """
        :param data: Must be a Content object or a string
        """
        if isinstance(data, Content):
            self.content = data
            self.text = None
        elif isinstance(data, str):
            self.content = None
            self.text = data
        else:
            raise 'Data argument only can be a Content object or a string'
            

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
        
    def add_piece(self, order, piece):


class Category(Content):

    def __init__(self):
        self.contents = set()
        
    def add(self, content):
        self.contents.add(content)
        