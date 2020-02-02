from rest_framework import serializers
from .models import RegisterAccessRequest

class RegisterAccessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterAccessRequest
        fields = ( 
            'id',
            'email', 
            'designation', 
            'product_domains',
            'date_created',
        )

    def __str__(self):
        return self.email