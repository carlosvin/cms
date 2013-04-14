from models import Content
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    
    
class ContentXML:
    """
    Manage all persistence operations over a content
    """
    
    def __init__(self, content):
        if isinstance(content, Content):
            self.content = content
            try:
                _load(content.id)
            except:
                _save(content)
        else:
            raise 'Must be a models.Content instance'
        
    def load(self, content):