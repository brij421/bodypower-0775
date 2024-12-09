# Generated by Django 2.0.3 on 2018-04-27 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_member_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='amount',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='batch',
            field=models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening'), ('', 'All')], default='morning', max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(default=datetime.datetime(2018, 4, 27, 19, 13, 14, 138615)),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
