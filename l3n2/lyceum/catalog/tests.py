from http import HTTPStatus

from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from catalog.models import Category, Item, Tag


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


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(
            is_published=True, name='test-name1', slug='test-slug1', weight=100
        )

        cls.tag = Tag.objects.create(
            is_published=True, name='test-name2', slug='test-slug2'
        )

    def test_max_name_lenght(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='test-item' * 100,
                category=self.category,
                text='превосходно',
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_min_text_lenght(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='test-item',
                category=self.category,
                text='1',
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_perfect_in_text(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='test-item',
                category=self.category,
                text='test-text',
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTest.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_create(self):
        item_count = Item.objects.count()
        self.item = Item(
            name='test-item',
            category=self.category,
            text='превосходно, роскошно',
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTest.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_slug_validator(self):
        tag_count = Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.test_tag = Tag(name='test-tag', slug='slug(((@#)))')
            self.test_tag.full_clean()
            self.test_tag.save()
        self.assertEqual(Tag.objects.count(), tag_count)

    def test_category_max_weight(self):
        categories_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.test_category = Category(name='test-category', weight=1000000)
            self.test_category.full_clean()
            self.test_category.save()
        self.assertEqual(Category.objects.count(), categories_count)

    def test_category_min_weight(self):
        categories_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.test_category = Category(name='test-category', weight=-1)
            self.test_category.full_clean()
            self.test_category.save()
        self.assertEqual(Category.objects.count(), categories_count)
