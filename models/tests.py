'''
Created on 14/04/2013

@author: carlos
'''
import unittest
from models import Content


class TestContent(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCreate (self):
        content = Content (1, 'Title')
        content.add_piece(Piece('2323'))


if __name__ == "__main__":
    unittest.main()