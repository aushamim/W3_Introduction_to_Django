# Generated by Django 4.2.11 on 2024-03-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
