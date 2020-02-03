from rest_framework import serializers
from .models import RegisterAccessRequest, ProductDomain


class ProductDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDomain
        fields = (
            'id',
            'name'
        )


class RegisterAccessRequestSerializer(serializers.ModelSerializer):
    product_domains = ProductDomainSerializer(many=True)
    class Meta:
        model = RegisterAccessRequest
        fields = (
            'id',
            'email',
            'designation',
            'date_created',
            'product_domains'
        )
    
    def create(self, validated_data):
        print('[serializers.py]',validated_data)
        product_domains = validated_data.pop('product_domains')
        request_access = RegisterAccessRequest.objects.create(**validated_data)

        for name in product_domains:
            print(name)
        return request_access

    def __str__(self):
        return self.email