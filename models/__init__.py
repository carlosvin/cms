import datetime

__author__ = 'carlos'


class Piece:
    
    def __init__(self, data, index = None):
        """
        :param data: Must be a Content object or a string
        """
        self.index = index
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
        return self.id is not c.id

class Category(Content):

    def __init__(self, identif, title):
        super().__init__(identif, title)
        self.contents = set()
        
    def add(self, content):
        self.contents.add(content)
        
class Factory:
    
    @staticmethod
    def instantiate(c_id, title, c_type):
        if c_type == Category.__name__:
            return Category(c_id, title)
        else:
            raise 'Unknown type ' + type
            
        