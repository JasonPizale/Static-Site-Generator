import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    extract_markdown_images, 
    extract_markdown_links
)
from textnode import TextNode, TextType

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        text = "![a](http://example.com/a.png) and ![b](http://example.com/b.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("a", "http://example.com/a.png"), ("b", "http://example.com/b.jpg")], matches)

    def test_no_images(self):
        text = "Just some text without images."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "A link [to boot dev](https://boot.dev)."
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://boot.dev")], matches)
    
    def test_multiple_links(self):
        text = "[a](http://a.com) and [b](http://b.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("a", "http://a.com"), ("b", "http://b.com")], matches)  
    
    def test_no_links(self):
        text = "Nothing here."
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)
    
    def test_ignore_images(self):
        text ="![img](http://i.com/x.png) and [site](http://s.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("site", "http://s.com")], matches)

class TestInlineMarkdownParsing(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text")
    
    def test_split_nodes_delimiter_italic(self):
        old_nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " text")

    def test_split_nodes_code(self):
        old_nodes = [TextNode("Here is `code` snippet", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Here is ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " snippet")

    def test_split_nodes_image_basic(self):
        nodes = [TextNode("A ![obi](https://img) B", TextType.TEXT)]
        got = split_nodes_image(nodes)
        want = [
            ("A ", TextType.TEXT, None),
            ("obi", TextType.IMAGE, "https://img"),
            (" B", TextType.TEXT, None),
        ]
        self.assertEqual(
            [(n.text, n.text_type, getattr(n, "url", None)) for n in got],
            want,
        )

    def test_text_to_textnodes_mixed(self):
        text = "This is **bold** and *it* and `code` and ![img](https://i) and a [lnk](https://b)"
        got = text_to_textnodes(text)
        want = [
            ("This is ", TextType.TEXT, None),
            ("bold", TextType.BOLD, None),
            (" and ", TextType.TEXT, None),
            ("it", TextType.ITALIC, None),
            (" and ", TextType.TEXT, None),
            ("code", TextType.CODE, None),
            (" and ", TextType.TEXT, None),
            ("img", TextType.IMAGE, "https://i"),
            (" and a ", TextType.TEXT, None),
            ("lnk", TextType.LINK, "https://b"),
        ]
        self.assertEqual(
            [(n.text, n.text_type, getattr(n, "url", None)) for n in got],
            want,
        )

if __name__ == '__main__':
    unittest.main()