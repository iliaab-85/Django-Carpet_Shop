# Generated by Django 4.2.6 on 2024-06-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_product_order_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='Visit_Seller',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='chats',
            name='Visit_Support',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='chats',
            name='Visit_User',
            field=models.IntegerField(default='0'),
        ),
    ]
