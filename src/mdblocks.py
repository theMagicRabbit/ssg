from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    ULIST = 'unordered list'
    OLIST = 'ordered list'

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    map_blocks = list(map(lambda block: block.strip(), blocks))
    return map_blocks

def block_to_block_type(markdown):
    heading_re = r"^#{1,6}\s+"
    code_re = r"^(```).*(```)$"
    quote_re = r"^> "
    ulist_re = r"^- "
    olist_re = r"^\n+\. "

    heading = re.match(heading_re, markdown, re.M)
    code = re.match(code_re, markdown, re.M)
    quote = re.match(quote_re, markdown, re.M)
    ulist = re.match(ulist_re, markdown, re.M)
    olist = re.match(olist_re, markdown, re.M)

    if heading:
        return BlockType.HEADING
    elif code:
        return BlockType.CODE
    elif quote:
        return BlockType.QUOTE
    elif ulist:
        return BlockType.ULIST
    elif olist:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH


    

