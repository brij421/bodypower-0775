# Generated by Django 5.1.3 on 2024-11-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
