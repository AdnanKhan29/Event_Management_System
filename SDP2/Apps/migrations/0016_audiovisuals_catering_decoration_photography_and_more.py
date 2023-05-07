# Generated by Django 4.1.5 on 2023-05-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0015_alter_admin_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioVisuals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('servicetype', models.CharField(max_length=30)),
                ('equipment', models.CharField(max_length=30)),
                ('avquantity', models.CharField(max_length=30)),
                ('techsupp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('servicetype', models.CharField(max_length=20)),
                ('cateringtype', models.CharField(max_length=50)),
                ('menuitems', models.CharField(max_length=50)),
                ('dietres', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('servicetype', models.CharField(max_length=30)),
                ('dedecoration', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('servicetype', models.CharField(max_length=20)),
                ('photographytype', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('delivery', models.CharField(max_length=50)),
                ('additional', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Videography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('servicetype', models.CharField(max_length=30)),
                ('vivideography', models.CharField(max_length=30)),
                ('viduration', models.CharField(max_length=30)),
                ('vistyle', models.CharField(max_length=30)),
                ('vilocation', models.CharField(max_length=30)),
                ('videlivery', models.CharField(max_length=30)),
                ('viadditional', models.CharField(max_length=30)),
            ],
        ),
    ]