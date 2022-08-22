from tabnanny import verbose
from django.db import models

# Create your models here.

# https://thesimpsonsquoteapi.glitch.me/quotes
#
# [
#   {
#     "quote": "You're turning me into a criminal when all I want to be is a petty thug.",
#     "character": "Bart Simpson",
#     "image": "https://cdn.glitch.com/3c3ffadc-3406-4440-bb95-d40ec8fcde72%2FBartSimpson.png?1497567511638",
#     "characterDirection": "Right"
#   }
# ]


class SimpsonQuote(models.Model):
    quote = models.CharField(max_length=500)
    character = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    characterDirection = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.quote

    class Meta:
        verbose_name = 'Quotes from The Simpson'
        verbose_name_plural = 'Quotes from The  Simpson'
        ordering = ['created']


#   {
#     "quote_id": 92,
#     "quote": "There’s no honor among thieves… except for us of course",
#     "author": "Jimmy McGill",
#     "series": "Better Call Saul"
#   }


class BrBadQuote(models.Model):
    quote_id = models.IntegerField()
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    series = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.quote

    class Meta:
        verbose_name = 'Quotes from The Breaking Bad'
        verbose_name_plural = 'Quotes from The Breaking Bad'
        ordering = ['created']
