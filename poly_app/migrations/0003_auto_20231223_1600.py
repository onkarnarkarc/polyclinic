# Generated by Django 3.2 on 2023-12-23 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poly_app', '0002_auto_20231223_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='day_of_appointment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poly_app.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='type_of_visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poly_app.visittype'),
        ),
    ]
