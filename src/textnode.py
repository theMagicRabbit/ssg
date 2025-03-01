from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = 'Normal text'
    BOLD_TEXT = 'Bold text'
    ITALIC_TEXT = 'Italic text'
    CODE = 'Code text'
    LINKS = 'Links'
    IMAGES = 'Images'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
            ):
            return True
        return False

    def __repr__(self):
        if not self.text_type:
            text_type_value = None
        else:
            text_type_value = self.text_type.value
        return f"TextNode({self.text}, {text_type_value}, {self.url})"

