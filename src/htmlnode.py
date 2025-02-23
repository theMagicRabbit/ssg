from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplemented

    def props_to_html(self):
        if not self.props:
            return None
        prop_str = ""
        for key,value in self.props.items():
            prop_str += f" {key}=\"{value}\""
        return prop_str

    def __repl__(self):
        return f"tag: {self.tag}; value: {self.value}; children: {self.children}; props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html() if self.props else ""}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("HTML Tag is required")
        if not self.children:
            raise ValueError("Children nodes are required")
        children_value = reduce(lambda html_str, node: html_str + node.to_html(), self.children, "")
        return f"<{self.tag}{self.props_to_html() if self.props else ""}>{children_value}</{self.tag}>"


