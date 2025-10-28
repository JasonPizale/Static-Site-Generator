from textnode import TextNode, TextType

def main():
    node = TextNode("hello world", TextType.LINK, url="http://example.com")
    print(node)
if __name__ == "__main__":
    main()
