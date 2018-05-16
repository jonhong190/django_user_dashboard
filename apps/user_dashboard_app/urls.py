from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^sign_in$', views.sign_in),
    url(r'register$', views.register)
]