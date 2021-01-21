from django.urls import path, re_path, include
from . import views

app_name = 'articles'

urlpatterns = [ # order in list is important
    re_path(r'^$',views.article_list, name='list'),
    re_path(r'^create/$',views.article_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='detail'),
]