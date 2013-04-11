import datetime

__author__ = 'carlos'


class Content(object):
    def __init__(self, identif, title):
        """

        :param identif: content identifier
        :param title: content title
        """
        self._id, self._title = id, title
        self._created = datetime.datetime.now()


class Category(Content):

    def a(self):
        print("")