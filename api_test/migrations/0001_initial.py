# Generated by Django 3.0.2 on 2020-01-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_created=True)),
                ('book_name', models.CharField(max_length=128)),
            ],
        ),
    ]
