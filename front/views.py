from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render
# from django.template.loader import render_to_string


class Person(object):
    def __init__(self, username):
        self.username = username


def index(request):
    # ?username=xxx
    username = request.GET.get('username')
    if username:
        # html = render_to_string("front_index.html")
        # return HttpResponse(html)
        # context = {'username': username}
        p = Person(username)
        context = {'person': p}
        return render(request, "front_index.html", context=context)
    else:
        login_url = reverse('front:login') + '?next=/'
        return redirect(login_url)


def login(request):
    text = request.GET.get('next')
    return HttpResponse('前台登陆页面<br></br>登陆完成后要跳转的url是 %s' % text)
