from django.urls import path
from .views import user_register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
