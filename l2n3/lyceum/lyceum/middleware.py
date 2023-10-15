from re import sub

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class ReverseWordsMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)

        if not settings.ALLOW_REVERSE:
            return response

        if not settings.MIDDLEWARE_COUNTER % 10:
            response.content = self.reverse_russian_words(
                response.content.decode('utf-8')
            ).encode('utf-8')
        settings.MIDDLEWARE_COUNTER += 1

        return response

    def reverse_russian_words(self, response_text):
        def reverse_word(word):
            return word.group()[::-1]

        return sub(r'[а-яА-ЯёЁ]+', reverse_word, response_text)
