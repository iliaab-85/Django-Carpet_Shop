# Generated by Django 4.2.6 on 2024-06-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_chats_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order',
            name='Product_Count',
            field=models.IntegerField(default=1, verbose_name='تعداد محصول'),
        ),
    ]
