# Generated by Django 5.0.3 on 2024-04-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_accessrecords'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='email',
            field=models.EmailField(default='mini@gmail.com', max_length=254),
        ),
    ]
