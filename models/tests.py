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
        Content(1, 'Title')


if __name__ == "__main__":
    unittest.main()