"""book_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from App01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.index, name='index'),
    path('add_book/', views.addBook, name='addBook'),
    path('add_author/', views.addAuthor, name='addAuthor'),
    path('add_publish/', views.addPublish, name='addPublish'),
    path('book_manage/', views.bookManage, name='bookManage'),
    re_path('compile_book/(?P<id>\d+)/', views.compileBook, name='compileBook'),
    re_path('del_book/(?P<id>\d+)/', views.delBook, name='delBook'),
    path('manage_author/', views.manageAuthor, name='manageAuthor'),
    path('manage_publish/', views.managePublish, name='managePublish'),
    re_path('compile_author/(?P<id>\d+)/', views.compileAuthor, name='compileAuthor'),
    re_path('del_author/(?P<id>\d+)/', views.delAuthor, name='delAuthor'),
    re_path('del_publish/(?P<id>\d+)/', views.delPublish, name='delPublish'),
    re_path('compile_publish/(?P<id>\d+)/',views.compilePublish,name='compilePublish')
]
