from django.conf.urls import url
from . import views

urlpatterns = [
    url('home_page/', views.home_page, name='home_page'),
]