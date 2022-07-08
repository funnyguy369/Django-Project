# Generated by Django 3.2.7 on 2022-05-10 09:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillingSystem', '0015_alter_customer_industry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='goods_tax_id',
            field=models.CharField(blank=True, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="GST must be entered in the format: '22 AAAAA0000A 1 Z 5'.Up to 15 digits allowed.", regex='(3[0-7]|[1-2][0-9]|0[1-9])[A-Z]{3}[ABCEFGHJLPT]{1}[A-Z]{1}\\d{4}[A-Z]{1}\\d[Z]{1}[A-Z\\d]{1}')]),
        ),
    ]