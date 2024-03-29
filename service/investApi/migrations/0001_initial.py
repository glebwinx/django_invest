# Generated by Django 5.0.1 on 2024-01-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stoks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(max_length=20, verbose_name="Название")),
                ("ticker", models.TextField(max_length=5, verbose_name="Тикер")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=7, verbose_name="Цена"
                    ),
                ),
                (
                    "price_change",
                    models.DecimalField(
                        decimal_places=0,
                        default=0,
                        max_digits=5,
                        verbose_name="Изменение День %",
                    ),
                ),
                (
                    "capitalisation",
                    models.DecimalField(
                        decimal_places=0,
                        default=0,
                        max_digits=16,
                        verbose_name="Капитализация",
                    ),
                ),
                (
                    "volume",
                    models.DecimalField(
                        decimal_places=0, default=0, max_digits=16, verbose_name="Объём"
                    ),
                ),
            ],
        ),
    ]
