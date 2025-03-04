from django.db import models

from apps.common.models import BaseModel


class OrderStatus(models.TextChoices):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    DELIVERED = 'delivered'


class Order(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default=OrderStatus.PENDING, choices=OrderStatus.choices)

    class Meta:
        db_table = 'orders'


class Cart(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='carts')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='carts', null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'carts'
