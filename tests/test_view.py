from django.test import TestCase
from PIL import Image
from io import BytesIO


class ThumbnailTestCase(TestCase):
    def test_square(self):
        response = self.client.get("/generate/200/landscape.png")
        img = Image.open(BytesIO(response.content))
        self.assertEqual(img.size, (200, 200))

    def test_maxwidth(self):
        response = self.client.get("/generate/700/landscape.png")
        img = Image.open(BytesIO(response.content))
        self.assertEqual(img.size, (700, 700 * 0.75))
