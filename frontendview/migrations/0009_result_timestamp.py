# Generated by Django 4.2.2 on 2023-07-31 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontendview', '0008_alter_patient_guardian'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
