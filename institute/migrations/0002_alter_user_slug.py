# Generated by Django 4.2.11 on 2024-03-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, max_length=55, null=True),
        ),
    ]
