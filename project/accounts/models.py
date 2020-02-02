from django.db import models

# Create your models here.

class ProductDomainIndex(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    product_domain = models.CharField(max_length=200, unique=True, null=True, blank=True)
    business_unit = models.CharField(max_length=200, null=True, blank=True)
    eng_manager = models.EmailField(max_length=200, null=True, blank=True)
    team_lead = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name