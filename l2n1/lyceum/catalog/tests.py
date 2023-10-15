from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_info_endpoint(self):
        response = Client().get('/catalog/3/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
