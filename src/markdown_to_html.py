from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

def inline_children(text: str):
    tnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in tnodes]

def markdown_to_html_node(markdown: str) -> ParentNode:
    root = ParentNode('div', [])

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            para_text = " ".join(line.strip() for line in block.split("\n") if line.strip())
            node = ParentNode("p", inline_children(para_text))
        
        elif block_type == BlockType.HEADING:
            line = block.split("\n", 1)[0]
            level = len(line) - len(line.lstrip("#"))
            level = max(1, min(6, level))
            content = line[level:].lstrip(" ")
            node = ParentNode(f"h{level}", inline_children(content))
        
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            inner = "\n".join(lines[1:-1])
            node = ParentNode("pre", [LeafNode("code", inner)])
        
        elif block_type == BlockType.QUOTE:
            lines = [ln.lstrip("> ").lstrip(">") for ln in block.split("\n")]
            text = " ".join(s for s in (ln.strip() for ln in lines) if s)
            node = ParentNode("blockquote", inline_children(text))
        
        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for ln in block.split("\n"):
                ln = ln.strip()
                if ln.startswith(("- ", "* ")):
                    item_text = ln[2:]
                    items.append(ParentNode("li", inline_children(item_text)))
            node = ParentNode("ul", items)
        
        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for ln in block.split("\n"):
                ln = ln.strip()
                i = ln.find(". ")
                if i > 0 and ln[:i].isdigit():
                    item_text = ln[i+2:]
                    items.append(ParentNode("li", inline_children(item_text)))
            node = ParentNode("ol", items)
        
        else:
            node = ParentNode("p", inline_children(block))

        root.children.append(node)
    
    return root
              