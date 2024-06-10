from django.core.management.base import BaseCommand
from hw_sem2_app.models import Good


class Command(BaseCommand):
    help = "Create good"
    def handle(self, *args, **kwargs):
        good = Good(
            good_name="Milk 1l",
            description="Milk 1l Piskarevskiy",
            price=65.50,
            quantity = 3,
        )
        # good = Good(
        #     good_name="White bread",
        #     description="White bread Fazer",
        #     price=50.00,
        #     quantity=3,
        # )
        good.save()
        self.stdout.write(f'Good "{good.good_name}" added.')

        def __str__(self):
            return f'{self.good_name}, price: {self.price}, quantity: {self.quantity}.'