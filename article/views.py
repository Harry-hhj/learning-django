from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def article(request):
    return HttpResponse('文章首页')


def article_list(request, year):
    if int(year) <= 2020:
        text = '你输入的年份是 %s' % year
        return HttpResponse(text)
    else:
        article_url = reverse('article:year', kwargs={'year': '2020'})
        return redirect(article_url)


def article_list_month(request, year, month):
    text = '你输入的年份是 %s 月份是 %s' % (year, month)
    return HttpResponse(text)


def article_list_date(request, year, month, date):
    text = '你输入的年份是 %s 月份是 %s 日期是 %s' % (year, month, date)
    return HttpResponse(text)


def article_categories_list(request, categories):
    text = '您给的分类是 % s' % categories
    return HttpResponse(text)
