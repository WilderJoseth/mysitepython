from django.urls import path
from mysite.apps.app1 import views

urlpatterns = [
    path('', views.index, name = 'index'),
]