from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='Store'),
    path('cart/', views.cart, name='Cart'),
    path('update_item/', views.updateItem, name='UpdateItem'),
    path('confirm/', views.confirm, name='Confirm'),
    path('viewproduct/<int:pk>', views.view_product, name='ViewProduct'),
    path('order_completed/', views.order_completed, name='OrderCompleted'),
]