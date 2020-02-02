from rest_framework import serializers
from .models import ProductDomainIndex

class ProductDomainIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDomainIndex
        fields = '__all__'

    def __str__(self):
        return self.name