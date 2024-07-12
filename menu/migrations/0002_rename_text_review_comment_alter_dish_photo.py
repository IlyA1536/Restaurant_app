# Generated by Django 5.0.6 on 2024-07-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(blank=True, upload_to='dishes/'),
        ),
    ]
