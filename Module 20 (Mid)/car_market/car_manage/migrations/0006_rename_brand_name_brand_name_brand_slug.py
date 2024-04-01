# Generated by Django 4.2.11 on 2024-04-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_manage', '0005_alter_car_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]