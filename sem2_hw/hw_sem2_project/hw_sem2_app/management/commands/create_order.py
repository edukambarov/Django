from django.core.management.base import BaseCommand
from django.db.models import Sum, F, DecimalField
from hw_sem2_app.models import Good, Order, Client


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        g1 = Good.objects.filter(pk=1).first()
        g2 = Good.objects.filter(pk=2).first()
        order = Order.objects.create(order_client=Client.objects.filter(pk=1).first())
        order.order_items.add(g1)
        order.order_total += g1.get_good_total()
        order.order_items.add(g2)
        order.order_total += g2.get_good_total()
        order.save()
        self.stdout.write(f'Order added.')





