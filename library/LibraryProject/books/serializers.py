from rest_framework import serializers
from .models import Book
class BookSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','Title','Author','Year','Genre']