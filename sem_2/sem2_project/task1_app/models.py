from django.db import models


# Create your models here.
class CoinFlip(models.Model):
    # HEADS = 'H'
    # TAILS = 'T'
    # FLIP_CHANCES = [
    #     (HEADS, 'Heads'),
    #     (TAILS, 'Tails'),
    # ]

    FLIP_CHANCES = [
        ('H', 'Heads'),
        ('T', 'Tails'),
    ]

    result = models.CharField(max_length=1, choices=FLIP_CHANCES)
    flip_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_n_flips_stats(n: int):
        flips = CoinFlip.objects.order_by('-flip_time')[:n]
        stats = {'heads': 0, 'tails': 0}
        for flip in flips:
            if flip.result == 'H':
                stats['heads'] += 1
            else:
                stats['tails'] += 1
        return stats


    def __str__(self):
        return f'{self.result} flipped at {self.flip_time}.'




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


