from django.core.management.base import BaseCommand
from hw_sem2_app.models import Client


class Command(BaseCommand):
    help = "Create client"


    def handle(self, *args, **kwargs):
        # client = Client(
        #     client_name="John Doe",
        #     email="johndoe@pochta.ru",
        #     phone="+79009000000",
        #     address="Petropavloskaaya Krepost 1",
        # )

        # client = Client(
        #     client_name="Jahn Doe",
        #     email="janedoe@pochta.ru",
        #     phone="+79009000001",
        #     address="Petropavloskaaya Krepost 2",
        # )

        client = Client(
            client_name="kotik",
            email="kotik@pochta.ru",
            phone="+79009000002",
            address="Kotiy Dom 1",
        )
        client.save()
        self.stdout.write(f'Client {client.client_name} added.')