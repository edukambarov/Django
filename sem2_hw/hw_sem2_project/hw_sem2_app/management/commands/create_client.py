from django.core.management.base import BaseCommand
from hw_sem2_app.models import Client


class Command(BaseCommand):
    help = "Create client"


    def handle(self, *args, **kwargs):
        client = Client(
            client_name="John Doe",
            email="johndoe@pochta.ru",
            phone="+79009000000",
            address="Petropavloskaaya Krepost 1",
        )
        client.save()
        self.stdout.write(f'Client {client.client_name} added.')