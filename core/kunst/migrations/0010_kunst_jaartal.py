# Generated by Django 5.1.7 on 2025-06-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunst', '0009_kunst_formaat_kunst_materiaal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kunst',
            name='jaartal',
            field=models.IntegerField(default='2025', null=True),
        ),
    ]
