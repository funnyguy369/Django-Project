# Generated by Django 3.2.7 on 2022-07-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0006_clientsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsettings',
            name='theme',
            field=models.CharField(blank=True, choices=[('Theme1', 'Theme1'), ('Theme2', 'Theme2'), ('Theme3', 'Theme3'), ('Theme4', 'Theme4'), ('Theme5', 'Theme5')], max_length=100, null=True),
        ),
    ]
