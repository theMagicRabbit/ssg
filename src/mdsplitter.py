from textnode import TextNode, TextType
from mdextractor import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter not in node.text:
            new_nodes.append(node)
        else:
            split_strs = node.text.split(sep=delimiter)
            enum_strs = list(enumerate(split_strs))
            match_text_type = map(lambda enum_tup: (enum_tup[1], node.text_type) if not enum_tup[0] % 2 else (enum_tup[1], text_type), enum_strs)
            new_nodes_map = map(lambda str_type_tup: TextNode(str_type_tup[0], str_type_tup[1]), match_text_type)
            new_nodes.extend(new_nodes_map)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        node_text = node.text
        for alt,src in images:
            text_splits = node_text.split(f"![{alt}]({src})", 1)
            if text_splits[0]:
                new_nodes.append(TextNode(text_splits[0], TextType.NORMAL_TEXT))
            node_text = text_splits[1]
            new_nodes.append(TextNode(alt, TextType.IMAGES, src))
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.NORMAL_TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        node_text = node.text
        for txt,url in links:
            text_splits = node_text.split(f"[{txt}]({url})", 1)
            if text_splits[0]:
                text_node = TextNode(text_splits[0], TextType.NORMAL_TEXT)
                new_nodes.append(text_node)
            node_text = text_splits[1]
            new_nodes.append(TextNode(txt, TextType.LINKS, url))
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.NORMAL_TEXT))
    return new_nodes

def text_to_textnode(text):
    node = TextNode(text, TextType.NORMAL_TEXT)
    new_nodes = [node]
    md_types = [
            ('**', TextType.BOLD_TEXT),
            ('_', TextType.ITALIC_TEXT),
            ('`', TextType.CODE),
            ]
    if not text:
        return new_nodes
    for delim,text_type in md_types:
        new_nodes = split_nodes_delimiter(new_nodes, delim, text_type)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

