# Generated by Django 4.0.4 on 2022-07-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0010_purchase_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='sales_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='nameofitem',
            field=models.CharField(default=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='partyAccntname',
            field=models.CharField(default=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchaseledger',
            field=models.CharField(default=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='supplierinvoiceno',
            field=models.CharField(default=True, max_length=225),
        ),
    ]
