from ckeditor.fields import RichTextField
from django.db import models

from apps.common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    district = models.ForeignKey('common.District', on_delete=models.CASCADE, related_name='products')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    class Meta:
        db_table = 'product_images'

    def __str__(self):
        return self.product.name
