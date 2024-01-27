from django.db import models


class Stock(models.Model):
    title = models.TextField(
        max_length=20,
        verbose_name='Название',
        unique=True
    )
    ticker = models.TextField(
        max_length=5,
        verbose_name="Тикер",
        unique=True
    )
    price = models.DecimalField(
        max_digits=14,
        decimal_places=7,
        default=0,
        verbose_name="Цена"
    )
    price_change = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="Изменение День %"
    )
    capitalisation = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        verbose_name="Капитализация"
    )
    volume = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        default=0,
        verbose_name="Объём"
    )

    def __str__(self):
        return f'{self.title}'
