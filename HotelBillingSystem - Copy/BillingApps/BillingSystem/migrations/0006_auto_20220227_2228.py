# Generated by Django 3.2.7 on 2022-02-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillingSystem', '0005_alter_customer_pending_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='item_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
