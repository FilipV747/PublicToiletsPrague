# Generated by Django 4.2.2 on 2023-10-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prague', '0004_alter_toilet_address_alter_toilet_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]