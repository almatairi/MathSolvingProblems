from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.viewUsers , name='view-users'),

    #path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
]