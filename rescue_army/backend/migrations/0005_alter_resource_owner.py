# Generated by Django 4.1a1 on 2022-06-03 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0004_remove_event_address_alter_resource_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="backend.staff",
            ),
        ),
    ]
