# Generated by Django 4.1.5 on 2023-05-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='usertype',
            field=models.TextField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]