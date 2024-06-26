# Generated by Django 5.0.6 on 2024-06-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_avatar_alter_customuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/default.jpg', upload_to='user-avatars/'),
        ),
    ]
