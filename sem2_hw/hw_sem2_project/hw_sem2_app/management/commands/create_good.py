from django.core.management.base import BaseCommand
from hw_sem2_app.models import Good


class Command(BaseCommand):
    help = "Create good"
    def handle(self, *args, **kwargs):
        good = Good(
            good_name="Banana 1kg",
            description="Banana from Vietnam",
            price=100.50,
            quantity = 2,
        )
        # good = Good(
        #     good_name="Mango 1 kg",
        #     description="Mango from Thailand",
        #     price=199.00,
        #     quantity=3,
        # )
        good.save()
        self.stdout.write(f'Good "{good.good_name}" added.')

        def __str__(self):
            return f'{self.good_name}, price: {self.price}, quantity: {self.quantity}.'