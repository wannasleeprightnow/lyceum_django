from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk: int):
    return HttpResponse('Подробно элемент')


def item_re_detail(request, pk: int):
    return HttpResponse(pk)
