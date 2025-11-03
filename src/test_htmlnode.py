import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node

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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")