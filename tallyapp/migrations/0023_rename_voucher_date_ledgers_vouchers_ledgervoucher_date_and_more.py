# Generated by Django 4.0.4 on 2022-09-02 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0022_ledgers_vouchers_subgroup_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledgers_vouchers',
            old_name='voucher_date',
            new_name='ledgervoucher_date',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='company',
        ),
    ]