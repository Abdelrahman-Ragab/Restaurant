# Generated by Django 3.2.7 on 2021-09-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0006_dessert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=1000)),
            ],
        ),
    ]
