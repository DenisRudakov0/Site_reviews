# Generated by Django 3.2.9 on 2021-12-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0023_auto_20211201_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]