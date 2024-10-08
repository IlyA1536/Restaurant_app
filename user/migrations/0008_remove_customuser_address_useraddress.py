# Generated by Django 5.1 on 2024-08-15 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=63)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.IntegerField()),
                ('entrance_number', models.IntegerField(blank=True, null=True)),
                ('floor_number', models.IntegerField(blank=True, null=True)),
                ('apartment_number', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
