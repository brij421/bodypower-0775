# Generated by Django 5.1.3 on 2024-11-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_alter_generatereports_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatereports',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
