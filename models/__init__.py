import datetime

__author__ = 'carlos'


class Content(object):
    def __init__(self, id, title):
        self._id, self._title = id, title
        self._created = datetime.datetime.now()


class Category(Content):