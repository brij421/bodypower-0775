# Generated by Django 2.0.3 on 2018-03-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20180314_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
