# Generated by Django 5.0.1 on 2024-02-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_carusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='otzyv',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads/images/'),
        ),
    ]
