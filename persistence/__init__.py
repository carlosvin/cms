from models import Content, Factory, Piece, Category
from settings.paths import CONTENT_FOLDER_NAME, CONTENT_PATH
import os
import logging
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    
class CategoryXML:
    @staticmethod
    
    
class ContentXML:
    """
    Manage all persistence operations over a content
    """
    def __init__(self):
        self.content = None

    def load_piece(self, child_element):
        content_id = child_element['content_ref_id']
        index = child_element['index']
        if content_id:
            content = ContentXML.load(content_id) 
            p = Piece(content, index)
        else:
            p = Piece(child_element.text, index)
        return p
        
    @staticmethod
    def load_child_content(child_element, content):
        if isinstance(content, Category):
            CategoryXML.
        
        
    @staticmethod
    def load(content_id):
        """
        It returns a content object if it exists, else it raises an exception
        """
        tree = etree.parse(ContentXML.get_path(content_id))
        root = tree.getroot()
        self.content = Factory.instantiate(content_id, root['title'], root['type'])
        for child in root:
            try:
                ContentXML.load_piece(child, content)
            except Exception as e:
                logging.warning(e)
        ContentXML.load_child_content(root, content)
        return content
        
    @staticmethod 
    def get_path(content_id):
        return os.path.join(CONTENT_PATH, content_id + '.xml')