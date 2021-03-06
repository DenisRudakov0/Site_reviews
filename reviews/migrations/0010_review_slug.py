# Generated by Django 3.2.9 on 2021-11-29 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20211128_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique_for_date='publish'),
        ),
    ]
