# Generated by Django 5.0 on 2024-04-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_student_teacher_rename_name_admin_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='password', max_length=50),
        ),
    ]
