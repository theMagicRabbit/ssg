import unittest
from mdextractor import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_images1(self):
        expected = [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ]
        text = (
                "This is text with a "
                "![rick roll](https://i.imgur.com/aKaOqIh.gif) "
                "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
                )
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_images2(self):
        expected = [
                ("image", "https://www.github.com/image.jpg"),
                ("image2", "https://i.imgur.com/fJRm4Vk.jpeg"),
                ("image3", "http://example.com/unsecure.png")
                ]
        text = (
                "This is text with a "
                "![image](https://www.github.com/image.jpg) "
                "and ![image2](https://i.imgur.com/fJRm4Vk.jpeg) "
                "and another ![image3](http://example.com/unsecure.png)"
                )
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_images3(self):
        expected = [("boot dev logo", "https://www.boot.dev/img/bootdev-logo-full-small.web")]
        text = "This is text with a ![boot dev logo](https://www.boot.dev/img/bootdev-logo-full-small.web \"boot dev logo\")"
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_images4(self):
        expected = [
                ("image", "https://www.web_site.com/image.jpg"),
                ("image2", "https://web-site.com/fJRm4Vk.jpeg"),
                ("image3", "http://example-web_site.com/unsecure.png")
                ]
        text = (
                "This is text with a "
                "![image](https://www.web_site.com/image.jpg) "
                "and ![image2](https://web-site.com/fJRm4Vk.jpeg) "
                "and another ![image3](http://example-web_site.com/unsecure.png)"
                )
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_links1(self):
        expected = [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
                ]
        text = (
                "This is text with a link [to boot dev](https://www.boot.dev) "
                "and [to youtube](https://www.youtube.com/@bootdotdev)"
                )
        links = extract_markdown_links(text)
        self.assertEqual(links, expected)

    def test_links2(self):
        expected = [
                ("link", "https://www.gitlab.com"),
                ]
        text = (
                "This is text with a link [link](https://www.gitlab.com) "
                )
        links = extract_markdown_links(text)
        self.assertEqual(links, expected)

    def test_links3(self):
        expected = [
                ("This is a long bit of text. Too long in fact.", "https://www.boot.dev"),
                ("to youtube", "http://www.youtube.com/@bootdotdev")
                ]
        text = (
                "This is a long bit of text. Too long in fact. "
                "[This is a long bit of text. Too long in fact.](https://www.boot.dev)"
                "and [to youtube](http://www.youtube.com/@bootdotdev)"
                )
        links = extract_markdown_links(text)
        self.assertEqual(links, expected)

    def test_links4(self):
        expected = []
        text = (
                "This is text with just an image, no link "
                "![image](https://example.com/image.gif"
                )
        links = extract_markdown_links(text)
        self.assertEqual(links, expected)

if __name__ == '__main__':
    _ = unittest.main()


