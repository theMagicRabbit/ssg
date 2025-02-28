import re

ALT_RE = r"!\[(?P<alt>[\w\s]+)\]"
SRC_RE = r"\((?P<url>https{,1}[-\w:./]+)(?:\s*\".*\"){,1}\)"
IMAGE_RE = ALT_RE + SRC_RE

def extract_markdown_images(md_text):
    matches = re.findall(IMAGE_RE, md_text)
    return matches

