# Generated by Django 4.2.7 on 2024-02-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_alter_donor_donorimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donorimage',
            field=models.FileField(blank=True, null=True, upload_to='Donor-image'),
        ),
    ]
