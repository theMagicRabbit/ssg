from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is the text", TextType.BOLD_TEXT, "www.gitlab.com")
    print(text_node)

if __name__ == '__main__':
    main()

