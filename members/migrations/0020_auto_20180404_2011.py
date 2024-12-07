# Generated by Django 2.0.3 on 2018-04-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_member_fee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='batch',
            field=models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], default='morning', max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='subscription_period',
            field=models.CharField(choices=[('1', '1 Month'), ('3', '3 Months'), ('6', '6 Months'), ('12', '12 Months')], default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='subscription_type',
            field=models.CharField(choices=[('gym', 'Gym'), ('cross_fit', 'Cross Fit'), ('gym_and_cross_fit', 'Gym + Cross Fit')], default='gym', max_length=30),
        ),
    ]
