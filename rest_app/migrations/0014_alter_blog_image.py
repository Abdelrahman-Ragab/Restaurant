# Generated by Django 3.2.7 on 2021-09-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0013_auto_20210913_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
