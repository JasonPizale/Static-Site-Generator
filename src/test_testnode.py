import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertEqual(node1, node2) 
    
    def test_eq_with_url(self):
        node1 = TextNode("Click here", TextType.LINK, url="http://example.com")
        node2 = TextNode("Click here", TextType.LINK, url="http://example.com")
        self.assertEqual(node1, node2)
    
    def test_not_eq_different_text(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hi", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_type(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_different_url(self):
        node1 = TextNode("Click here", TextType.LINK, url="http://example.com")
        node2 = TextNode("Click here", TextType.LINK, url="http://different.com")
        self.assertNotEqual(node1, node2)