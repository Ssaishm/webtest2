# Generated by Django 4.1.3 on 2023-06-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_hblogs_blogs_alter_home_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='hblogs',
            name='author',
            field=models.CharField(default=' ', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='outlet',
            field=models.CharField(default=' ', max_length=100, null=True),
        ),
    ]