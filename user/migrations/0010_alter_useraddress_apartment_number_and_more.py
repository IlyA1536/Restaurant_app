# Generated by Django 5.1 on 2024-08-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_useraddress_apartment_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='entrance_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='floor_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
