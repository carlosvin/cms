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
        content1 = Content (1, 'Title1')
        content1.add_piece(Piece('piece text'))
        
        content2 = Content(2, 'Title2')
        content2.append_piece(Piece('piece text'))
        content2.append_piece(Piece(content1))


if __name__ == "__main__":
    unittest.main()