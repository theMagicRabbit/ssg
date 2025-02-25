from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    props = None
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text, props)
        case TextType.BOLD_TEXT:
            return LeafNode('b', text_node.text, props)
        case TextType.ITALIC_TEXT:
            return LeafNode('i', text_node.text, props)
        case TextType.CODE:
            return LeafNode('code', text_node.text, props)
        case TextType.LINKS:
            props = {'href': text_node.url}
            return LeafNode('a', text_node.text, props)
        case TextType.IMAGES:
            props = {'src': text_node.url, 'alt': text_node.text}
            return LeafNode('img', None, props)
        case _:
            raise ValueError(f"TextNode is of unknown value: {text_node.text_type}")

