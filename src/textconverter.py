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
            return LeafNode('img', "", props)
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
                code_node = TextNode(block.replace('```', '').lstrip(), TextType.CODE)
                html_node = text_node_to_html_node(code_node)
                block_html.append(ParentNode('pre', [html_node]))
            case BlockType.HEADING:
                h_level = f"h{block.count('#')}"
                heading_nodes = list(map(lambda md_node: text_node_to_html_node(md_node), text_to_textnode(block.lstrip('# '))))
                block_html.append(ParentNode(h_level, heading_nodes))
            case BlockType.QUOTE:
                quote_text = "\n".join(map(lambda line: line.lstrip('> '), block.splitlines()))
                block_html.append(LeafNode('blockquote', quote_text))
            case BlockType.ULIST:
                items = map(lambda line: line.lstrip('- '), block.splitlines())
                child_list = []
                for list_item in items:
                    ulist_item_html = list(map(lambda md_node: text_node_to_html_node(md_node), text_to_textnode(list_item)))
                    child_list.append(ParentNode('li', ulist_item_html))
                list_node = ParentNode('ul', child_list)
                block_html.append(list_node)
            case BlockType.OLIST:
                ol_re = r"^(\d+\.\s+)"
                lines = block.splitlines()
                matches = map(lambda line: match(ol_re, line), lines)
                items = map(lambda line_m: line_m[0].lstrip(line_m[1].group(1)), zip(lines, matches))
                child_list = []
                for list_item in items:
                    ol_item_node = list(map(lambda md_node: text_node_to_html_node(md_node), text_to_textnode(list_item)))
                    child_list.append(ParentNode('li', ol_item_node))
                list_node = ParentNode('ol', child_list)
                block_html.append(list_node)
            case _:
                raise TypeError("Block is unknown type")
        html_nodes.extend(block_html)
    return ParentNode('div', html_nodes)

