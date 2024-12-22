from django.contrib import admin
from django.urls import path
from multable import views

urlpatterns = [
     path('admin/', admin.site.urls), 
    # Categories
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # Items
    path('items/', views.item_list, name='item-list'),
    path('items/<int:pk>/', views.item_detail, name='item-detail'),

    # Orders
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
]