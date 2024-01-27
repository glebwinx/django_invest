from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Stock

from .serializers import StockSerializer


# Create your views here.

# class StockRobotPrice(generics.GenericAPIView, mixins.UpdateModelMixin):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)


class StockSerializerCreate(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class StockSerializerList(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StockSerializerListDetail(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = Stock.objects.all()
        ticker = self.kwargs.get('ticker')
        if ticker is not None:
            queryset = queryset.filter(ticker=ticker)
        return queryset
