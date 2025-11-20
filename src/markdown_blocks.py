from enum import Enum
from htmlnode import ParentNode

class BlockType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    pieces = markdown.split("\n\n")

    stripped = [piece.strip() for piece in pieces]

    blocks = [piece for piece in stripped if piece]
    return blocks

def block_to_block_type(text: str) -> BlockType:
    lines = text.split("\n")
    is_quote = all(line.startswith(">") for line in lines)
    is_unordered = all(line.rstrip().startswith("- ") for line in lines)
    is_ordered = all(line.rstrip().startswith(f"{i}. ") for i, line in enumerate(lines, start=1))
    is_code = text.startswith("```") and text.endswith("```")
    
    i = 0
    while i < len(text) and text[i] == "#":
        i += 1
    n_hashes = i
    is_heading = (
        1 <= n_hashes <= 6
        and len(text) > n_hashes
        and text[n_hashes] == " "
    )
    if is_code:
        return BlockType.CODE
    if is_ordered:
        return BlockType.OLIST
    if is_unordered:
        return BlockType.ULIST
    if is_quote:
        return BlockType.QUOTE
    if is_heading:
        return BlockType.HEADING
    return BlockType.PARAGRAPH

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")
