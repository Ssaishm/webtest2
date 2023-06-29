# Generated by Django 4.1.3 on 2023-06-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0003_discontact_message_discontact_personalname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discontact',
            name='message',
        ),
        migrations.AlterField(
            model_name='discontact',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='discontact',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
