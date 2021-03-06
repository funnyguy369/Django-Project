# Generated by Django 3.2.7 on 2022-05-03 12:17

import CustomUser.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0002_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Joined date in our office.'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='<ul><li>Your image size should be between 0.5 - 2MB</li><li>Please your a 2 x 2 image for between resolution.</li></ul>', upload_to='User profile images', validators=[CustomUser.validators.min_max_size]),
        ),
    ]
