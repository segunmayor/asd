# Generated by Django 4.2.2 on 2023-07-21 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontendview', '0007_alter_patient_guardian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='guardian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.guardian'),
        ),
    ]
