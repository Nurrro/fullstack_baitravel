# Generated by Django 5.0.1 on 2024-02-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_tours_total_people_zayavka_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='uploads_carusel')),
                ('title', models.CharField(max_length=65)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]
