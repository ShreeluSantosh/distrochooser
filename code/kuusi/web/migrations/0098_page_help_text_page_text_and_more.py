# Generated by Django 4.2.4 on 2024-05-19 12:01

from django.db import migrations, models
import web.models.translateable


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0097_facetteselectionwidget_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="help_text",
            field=web.models.translateable.TranslateableField(
                blank=True,
                help_text="A comment for translators to identify this value",
                max_length=80,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="text",
            field=web.models.translateable.TranslateableField(
                blank=True,
                help_text="A comment for translators to identify this value",
                max_length=80,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="facetteselectionwidget",
            name="description",
            field=models.TextField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
