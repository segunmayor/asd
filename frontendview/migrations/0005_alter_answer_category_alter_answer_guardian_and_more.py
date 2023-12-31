# Generated by Django 4.2.2 on 2023-07-14 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontendview', '0004_patient_category_alter_answer_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.category'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='guardian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.guardian'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='patient',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.patient'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.question'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.category'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='guardian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.guardian'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.category'),
        ),
        migrations.AlterField(
            model_name='result',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.category'),
        ),
        migrations.AlterField(
            model_name='result',
            name='guardian',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.guardian'),
        ),
        migrations.AlterField(
            model_name='result',
            name='patient',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontendview.patient'),
        ),
    ]
