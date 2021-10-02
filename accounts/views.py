from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


import logging

# Create your views here.
"""
- Qiita | Djangoで「会員登録機能 + ログイン機能」を実装する
  https://qiita.com/knakajima3027/items/34b2a105da7cdb411736
"""

def index(request):
    """
    - ログインしているかどうかの確認
      https://docs.djangoproject.com/ja/3.2/topics/auth/default/#limiting-access-to-logged-in-users
    """
    context = {}
    if request.user.is_authenticated:
        context["auth_user"] = request.user
    logging.info(context)
    return HttpResponse(render(request, 'accounts/index.html', context))

def user_logout(request):
    """
    - ログアウト
      https://docs.djangoproject.com/ja/3.2/topics/auth/default/#how-to-log-a-user-out
    """
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))

class UserLogin(View):
    """
    - クラスベースのビュー
      https://docs.djangoproject.com/ja/3.2/topics/class-based-views/intro/
    """
    def post(self, request):
        """
        - ログイン
          https://docs.djangoproject.com/ja/3.2/topics/auth/default/#how-to-log-a-user-in
        """
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:index'))
        else:
            context = {
                "error": True,
                "username": username,
            }
            return render(request, 'accounts/login.html', context)


    def get(self, request):
        return render(request, 'accounts/login.html')

class UserCreate(View):
    def post(self, request):
        """
        - ユーザー作成
          https://docs.djangoproject.com/ja/3.2/topics/auth/default/#creating-users
        """
        username = request.POST['username']
        password = request.POST['password1']
        email = "piyo@example.com"
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect(reverse('accounts:index'))

    def get(self, request):
        return render(request, 'accounts/create.html')