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
        content1.append_piece(Piece('piece text'))
        
        content2 = Content(2, 'Title2')
        content2.append_piece(Piece('piece text'))
        content2.append_piece(Piece(content1))
        
    def testEq(self):
        content1 = Content(1,'asdf')
        content2 = Content(1,'asdf')
        self.assertEqual(content1, content2)
        
        content3 = Content(1,'1234')
        self.assertEqual(content1, content3)

        content4 = Content(2,'asdf')
        self.assertNotEqual(content1, content3)

if __name__ == "__main__":
    unittest.main()