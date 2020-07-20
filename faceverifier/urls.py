from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='singUp'),
    path('home', views.home, name='home'),
    #path('tryapi', views.tryapi, name='tryapi'),
    path('uploadimage', views.uploadimages, name='uploadimage'),
    path('setting', views.usersetting, name='settings'),
    path('license', views.userlicense, name='license'),
    path('logout',  views.logout, name='logout'),
]