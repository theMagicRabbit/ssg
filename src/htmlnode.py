from enum import Enum

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
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

