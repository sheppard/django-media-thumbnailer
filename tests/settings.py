SECRET_KEY = '1234'
MIDDLEWARE_CLASSES = tuple()
MEDIA_ROOT="tests/images"
ROOT_URLCONF="tests.urls"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
