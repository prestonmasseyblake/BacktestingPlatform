from django.urls import path

from . import views

urlpatterns = [
    path('join/', views.join, name='join'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('favorites/',views.favorites, name='favorites')
]