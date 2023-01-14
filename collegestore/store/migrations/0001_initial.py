# Generated by Django 4.1.5 on 2023-01-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('purpose', models.CharField(max_length=250)),
                ('materials', models.CharField(max_length=500)),
            ],
        ),
    ]
