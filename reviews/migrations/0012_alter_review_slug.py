# Generated by Django 3.2.9 on 2021-11-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_alter_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200, verbose_name='название статьи'), max_length=250, unique_for_date='publish'),
        ),
    ]
