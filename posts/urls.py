from django.urls import path

from . import views

urlpatterns = [
    # this is the main index of the website
    path('', views.index,name='index'),
]
