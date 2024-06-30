# Generated by Django 5.0.6 on 2024-06-30 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_department_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.department'),
        ),
        migrations.AddField(
            model_name='user',
            name='designation_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.designation'),
        ),
    ]