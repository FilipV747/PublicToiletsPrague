# Generated by Django 4.2.2 on 2023-09-14 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.CharField(max_length=100)),
                ('schedule', models.ManyToManyField(to='prague.timeschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('toilet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prague.toilet')),
            ],
        ),
    ]
