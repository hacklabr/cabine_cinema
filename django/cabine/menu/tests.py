# Copyright (C) 2012 Hacklab Ltda

# This software is free software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation;  either
# version 3 of the License, or (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this software; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


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
