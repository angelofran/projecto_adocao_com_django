from django.urls import path
from . import views

urlpatterns = [
    path('login/',  views.llogin, name='login'),
    path('register/', views.register, name='register'),
    path('sair/', views.sair, name="sair"),
]