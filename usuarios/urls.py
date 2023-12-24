from django.urls import path
from usuarios.views import login, logout, register, login_2

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('login_2', login_2, name='login_2'),
]