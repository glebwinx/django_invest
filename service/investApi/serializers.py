from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            "title",
            "ticker",
            "price",
            "price_change",
            "capitalisation",
            "volume"
        )

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)
