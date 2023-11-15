# Generated by Django 4.2.7 on 2023-11-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Newsletter',
            },
        ),
    ]
