# Generated by Django 5.1.3 on 2024-11-12 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing'),
        ),
    ]