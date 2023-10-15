from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_home_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
