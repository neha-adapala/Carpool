# Generated by Django 4.0.6 on 2022-07-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool_app', '0020_profile_user_alter_profile_id'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='membercar',
            constraint=models.UniqueConstraint(fields=('user_id', 'car_registration_number'), name='unique car registration number constraint'),
        ),
    ]
