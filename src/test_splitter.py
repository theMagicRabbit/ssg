import unittest
from mdsplitter import split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_code1(self):
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, expected)

    def test_bold1(self):
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold phrase", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        node = TextNode("This is text with a **bold phrase** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_italic1(self):
        expected = [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("italic phrase", TextType.ITALIC_TEXT),
                TextNode(" word", TextType.NORMAL_TEXT),
                ]
        node = TextNode("This is text with a _italic phrase_ word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, expected)

    def test_split_images1(self):
        expected = [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode("second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"),
                ]
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.NORMAL_TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(expected, new_nodes)

    def test_split_images2(self):
        expected = [
                TextNode("This string has no images, but it does have **bold** text.", TextType.NORMAL_TEXT),
                ]
        node = TextNode(
                "This string has no images, but it does have **bold** text.",
                TextType.NORMAL_TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(expected, new_nodes)

    def test_split_images3(self):
        expected = [
                TextNode("This string has no images, but it does have **bold** text.", TextType.NORMAL_TEXT),
                TextNode("This string has ", TextType.NORMAL_TEXT),
                TextNode("an image", TextType.IMAGES, "http://example.com/image.png"),
                ]
        node = TextNode(
                "This string has no images, but it does have **bold** text.",
                TextType.NORMAL_TEXT,
                )
        node2 = TextNode(
                "This string has ![an image](http://example.com/image.png)",
                TextType.NORMAL_TEXT,
                )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(expected, new_nodes)

    def test_split_images4(self):
        expected = []
        node = TextNode(None, None, None)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(expected, new_nodes)

    def test_split_images5(self):
        expected = [
                TextNode("an image", TextType.IMAGES, "http://example.com/image.png"),
                ]
        node = TextNode(
                "![an image](http://example.com/image.png)",
                TextType.NORMAL_TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(expected, new_nodes)

if __name__ == '__main__':
    _ = unittest.main()


