from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='Store'),
    path('cart/', views.cart, name='Cart'),
    path('update_item/', views.updateItem, name='UpdateItem'),
]