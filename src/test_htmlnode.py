import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props1(self):
        html_node = HTMLNode('a', "www.gitlab.com", None, {'href': "https://www.gitlab.com"})
        self.assertEqual(html_node.props_to_html(), ' href="https://www.gitlab.com"')

    def test_props2(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), None)

    def test_props3(self):
        html_node = HTMLNode('a', None, None, {})
        self.assertEqual(html_node.props_to_html(), None)

    def test_props4(self):
        html_node = HTMLNode('div', None, None, {'draggable': 'true'})
        self.assertEqual(html_node.props_to_html(), ' draggable="true"')


if __name__ == '__main__':
    _ = unittest.main()

