# Generated by Django 4.1.3 on 2023-06-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0002_alter_discontact_companyaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discontact',
            name='message',
            field=models.TextField(blank=True, default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='discontact',
            name='personalname',
            field=models.CharField(max_length=255, null=True, verbose_name='personalname'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='description',
            field=models.TextField(blank=True, default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='designation',
            field=models.CharField(max_length=255, null=True, verbose_name='designation'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='industry',
            field=models.CharField(max_length=255, null=True, verbose_name='industry'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='question',
            field=models.CharField(max_length=255, null=True, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='speciality',
            field=models.CharField(max_length=255, null=True, verbose_name='speciality'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='years',
            field=models.CharField(max_length=255, null=True, verbose_name='years'),
        ),
    ]
