from django.shortcuts import render
from datetime import datetime


def demo(request):
    context = {
        'today': datetime.now(),
        'value': {},
        'list': ['a', 'b', 'c', 'd'],
        'float': 0.99,
        'string': "Hello",
        'safe': "<script>alert('hello world');</script>",
        'mytime': datetime(year=2020, month=4, day=5, hour=12, minute=0, second=0)
    }
    return render(request, 'filter.html', context=context)
