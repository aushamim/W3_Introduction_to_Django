# Generated by Django 4.2.11 on 2024-03-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basicFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('address', models.TextField()),
                ('course', models.CharField(max_length=100)),
                ('extra_course', models.CharField(max_length=100)),
                ('agree', models.BooleanField()),
            ],
        ),
    ]