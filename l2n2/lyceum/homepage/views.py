from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse('Главная')


def coffee(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
