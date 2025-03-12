import re

def extract_markdown_images(md_text):
    ALT_RE = r"!\[(?P<alt>[\w\s]+)\]"
    SRC_RE = r"\((?P<src>https{,1}[-\w:./]+)(?:\s*\".*\"){,1}\)"
    IMAGE_RE = ALT_RE + SRC_RE
    matches = re.findall(IMAGE_RE, md_text)
    return matches

def extract_markdown_links(md_text):
    LINK_TEXT_RE = r"(?<!!)\[(?P<txt>[^\[\]]+)\]"
    URL_RE = r"\((?P<url>[^\(\)]*)\)"
    MD_LINK_RE = LINK_TEXT_RE + URL_RE
    matches = re.findall(MD_LINK_RE, md_text)
    return matches

def extract_title(md_text):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line.lstrip("# ").rstrip()
    raise ValueError("No h1 line found")

