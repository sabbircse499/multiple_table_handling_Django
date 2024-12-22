from rest_framework import serializers
from .models import Category, Item, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested representation

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'category', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)  # Nested representation

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'email', 'items', 'total_price', 'created_at']
