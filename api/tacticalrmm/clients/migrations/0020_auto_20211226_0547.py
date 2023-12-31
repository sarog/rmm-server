# Generated by Django 3.2.10 on 2021-12-26 05:47

import clients.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_remove_deployment_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='agent_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='failing_checks',
            field=models.JSONField(default=clients.models._default_failing_checks_data),
        ),
        migrations.AddField(
            model_name='site',
            name='agent_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='site',
            name='failing_checks',
            field=models.JSONField(default=clients.models._default_failing_checks_data),
        ),
    ]
