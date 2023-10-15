from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_info_endpoint(self):
        response = Client().get('/catalog/3/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_catalog_re_info_endpoint(self):
        client = Client()
        response = client.get('/catalog/re/3/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response = client.get('/catalog/re/-3/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        response = client.get('/catalog/re/a/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        response = client.get('/catalog/re/0/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_catalog_converter_endpoint(self):
        client = Client()
        responses = [
            client.get(f'/catalog/converter/{i}/').status_code
            for i in range(1, 100)
        ]
        self.assertEqual(responses.count(HTTPStatus.OK), 99)
        responses = [
            client.get(f'/catalog/converter/{i}/').status_code
            for i in range(0, -99, -1)
        ]
        self.assertEqual(responses.count(HTTPStatus.NOT_FOUND), 99)
        response = client.get('/catalog/converter/a/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
