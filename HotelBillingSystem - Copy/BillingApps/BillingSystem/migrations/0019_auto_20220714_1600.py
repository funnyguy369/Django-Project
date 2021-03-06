# Generated by Django 3.2.7 on 2022-07-14 10:30

from django.db import migrations, models
import djangocustom.models.fields
import djangocustom.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('BillingSystem', '0018_auto_20220714_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='goods_tax_id',
            field=djangocustom.models.fields.GSTField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, validators=[djangocustom.models.validators.NonZeroValidator()], verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='item_quantity',
            field=models.DecimalField(decimal_places=2, max_digits=20, validators=[djangocustom.models.validators.NonZeroValidator()], verbose_name='Quantity'),
        ),
    ]
