# Generated by Django 3.2.9 on 2021-12-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_review_prev_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='prev_text',
            field=models.TextField(default='', max_length=400, verbose_name='Превью текст'),
        ),
    ]