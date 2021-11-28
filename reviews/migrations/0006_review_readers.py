# Generated by Django 3.2.9 on 2021-11-28 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0005_auto_20211128_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='readers',
            field=models.ManyToManyField(through='reviews.Raiting', to=settings.AUTH_USER_MODEL),
        ),
    ]
