# Generated by Django 4.0.4 on 2022-09-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0027_ledgers_vouchers_subgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledgers_vouchers',
            name='ledger',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
