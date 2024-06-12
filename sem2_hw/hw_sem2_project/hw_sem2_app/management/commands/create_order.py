from django.core.management.base import BaseCommand
from django.db.models import Sum, F, DecimalField
from hw_sem2_app.models import Good, Order, Client


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        # g1 = Good.objects.filter(pk=1).first()
        # g2 = Good.objects.filter(pk=2).first()
        # order = Order.objects.create(order_client=Client.objects.filter(pk=1).first())
        # order.order_items.add(g1)
        # order.order_total += g1.get_good_total()
        # order.order_items.add(g2)
        # order.order_total += g2.get_good_total()
        # order.save()
        # self.stdout.write(f'Order added.')

        # g3 = Good.objects.filter(pk=3).first()
        # g4 = Good.objects.filter(pk=4).first()
        # order = Order.objects.create(order_client=Client.objects.filter(pk=2).first())
        # order.order_items.add(g3)
        # order.order_total += g3.get_good_total()
        # order.order_items.add(g4)
        # order.order_total += g4.get_good_total()
        # order.save()
        # self.stdout.write(f'Order added.')

        g5 = Good.objects.filter(pk=5).first()
        g6 = Good.objects.filter(pk=6).first()
        order = Order.objects.create(order_client=Client.objects.filter(pk=3).first())
        order.order_items.add(g5)
        order.order_total += g5.get_good_total()
        order.order_items.add(g6)
        order.order_total += g6.get_good_total()
        order.save()
        self.stdout.write(f'Order added.')





