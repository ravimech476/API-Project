# Generated by Django 4.1 on 2022-09-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_model',
            name='Is_Delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='oraganization_model',
            name='Is_Delete',
            field=models.BooleanField(default=False),
        ),
    ]
