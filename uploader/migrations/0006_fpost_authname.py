# Generated by Django 3.2.5 on 2021-07-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_alter_fpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpost',
            name='authname',
            field=models.CharField(max_length=500, null=True),
        ),
    ]