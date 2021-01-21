from django.urls import path, re_path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name="signup"),
]