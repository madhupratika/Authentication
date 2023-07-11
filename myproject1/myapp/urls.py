
from django.urls import path
from myapp import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('hello/', views.hello, name='hello'),
]
