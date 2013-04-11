import datetime

__author__ = 'carlos'


class Content(object):
    def __init__(self, id, title):
        self.id, self._title = id, title
        self.created = datetime.datetime.now()

        
class Category(Content):