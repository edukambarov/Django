import datetime

from django import forms

from .models import Author


class RandomForm(forms.Form):
    EVENT_CHOICES = [('coinflip','Монета'),
                     ('random_num','Случайное число'),
                     ('dice','Игральные кости')]
    event_type = forms.ChoiceField(choices=EVENT_CHOICES, label='Выберите игру')
    attempts = forms.IntegerField(min_value=1, max_value=64, label='Введите количество попыток')


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}
    ))


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)
    publication_date = forms.DateField(initial=datetime.date.today,
                                       widget=forms.DateInput(
                                        attrs={'class': 'form-control', 'type': 'date'}
                                        ))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)
    is_published = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(
                                    attrs={'class': 'form-check-input'}
                                    ))
    views = forms.IntegerField(min_value=0)