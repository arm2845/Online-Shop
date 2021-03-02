from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='LogIn'),
    path('logout/', auth_views.LogoutView.as_view(), name='LogOut'),
    path('create/', views.create, name='CreateUser'),
    path('profile/', views.profile_page, name='ProfilePage'),
    path('update/', views.profile_update, name='ProfileUpdate'),
]