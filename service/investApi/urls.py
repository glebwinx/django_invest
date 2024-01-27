from django.urls import path
from .views import StockSerializerCreate, StockSerializerList, StockSerializerListDetail

urlpatterns = [
    path('api/v1/stock/create/', StockSerializerCreate.as_view(), name='api-create-stock'),
    path('api/v1/stock/list/', StockSerializerList.as_view(), name='api-list-stock'),
    path('api/v1/stock/list/<str:ticker>/', StockSerializerListDetail.as_view(), name='api-pk-stock'),

]
