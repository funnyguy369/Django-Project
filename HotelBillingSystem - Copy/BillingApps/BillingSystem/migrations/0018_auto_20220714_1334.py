# Generated by Django 3.2.7 on 2022-07-14 08:04

from django.db import migrations, models
import django.db.models.deletion
import djangocustom.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BillingSystem', '0017_auto_20220713_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='goods_tax_id',
            field=djangocustom.models.fields.GSTField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='BillingSystem.customer', verbose_name='Customer ID'),
        ),
    ]
