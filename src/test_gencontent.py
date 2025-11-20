import pytest
from gencontent import extract_title

def test_extract_title_simple():
    markdown = "# Hello"
    assert extract_title(markdown) == "Hello"

def test_extract_title_second_line():
    markdown = "\n# World"
    assert extract_title(markdown) == "World"

def test_extract_title_no_title():
    markdown = "No headings here\nJust some text"
    with pytest.raises(Exception):
        extract_title(markdown)