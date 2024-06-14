from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render
from .models import Client, Good, Order

# Create your views here.
def shop_main(request):
    context = {'title': 'main'}
    return render(request,'hw_sem3_app/shop_main.html', context=context)


def find_date_for_filter(days: int):
    end = datetime.today()
    delta_sec = days * 24 * 60 * 60
    return (end - timedelta(seconds=delta_sec)).date()


def sort_orders_with_distinct_products(request, client_id: int, days: int):
    orders_ = Order.objects.filter(
        order_client_id=client_id,
        order_date__gte=find_date_for_filter(days))

    client = Client.objects.filter(id=client_id).first()
    good_refs = [ref['order_items'] for ref in orders_.values('order_items')]

    goods = []
    for ref in good_refs:
        good = Good.objects.filter(id=ref).first()
        goods.append(good)
    goods_set = set(goods)
    sales = []
    print(goods_set)
    i = 0
    for good in list(goods_set):
        sale = {'Товар': good.good_name}
        if good.id in [ref['order_items'] for ref in orders_.values('order_items')]:
            for order in list(orders_):
                sale['Номер заказа'] = order.id
                sale['Дата заказа'] = order.order_date
        sales.append(sale)
    print(sales)
    context = {'title': f'{days} sales report',
               'sales': sales,
               'days': days,
               'client': client.client_name}
    return render(request,'hw_sem3_app/shop_sales_report.html', context=context)





