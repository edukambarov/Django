from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop_main, name='main'),
    path('shop_sales_report/<int:client_id>/<int:days>',
         views.sort_orders_with_distinct_products,
         name='report')
]
