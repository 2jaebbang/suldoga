# Generated by Django 4.0.6 on 2022-08-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('eng_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='cocktail/')),
                ('alcohol', models.CharField(max_length=20)),
                ('taste', models.CharField(max_length=20)),
                ('base', models.CharField(max_length=20)),
                ('match_food', models.CharField(max_length=20)),
            ],
        ),
    ]
