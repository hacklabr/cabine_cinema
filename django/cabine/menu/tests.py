from django.test import TestCase
from menu import *

class ClipTest(TestCase):
    def setUp(self):
        self.proj = Clip.objects.create(name = 'teste',
                                           position = 1,
                                           file_path = "/home/hacklab/teste.avi",
                                           genre = Genre(),
                                           director = Director(),
                                           writer = Writer(),
                                           stars = Stars(),
                                           year = Year(),
                                           description = "fuuu")

class GenreTest(TestCase):
    def setUp(self):
        pass
