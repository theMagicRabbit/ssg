from enum import Enum
from functools import reduce
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
    heading = re.match(heading_re, markdown, re.M)
    if heading:
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    md_list = markdown.splitlines()
    quote = reduce(lambda cur, next: cur and next.startswith("> "), md_list, True)
    
    if quote:
        return BlockType.QUOTE
    
    ulist = reduce(lambda cur, next: cur and next.startswith("- "), md_list, True)
    if ulist:
        return BlockType.ULIST

    if markdown.startswith('1.'):
        i = 1
        for line in md_list:
            if not line.startswith(f"{i}."):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


    

