# Generated by Django 3.0.2 on 2020-01-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='add_time',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
