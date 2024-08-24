# Generated by Django 5.1 on 2024-08-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_customuser_address_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='entrance_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='floor_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='house_number',
            field=models.CharField(max_length=10),
        ),
    ]
