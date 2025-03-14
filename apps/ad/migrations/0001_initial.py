# Generated by Django 5.1.6 on 2025-02-26 12:10

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='ads/')),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
                'db_table': 'ads',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AdImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads/')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ad.ad')),
            ],
            options={
                'verbose_name': 'Ad Image',
                'db_table': 'ad_images',
                'verbose_name_plural': 'Ad Images',
                'ordering': ['id'],
            },
        ),
    ]
