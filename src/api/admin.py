from django.contrib import admin

# Register your models here.
from .models import SimpsonQuote, BrBadQuote


class SimpsonQuoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'character',
        'quote',
        'created',
    )
    list_display_links = (
        'id',
        'character',
        'quote',
        'created',
    )
    search_fields = ('character', 'quote')


class BrBadQuoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'quote_id',
        'author',
        'quote',
        'created',
    )
    list_display_links = (
        'id',
        'author',
        'quote',
        'created',
    )
    search_fields = ('character', 'quote')


admin.site.register(SimpsonQuote, SimpsonQuoteAdmin)
admin.site.register(BrBadQuote, BrBadQuoteAdmin)
