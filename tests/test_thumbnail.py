from rest_framework.test import APITestCase
from dmrt.util import generate_image
from PIL import Image


class ThumbnailTestCase(APITestCase):
    # Landscape: 1024x768 (4:3)
    def test_landscape_square(self):
        img = Image.open(generate_image("landscape.png", 200))
        self.assertEqual(img.size, (200, 200))

    def test_landscape_fit(self):
        img = Image.open(generate_image("landscape.png", 400))
        self.assertEqual(img.size, (400, 400 * 0.75))

    def test_landscape_maxwidth(self):
        img = Image.open(generate_image("landscape.png", 700))
        self.assertEqual(img.size, (700, 700 * 0.75))

    # Portrait: 768x1024 (3:4)
    def test_portrait_square(self):
        img = Image.open(generate_image("portrait.png", 200))
        self.assertEqual(img.size, (200, 200))

    def test_portrait_fit(self):
        img = Image.open(generate_image("portrait.png", 400))
        self.assertEqual(img.size, (400 * 0.75, 400))

    def test_portrait_maxwidth(self):
        img = Image.open(generate_image("portrait.png", 700))
        self.assertEqual(img.size, (700, 700 // 0.75))

    # Small: 1x1 (1:1)
    def test_small_square(self):
        img = Image.open(generate_image("small.png", 200))
        self.assertEqual(img.size, (200, 200))

    def test_small_fit(self):
        img = Image.open(generate_image("small.png", 400))
        self.assertEqual(img.size, (1, 1))

    def test_small_maxwidth(self):
        img = Image.open(generate_image("small.png", 700))
        self.assertEqual(img.size, (1, 1))
