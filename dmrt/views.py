from django.http import HttpResponse
from .util import generate_image

def generate(request, size, image):
    data = generate_image(image, size)
    return HttpResponse(data.read())
