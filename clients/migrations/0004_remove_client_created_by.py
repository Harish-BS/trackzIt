# Generated by Django 5.0.6 on 2024-06-26 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_remove_client_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_by',
        ),
    ]