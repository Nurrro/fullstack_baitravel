# Generated by Django 5.0.1 on 2024-02-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_alter_phototours_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='price_of_tour',
            field=models.IntegerField(),
        ),
    ]
