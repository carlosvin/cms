'''
Created on 14/04/2013

@author: carlos
'''
import unittest
from models import Content, Piece


class TestContent(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCreate (self):
        content1 = Content (1, 'Title')
        content1.add_piece(Piece('2323'))


if __name__ == "__main__":
    unittest.main()