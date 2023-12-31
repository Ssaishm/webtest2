# Generated by Django 4.1.3 on 2023-06-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discontact',
            name='companyaddress',
            field=models.TextField(null=True, verbose_name='companyaddress'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companycity',
            field=models.CharField(max_length=255, null=True, verbose_name='companycity'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companyemail',
            field=models.EmailField(max_length=255, null=True, verbose_name='CompanyEmail'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companyname',
            field=models.CharField(max_length=255, null=True, verbose_name='companyname'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companystate',
            field=models.CharField(max_length=255, null=True, verbose_name='companystate'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companyurl',
            field=models.CharField(max_length=255, null=True, verbose_name='companyurl'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='companyzipcode',
            field=models.CharField(max_length=255, null=True, verbose_name='companyzipcode'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='personalemail',
            field=models.EmailField(max_length=255, null=True, verbose_name='personalEmail'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
