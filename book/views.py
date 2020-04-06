from django.http import HttpResponse
from django.shortcuts import render


def book(request):
    return render(request, 'book.html')


def book_detail(request, book_id):
    text = '您获取的图书id是 %s' % book_id
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET.get('id')
    text = '作者的id是 %s' % author_id
    return HttpResponse(text)


def pubish_detail(request, publisher_id):
    text = "出版社id是 %s" % publisher_id
    return HttpResponse(text)


def book_list(request):
    return HttpResponse('图书列表')
