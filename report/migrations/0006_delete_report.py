# Generated by Django 4.1.5 on 2023-01-28 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_remove_nursereport_doctor_nursereport_doctor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Report',
        ),
    ]
