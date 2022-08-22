from dataclasses import fields
from rest_framework import serializers
from .models import SimpsonQuote, BrBadQuote


class SimpsonQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpsonQuote
        fields = '__all__'
        ordering = ['created']


class LastQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpsonQuote
        fields = ['id', 'quote', 'character']


class BrBaQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrBadQuote
        fields = '__all__'
        ordering = ['created']


class LastBrBaQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrBadQuote
        fields = ['id', 'quote', 'author']
