# Generated by Django 4.2.14 on 2024-08-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0117_remove_facetteselectionwidget_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="session",
            name="display_mode",
        ),
    ]
