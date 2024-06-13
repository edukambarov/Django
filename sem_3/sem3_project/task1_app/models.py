from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()


    def full_name(self):
        return f'{self.first_name} {self.last_name}'



class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)



    def __str__(self):
        return f'"{self.title}" by author: {self.author}'

    def get_summary(self):
        words = self.text.split()
        return f'{" ".join(words[:6])}...'

