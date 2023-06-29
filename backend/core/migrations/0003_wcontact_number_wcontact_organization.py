# Generated by Django 4.1.3 on 2023-06-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_contact_wcontact_alter_wcontact_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='wcontact',
            name='number',
            field=models.CharField(max_length=10, null=True, verbose_name='number'),
        ),
        migrations.AddField(
            model_name='wcontact',
            name='organization',
            field=models.CharField(max_length=255, null=True, verbose_name='organization'),
        ),
    ]