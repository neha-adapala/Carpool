# Generated by Django 4.0.6 on 2022-07-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool_app', '0008_alter_membercar_class_id_alter_membercar_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='driving_license_valid_from',
            field=models.IntegerField(choices=[(2022, '2022'), (2021, '2021'), (2020, '2020'), (2019, '2019'), (2018, '2018'), (2017, '2017'), (2016, '2016'), (2015, '2015'), (2014, '2014'), (2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005')], null=True),
        ),
    ]
