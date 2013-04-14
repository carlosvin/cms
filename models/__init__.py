import datetime

__author__ = 'carlos'


class Content:
    def __init__(self, identif, title):
        """

        :param identif: content identifier
        :param title: content title
        """
        self._id, self._title = id, title
        self._created = datetime.datetime.now()


class Category(Content):

    def __init__(self):
        
        
class Piece:
    def __init__(self, data):
        self.content, self.data = None, None
        if isinstance(data, Content):
            self.content = data
        else:
            self.text = data