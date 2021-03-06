# Generated by Django 3.0.2 on 2020-02-01 20:36

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterAccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('designation', models.CharField(blank=True, choices=[('Engineering Manager', 'Engineering Manager'), ('Team Lead', 'Team Lead')], max_length=200)),
                ('product_domains', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('and', 'and'), ('ath', 'ath'), ('cnm', 'cnm'), ('cnt', 'cnt'), ('cul', 'cul')], max_length=19)),
            ],
        ),
    ]
