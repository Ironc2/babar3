from rest_framework import serializers
from .models import *


class StatusSerializer(serializers.ModelSerializer):
    """
    Status's view is read-only anyway
    """
    class Meta:
        model = Status
        fields = ('pk', 'name', 'overdraft')


class ProductSerializer(serializers.ModelSerializer):
    """
    Product's view is read-only anyway
    """
    class Meta:
        model = Product
        fields = ('pk', 'name', 'price')


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer's view is read-only anyway
    """
    class Meta:
        model = Customer
        fields = ('pk', 'firstname', 'lastname', 'nickname', 'fullname', 'email', 'status', 'balance')


class PaymentSerializer(serializers.ModelSerializer):
    """
    Payment is not read-only: specify the fields which are
    """
    class Meta:
        model = Payment
        fields = ('pk', 'customer', 'money')
        read_only_fields = ('timestamp')


class PurchaseSerializer(serializers.ModelSerializer):
    """
    Purchase is not read-only: specify the fields which are
    """
    class Meta:
        model = Purchase
        fields = ('pk', 'customer', 'product')
        read_only_fields = ('timestamp')
