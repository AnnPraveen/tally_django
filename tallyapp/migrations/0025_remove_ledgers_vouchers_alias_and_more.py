# Generated by Django 4.0.4 on 2022-09-02 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0024_alter_ledgers_vouchers_ledger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgers_vouchers',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='ledgers_vouchers',
            name='voucher_name',
        ),
    ]
