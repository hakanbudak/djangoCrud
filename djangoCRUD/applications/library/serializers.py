from rest_framework import serializers

from applications.library.models import Library


class CursorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name', 'stock')
