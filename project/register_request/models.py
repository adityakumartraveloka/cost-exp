from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
# Create your models here.


class RegisterAccessRequest(models.Model):
    DESIGNATION = [
        ('Engineering Manager', 'Engineering Manager'),
        ('Team Lead', 'Team Lead')
    ]

    PRODUCT_DOMAIN = [
        ('and', 'and'),
        ('ath', 'ath'),
        ('cnm', 'cnm'),
        ('cnt', 'cnt'),
        ('cul', 'cul'),
    ]

    email = models.EmailField(blank=True)
    designation = models.CharField(max_length=200, blank=True, choices=DESIGNATION)
    product_domains = MultiSelectField(blank=True, choices=PRODUCT_DOMAIN)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.email)



'''
        'and',
        'ath',
        'cnm',
        'cnt',
        'cul',
        'cxp',
        'hcn',
        'ios',
        'loc',
        'lpc',
        'mch',
        'msg',
        'rec',
        'srs',
        'tda',
        'trp',
        'ugc',
        'usr',
        'vcp',
        'web',
        'xpe',
        'xpi',
        'xps',
        'xxt'
'''