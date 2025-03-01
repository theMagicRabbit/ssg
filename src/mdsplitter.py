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
    return new_nodes

