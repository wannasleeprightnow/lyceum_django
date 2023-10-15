from django import test


class StaticURLTest(test.TestCase):
    @test.override_settings(ALLOW_REVERSE=True)
    def test_allow_reverse_russian_words(self):
        contents = [test.Client().get('/coffee/').content for _ in range(10)]
        self.assertIn('Я чайник'.encode(), contents)
        self.assertIn('Я кинйач'.encode(), contents)
        self.assertEqual(contents.count('Я чайник'.encode()), 9)
        self.assertEqual(contents.count('Я кинйач'.encode()), 1)

    @test.override_settings(ALLOW_REVERSE=False)
    def test_disallow_reverse_russian_words(self):
        contents = [test.Client().get('/coffee/').content for _ in range(10)]
        self.assertIn('Я чайник'.encode(), contents)
        self.assertNotIn('Я кинйач'.encode(), contents)
        self.assertEqual(contents.count('Я чайник'.encode()), 10)
        self.assertEqual(contents.count('Я кинйач'.encode()), 0)

    def test_reverse_russian_words(self):
        contents = [test.Client().get('/coffee/').content for _ in range(10)]
        self.assertIn('Я чайник'.encode(), contents)
        self.assertIn('Я кинйач'.encode(), contents)
        self.assertEqual(contents.count('Я чайник'.encode()), 9)
        self.assertEqual(contents.count('Я кинйач'.encode()), 1)
