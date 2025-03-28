import unittest

from textconverter import text_node_to_html_node, markdown_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_empty(self):
        text_node = TextNode(None, None, None)
        with self.assertRaises(ValueError):
            _ = text_node_to_html_node(text_node)

    def test_normal(self):
        text_node = TextNode("This is plain text", TextType.NORMAL_TEXT, None)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is plain text")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)

    def test_bold(self):
        text = "This is bold text"
        text_node = TextNode(text, TextType.BOLD_TEXT, None)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)

    def test_italic(self):
        text = "This is italic text"
        text_node = TextNode(text, TextType.ITALIC_TEXT, None)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)

    def test_link(self):
        text = "This is link text"
        url = "https://www.gitlab.com"
        text_node = TextNode(text, TextType.LINKS, url)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props['href'], url)
        self.assertEqual(html_node.children, None)

    def test_image(self):
        text = "This is link text"
        url = "https://www.gitlab.com"
        text_node = TextNode(text, TextType.IMAGES, url)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props['src'], url)
        self.assertEqual(html_node.props['alt'], text)
        self.assertEqual(html_node.children, None)

    def test_code(self):
        text = "This is code text"
        text_node = TextNode(text, TextType.CODE, None)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        ) 

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
This paragraph has a quote

> This is a quotation

This is a second paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This paragraph has a quote</p><blockquote>This is a quotation</blockquote><p>This is a second paragraph</p></div>",
        )

    def test_multiline_quoteblock(self):
        md = """
# Tolkien Fan Club

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><h1>Tolkien Fan Club</h1><p>Here's the deal, <b>I like Tolkien</b>.</p><blockquote>"I am in fact a Hobbit in all but size."\n\n-- J.R.R. Tolkien</blockquote><h1>Blog posts</h1></div>""",
        )

if __name__ == '__main__':
    _ = unittest.main()

