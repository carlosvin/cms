from models import Content, Factory, Piece
from settings.paths import CONTENT_FOLDER_NAME, CONTENT_PATH
import os
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    
    
class ContentXML:
    """
    Manage all persistence operations over a content
    """
#    
#    def __init__(self, content):
#        if isinstance(content, Content):
#            self.content = content
#            try:
#                _load(content.id)
#            except:
#                _save(content)
#        else:
#            raise 'Must be a models.Content instance'

    @staticmethod
    def load_piece(child_element, content):
        content_id = child_element['content_ref_id']
        child_element['index']
        if content_id:
            content = ContentXML.load(content_id) 
            p = Piece(content, index)
        
        
        
    @staticmethod
    def load(content_id):
        """
        It returns a content object if it exists, else it raises an exception
        """
        tree = etree.parse(ContentXML.get_path(content_id))
        root = tree.getroot()
        content = Factory.instantiate(content_id, root['title'], root['type'])
        for child in root:
            try:
                load_piece(child, content)
            
        return content
        
    @staticmethod 
    def get_path(content_id):
        return os.path.join(CONTENT_PATH, content_id + '.xml')