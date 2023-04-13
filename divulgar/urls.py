from django.urls import path
from . import views

urlpatterns = [
    path('novo_pet/', views.new_pet, name="novo-pet"),
    path('seus_pets/', views.seus_pets, name="seus_pets"),
    path('remover_pets/<int:id>', views.remover_pets, name='remover_pets'),
    path('ver_pet/<int:id>', views.ver_pet, name='ver_pet'),
    path('ver_pedido_adocao/', views.ver_pedido_adocao, name="ver_pedido_adocao"),
]
