from re import match
from htmlnode import LeafNode, ParentNode
from textnode import TextType, TextNode
from mdsplitter import text_to_textnode
from mdblocks import BlockType, markdown_to_blocks, block_to_block_type

def text_node_to_html_node(text_node):
    props = None
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text.replace('\n', ' '), props)
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

def markdown_to_html_node(markdown):
    html_nodes = []
    for block in markdown_to_blocks(markdown):
        block_html = []
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                child_nodes = list(map(lambda md_node: text_node_to_html_node(md_node), text_to_textnode(block)))
                parent = ParentNode('p', child_nodes)
                block_html.append(parent)
            case BlockType.CODE:
                block_html.append(TextNode(block.strip('`'), TextType.CODE))
            case BlockType.HEADING:
                block_html.append(LeafNode('h1', block.lstrip('# ')))
            case BlockType.QUOTE:
                quote_text = "\n".join(map(lambda line: line.lstrip('> '), block.splitlines()))
                block_html.append(LeafNode('q', quote_text))
            case BlockType.ULIST:
                items = map(lambda line: line.lstrip('- '), block.splitlines())
                ulist_nodes_list = list(map(lambda item: LeafNode('li', item), items))
                list_node = ParentNode('ul', ulist_nodes_list)
                block_html.append(list_node)
            case BlockType.OLIST:
                ol_re = r"^(\d+\.\s+)"
                lines = block.splitlines()
                matches = map(lambda line: match(ol_re, line), lines)
                items = map(lambda line_m: line_m[0].lstrip(line_m[1].group(1)), zip(lines, matches))
                olist_nodes_list = list(map(lambda item: LeafNode('li', item), items))
                list_node = ParentNode('ol', olist_nodes_list)
                block_html.append(list_node)
            case _:
                raise TypeError("Block is unknown type")
        html_nodes.extend(block_html)
    return ParentNode('div', html_nodes)



        

    

