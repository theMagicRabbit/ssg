import unittest
from mdextractor import extract_markdown_images

class TestTextNode(unittest.TestCase):
    def test_images1(self):
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_images2(self):
        expected = [("image", "https://www.github.com/image.jpg"), ("image2", "https://i.imgur.com/fJRm4Vk.jpeg"), ("image3", "http://example.com/unsecure.png")]
        text = "This is text with a ![image](https://www.github.com/image.jpg) and ![image2](https://i.imgur.com/fJRm4Vk.jpeg) and another ![image3](http://example.com/unsecure.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

    def test_images3(self):
        expected = [("boot dev logo", "https://www.boot.dev/img/bootdev-logo-full-small.web")]
        text = "This is text with a ![boot dev logo](https://www.boot.dev/img/bootdev-logo-full-small.web 'boot dev logo')"
        images = extract_markdown_images(text)
        self.assertEqual(images, expected)

if __name__ == '__main__':
    _ = unittest.main()


