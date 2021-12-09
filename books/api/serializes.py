from rest_framework import serializers
from books.models import Books


class BookSerializers(serializers.ModelSerializers):
    class Meta:
        model = Books
        fields = "__all__"
