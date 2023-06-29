# Generated by Django 4.1.3 on 2023-06-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_home_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hblogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('blogs', models.TextField(max_length=255, null=True, verbose_name='News')),
            ],
            options={
                'verbose_name_plural': 'Hblogs',
            },
        ),
        migrations.AlterField(
            model_name='home',
            name='news',
            field=models.TextField(max_length=500, null=True, verbose_name='News'),
        ),
    ]
