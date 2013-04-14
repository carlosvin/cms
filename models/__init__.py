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
        self.pieces = []
        
    def add_piece(self, index, piece):
        self.pieces.insert(index, piece)
        
    def append_piece(self, piece):
        self.pieces.append(piece)
    
    def __eq__(self, c):
        return self.id == c.id
    
    def __ne__(self, c):
        return self.id <> c.id


class Category(Content):

    def __init__(self):
        self.contents = set()
        
    def add(self, content):
        self.contents.add(content)
        