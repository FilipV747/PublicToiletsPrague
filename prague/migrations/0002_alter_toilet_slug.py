# Generated by Django 4.2.2 on 2023-09-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prague', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toilet',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
