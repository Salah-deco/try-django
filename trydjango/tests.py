#https://docs.python.org/3/library/unittest.html
from django.test import TestCase


class TryDjangoConfigTest(TestCase):
    def test_name(self):
        self.assertTrue(1==1)