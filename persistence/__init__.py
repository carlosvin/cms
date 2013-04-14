from models import Content
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    
class ContentXML:
    
    def __init__(self, content):
        if isinstance(content, Content)