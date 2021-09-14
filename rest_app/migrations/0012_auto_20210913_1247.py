# Generated by Django 3.2.7 on 2021-09-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0011_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='details',
        ),
        migrations.RemoveField(
            model_name='dessert',
            name='price',
        ),
        migrations.AlterField(
            model_name='break',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]