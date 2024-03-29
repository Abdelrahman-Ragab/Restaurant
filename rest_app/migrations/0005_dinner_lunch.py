# Generated by Django 3.2.7 on 2021-09-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0004_break'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=1000)),
            ],
        ),
    ]
