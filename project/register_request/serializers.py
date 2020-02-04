from rest_framework import serializers
from .models import RegisterAccessRequest, ProductDomain, AuthorisedUser, RequestHistory


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
        # print('[serializers.py]',validated_data)
        product_domains_data = validated_data.pop('product_domains')
        request_access = RegisterAccessRequest.objects.create(**validated_data)

        for product_domain in product_domains_data:
            product_domain, created = ProductDomain.objects.get_or_create(name=product_domain['name'])
            request_access.product_domains.add(product_domain)
        return request_access


    def update(self, instance, validated_data):
        product_domains_data = validated_data.pop('product_domains')
        instance.email =  validated_data.get('email', instance.email)
        instance.designation = validated_data.get('designation', instance.designation)

        product_domain_list = []

        for product_domain in product_domains_data:
            product_domain, created = ProductDomain.objects.get_or_create(name=product_domain['name'])
            product_domain_list.append(product_domain)
        
        # print(product_domain_list)

        # Can not assign directly, either use set or destructuring
        instance.product_domains.set(product_domain_list)
        instance.save()
        return instance
        

    def __str__(self):
        return self.email


class AuthorisedUserSerializer(serializers.ModelSerializer):
    product_domains = ProductDomainSerializer(many=True)
    class Meta:
        model = AuthorisedUser
        fields = (
            'id',
            'email',
            'status',
            'product_domains'
        )


    def create(self, validated_data):
        product_domains_data = validated_data.pop('product_domains')
        auth_user = AuthorisedUser.objects.create(**validated_data)

        for product_domain in product_domains_data:
            product_domain, created = ProductDomain.objects.get_or_create(name=product_domain['name'])
            auth_user.product_domains.add(product_domain)

        return auth_user


    def update(self, instance, validated_data):
        product_domains_data = validated_data.pop('product_domains')
        instance.email = validated_data.get('email', instance.email)

        product_domain_list = []

        for product_domain in product_domains_data:
            product_domain, created = ProductDomain.objects.get_or_create(name=product_domain['name'])
            product_domain_list.append(product_domain)

        instance.product_domains.set(product_domain_list)
        instance.save()
        return instance


class RequestHistorySerializer(serializers.ModelSerializer):
    product_domains = ProductDomainSerializer(many=True)

    class Meta:
        model = RequestHistory
        fields = (
            'id',
            'email',
            'product_domains',
            'approved_date'
        )

    def create(self, validated_data):
        product_domains_data = validated_data.pop('product_domains')
        request_history = RequestHistory.objects.create(**validated_data)

        for product_domain in product_domains_data:
            product_domain, created = ProductDomain.objects.get_or_create(name=product_domain['name'])
            request_history.product_domains.add(product_domain)

        return request_history
