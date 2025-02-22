import unittest

from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_leaf1(self):
        html_node = LeafNode('a', "www.gitlab.com", {'href': "https://www.gitlab.com"})
        self.assertEqual(html_node.to_html(), '<a href="https://www.gitlab.com">www.gitlab.com</a>')

    def test_leaf2(self):
        html_node = LeafNode(None, None, None)
        with self.assertRaises(ValueError):
            _ = html_node.to_html()

    def test_leaf3(self):
        html_node = LeafNode(None, "This is plain text", None)
        self.assertEqual(html_node.to_html(), "This is plain text")

    def test_leaf4(self):
        html_node = LeafNode('div', "This is a div", None)
        self.assertEqual(html_node.to_html(), '<div>This is a div</div>')

if __name__ == '__main__':
    _ = unittest.main()

