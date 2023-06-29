# Generated by Django 4.1.3 on 2023-06-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_hblogs_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hblogs',
            name='author',
            field=models.CharField(default='Pacify Medical Technologies ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hblogs',
            name='blogs',
            field=models.TextField(max_length=6000, null=True, verbose_name='Blogs'),
        ),
        migrations.AlterField(
            model_name='home',
            name='news',
            field=models.TextField(max_length=6000, null=True, verbose_name='News'),
        ),
    ]
