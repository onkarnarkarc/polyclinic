# Generated by Django 3.2 on 2023-12-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poly_app', '0005_alter_appointment_type_of_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='not_available',
            field=models.BooleanField(default=False),
        ),
    ]
