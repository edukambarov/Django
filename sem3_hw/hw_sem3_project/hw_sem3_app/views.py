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


def sort_orders_of_the_client_by_date_and_distinct_products(request, client_id: int, days: int):
    client = Client.objects.filter(id=client_id).first()
    sales_ = []
    orders_ = Order.objects.filter(
        order_client_id=client_id,
        order_date__gte=find_date_for_filter(days))
    good_set = set()
    for order in list(orders_):
        order_items = list(order.order_items.all())
        for good in order_items:
            if good not in good_set:
                sale = {'Товар': good.good_name,
                        'Номер заказа': order.id,
                        'Дата заказа': order.order_date}
                sales_.append(sale)
            good_set.add(good)
    sales = sorted(sales_, key=lambda x: x['Дата заказа'], reverse=True)
    context = {'title': f'{days} sales report',
               'sales': sales,
               'days': days,
               'client': client.client_name}
    return render(request,'hw_sem3_app/shop_sales_report.html', context=context)





