import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("", TextType.BOLD_TEXT)
        node2 = TextNode("", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This", TextType.BOLD_TEXT)
        node2 = TextNode("This", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode('This is a text node', TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        node2 = TextNode("This is also a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        self.assertNotEqual(node, node2)

    def test_uneq2(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        node2 = TextNode("This is a text node", TextType.LINKS, "www.gitlab.com")
        self.assertNotEqual(node, node2)

    def test_uneq3(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.gitlab.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    _ = unittest.main()

