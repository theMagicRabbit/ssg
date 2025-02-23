import unittest

from htmlnode import ParentNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_parent1(self):
        link1 = LeafNode('a', 'gitlab', {'href': 'https://www.gitlab.com'})
        link2 = LeafNode('a', 'DuckDuckGo', {'href': 'https://www.duckduckgo.com'})
        link3 = LeafNode('a', 'Python', {'href': 'https://www.python.org'})
        link4 = LeafNode('a', 'Signal', {'href': 'https://signal.org'})
        node_list1 = [link1, link2, link3, link4]
        html_node = ParentNode('div', node_list1, {'class': 'c_div'})
        self.assertEqual(html_node.to_html(), '<div class="c_div"><a href="https://www.gitlab.com">gitlab</a><a href="https://www.duckduckgo.com">DuckDuckGo</a><a href="https://www.python.org">Python</a><a href="https://signal.org">Signal</a></div>')

    def test_parent2(self):
        html_node = ParentNode(None, None, None)
        with self.assertRaises(ValueError):
            _ = html_node.to_html()

    def test_parent3(self):
        div1 = LeafNode('div', 'text in a leaf div', {'class': 'a_div'})
        text1 = LeafNode(None, 'Text in a parent node', None)
        b1 = LeafNode('b', 'This is bold text', None)
        p1 = ParentNode('p', [text1, b1], None)
        node_list3 = [div1, p1]
        html_node = ParentNode('div', node_list3, {'class': 'b_div'})
        self.assertEqual(html_node.to_html(), (
            '<div class="b_div">'
            '<div class="a_div">text in a leaf div</div>'
            '<p>'
            'Text in a parent node'
            '<b>This is bold text</b>'
            '</p>'
            '</div>'
            ))

    def test_parent4(self):
        p1 = LeafNode('p', 'This is a paragraph', None)
        html_node = ParentNode('div', [p1], None)
        self.assertEqual(html_node.to_html(), '<div><p>This is a paragraph</p></div>')

    def test_parent5(self):
        html_node = ParentNode('div', [], None)
        with self.assertRaises(ValueError):
            _ = html_node.to_html()

    def test_parent6(self):
        p1 = LeafNode('p', 'This is the text', None)
        div1 = ParentNode('div', [p1], None)
        div2 = ParentNode('div', [div1], None)
        div3 = ParentNode('div', [div2], None)
        div4 = ParentNode('div', [div3], None)
        div5 = ParentNode('div', [div4], None)
        html_node = ParentNode('div', [div5], None)
        self.assertEqual(html_node.to_html(), '<div><div><div><div><div><div><p>This is the text</p></div></div></div></div></div></div>')

if __name__ == '__main__':
    _ = unittest.main()

