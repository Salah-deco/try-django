#https://docs.python.org/3/library/unittest.html
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
import os

class TryDjangoConfigTest(TestCase):
    # def test_name(self):
    #     self.assertTrue(1==1)
    #     self.assertFalse(1==0)
    #     self.assertEqual("ss", "ss")
    #     self.assertNotEqual(0, 2)

    def test_secret_key_strength(self):
        SECRET_KEY = settings.SECRET_KEY
        # SECRET_KEY2 = os.environ.get("DJANGO_SECRET_KEY")
        # self.assertEqual(SECRET_KEY, "abc")
        SECRET_KEY = "abc"

        try:
            is_strong = validate_password(SECRET_KEY)

        except Exception as e:
            msg = f'Bad Secret Key {e.messages}'
            self.fail(msg)