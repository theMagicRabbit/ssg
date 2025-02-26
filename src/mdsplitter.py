from textnode import TextNode, TextType

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

