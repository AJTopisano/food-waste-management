# Generated by Django 3.2.5 on 2021-07-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0006_fpost_authname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpost',
            name='author',
        ),
    ]
