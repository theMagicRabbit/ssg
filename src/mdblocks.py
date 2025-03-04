def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    map_blocks = list(map(lambda block: block.strip(), blocks))
    return map_blocks

