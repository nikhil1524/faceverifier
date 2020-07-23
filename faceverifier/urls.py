from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views
from .views import UploadedImageView

# router = routers.DefaultRouter()
# router.register('images', UploadedImagesViewSet, 'images')

urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='singUp'),
    path('home', views.home, name='home'),
    path('uploadimage', views.uploadimages, name='uploadimage'),
    path('setting', views.usersetting, name='settings'),
    path('license', views.userlicense, name='license'),
    path('logout',  views.logout, name='logout'),
    url('api/image/', UploadedImageView.as_view()),
]
handler404 = views.error404