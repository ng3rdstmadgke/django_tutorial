from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.UserCreate.as_view(), name='create'),
]
