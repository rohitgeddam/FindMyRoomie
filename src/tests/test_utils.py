from django.test import SimpleTestCase
from django.urls import reverse, resolve
from src.base import utils


class TestUrls(SimpleTestCase):
    def test_(self):
        valid_ncsu_email = "abcd@ncsu.edu"
        invalid_ncsu_email = "abcd@gmail.com"

        self.assertEquals(utils.check_ncsu_email(valid_ncsu_email), True)
        self.assertEquals(utils.check_ncsu_email(invalid_ncsu_email), False)
