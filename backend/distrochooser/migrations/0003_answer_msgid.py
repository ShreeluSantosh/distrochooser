# Generated by Django 2.1.2 on 2019-02-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0002_question_msgid'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='msgid',
            field=models.CharField(default='new-value', max_length=100),
        ),
    ]
