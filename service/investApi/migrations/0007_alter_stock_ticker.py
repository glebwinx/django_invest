# Generated by Django 5.0.1 on 2024-01-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investApi", "0006_alter_stock_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="ticker",
            field=models.TextField(max_length=5, unique=True, verbose_name="Тикер"),
        ),
    ]