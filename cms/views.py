from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        current_namespace = request.resolver_match.namespace
        login_url = reverse('%s:login' % current_namespace)
        return redirect(login_url)


def login(request):
    return HttpResponse('CMS登陆页面')


def demo(request):
    context = {
        'heros': [
            '鲁班一号',
            '项羽',
            '程咬金'
        ],
        'book_list': [
            '三国演义',
            '水浒传',
            '西游记',
            '红楼梦'
        ],
        'person': {
            'username': 'test_user',
            'age': 18,
            'height': 180
        },
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 199
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 109
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 99
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 100
            }
        ],
        'comments': [],
        'info': "<a href='www.baidu.com'>百度</a>"
    }
    return render(request, 'cms_index.html', context=context)
