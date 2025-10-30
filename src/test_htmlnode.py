import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_one_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://www.boot.dev"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.boot.dev"') 
    
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(tag="a", props={"href": "image.png", "target": "An image"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="image.png" target="An image"')

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag="a")
        result = node.props_to_html()
        self.assertEqual(result, "")