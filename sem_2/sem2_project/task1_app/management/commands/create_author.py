from django.core.management.base import BaseCommand
from task1_app.models import Author


class Command(BaseCommand):
    help = "Create author"


    def handle(self, *args, **kwargs):
        author = Author(
            first_name="John",
            last_name="Doe",
            bio="Legendary John Doe",
            birthday="1987-01-01",
            email="johndoe@pochta.ru",
        )
        author.save()
        self.stdout.write(f'Author "{author.full_name()}" added.')