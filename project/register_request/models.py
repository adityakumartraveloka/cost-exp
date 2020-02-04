from django.db import models
from datetime import datetime
# Create your models here.


class ProductDomain(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class RegisterAccessRequest(models.Model):
    DESIGNATION = [
        ('Engineering Manager', 'Engineering Manager'),
        ('Team Lead', 'Team Lead')
    ]

    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=200, choices=DESIGNATION)
    product_domains = models.ManyToManyField(ProductDomain)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.email)


class AuthorisedUser(models.Model):
    email = models.EmailField(unique=True)
    product_domains = models.ManyToManyField(ProductDomain)
    status = models.BooleanField(default=False)


class RequestHistory(models.Model):
    email = models.EmailField()
    product_domains = models.ManyToManyField(ProductDomain)
    approved_date = models.DateTimeField(auto_now_add=True)