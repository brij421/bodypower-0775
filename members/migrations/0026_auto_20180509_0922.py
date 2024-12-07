# Generated by Django 2.0.3 on 2018-05-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0025_auto_20180502_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='subscription_type',
            field=models.CharField(choices=[('gym', 'Gym'), ('cross_fit', 'Cross Fit'), ('gym_and_cross_fit', 'Gym + Cross Fit'), ('pt', 'Personal Training')], default='gym', max_length=30),
        ),
    ]
