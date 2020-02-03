# Generated by Django 3.0.2 on 2020-02-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_request', '0002_registeraccessrequest_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='registeraccessrequest',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.RemoveField(
            model_name='registeraccessrequest',
            name='product_domains',
        ),
        migrations.AddField(
            model_name='registeraccessrequest',
            name='product_domains',
            field=models.ManyToManyField(to='register_request.ProductDomain'),
        ),
    ]
