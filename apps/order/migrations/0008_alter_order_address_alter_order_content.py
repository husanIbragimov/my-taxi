# Generated by Django 5.1.6 on 2025-03-04 17:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
