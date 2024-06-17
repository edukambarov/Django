from django.core.management.base import BaseCommand
from task1_app.models import Author


class Command(BaseCommand):
    help = "Create author"


    def handle(self, *args, **kwargs):
        author = Author(
            first_name="Jane",
            last_name="Doe",
            bio="Legendary John Doe",
            birthday="1988-02-02",
            email="janedoe@pochta.ru",
        )
        author.save()
        self.stdout.write(f'Author "{author.full_name()}" added.')