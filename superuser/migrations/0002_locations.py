# Generated by Django 4.1 on 2022-10-04 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
