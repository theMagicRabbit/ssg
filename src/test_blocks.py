import unittest
from mdblocks import markdown_to_blocks, block_to_block_type, BlockType

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                    ],
                )

    def test_markdown_to_blocks2(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "# This is a heading",
                    "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                    "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
                    ],
                )

    def test_block_type1(self):
        expected = BlockType.HEADING
        md = "# This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(expected, block_type)

    def test_block_type2(self):
        expected = BlockType.HEADING
        md = "###### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(expected, block_type)

    def test_block_type3(self):
        expected = BlockType.PARAGRAPH
        md = "####### This is a heading"
        block_type = block_to_block_type(md)
        self.assertEqual(expected, block_type)




if __name__ == '__main__':
    _ = unittest.main()


