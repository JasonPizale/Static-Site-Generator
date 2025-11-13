import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "# Heading 1"
        self.assertEqual(markdown_to_blocks(markdown), ["# Heading 1"])

    def test_multiple_blocks(self):
        markdown = "# Heading 1\n\nThis is a paragraph."
        self.assertEqual(markdown_to_blocks(markdown), ["# Heading 1", "This is a paragraph."])

    def test_extra_blank_lines(self):
        markdown = """
    # H1 


    This is a paragraph.

        
    """
        self.assertEqual(markdown_to_blocks(markdown), ["# H1", "This is a paragraph."])

if __name__ == '__main__':
    unittest.main()