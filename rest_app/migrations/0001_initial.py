# Generated by Django 3.2.7 on 2021-09-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=50, null=True)),
                ('hour', models.CharField(blank=True, choices=[('10:00', '10:00'), ('12:00', '12:00'), ('14:00', '14:00'), ('16:00', '16:00'), ('18:00', '18:00'), ('20:00', '20:00'), ('22:00', '22:00')], max_length=50, null=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('persons', models.CharField(blank=True, choices=[('1-Person', '1-Person'), ('2-Persons', '2-Persons'), ('3-Persons', '3-Persons'), ('4-Persons', '4-Persons'), ('5-Persons', '5-Persons'), ('6-Persons', '6-Persons'), ('7-Persons', '7-Persons')], max_length=50, null=True)),
            ],
        ),
    ]
