# Generated by Django 3.0.2 on 2020-02-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_request', '0008_auto_20200204_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoriseduser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
