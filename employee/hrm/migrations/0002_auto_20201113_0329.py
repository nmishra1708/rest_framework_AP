# Generated by Django 3.1.3 on 2020-11-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(max_length=30),
        ),
    ]
