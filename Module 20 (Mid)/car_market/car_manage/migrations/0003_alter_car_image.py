# Generated by Django 4.2.11 on 2024-04-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_manage', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car_manage/media/'),
        ),
    ]
