# Generated by Django 4.0.4 on 2022-09-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('mailing_name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journalledger', models.CharField(max_length=225, null=True)),
                ('journal_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ledgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger', models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierinvoiceno', models.CharField(default=True, max_length=225)),
                ('partyAccntname', models.CharField(default=True, max_length=225)),
                ('currentbalancep', models.CharField(max_length=225, null=True)),
                ('currentbalancepl', models.CharField(max_length=225, null=True)),
                ('purchaseledger', models.CharField(default=True, max_length=225)),
                ('nameofitem', models.CharField(max_length=225, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('purchase_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyAccntname', models.CharField(max_length=225)),
                ('currentbalancep', models.CharField(max_length=225, null=True)),
                ('salesledger', models.CharField(max_length=225)),
                ('currentbalancesl', models.IntegerField(null=True)),
                ('nameofitem', models.CharField(max_length=225, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField(default=0)),
                ('sales_date', models.DateField(null=True)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='SubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particularsby', models.CharField(max_length=225, null=True)),
                ('particularsto', models.CharField(max_length=225, null=True)),
                ('credit', models.IntegerField(default=0, null=True)),
                ('debit', models.IntegerField(default=0, null=True)),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='ledgers_vouchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledgervoucher_date', models.DateField(null=True)),
                ('credit', models.IntegerField(default=0)),
                ('debit', models.IntegerField(default=0)),
                ('closingbalance', models.IntegerField(default=0)),
                ('Group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.group')),
                ('SubGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.subgroup')),
                ('Voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.voucher')),
                ('ledgers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.ledgers')),
            ],
        ),
        migrations.AddField(
            model_name='ledgers',
            name='SubGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.subgroup'),
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_accounts', models.BooleanField(default=True)),
                ('bill_wise_entry', models.BooleanField(default=True)),
                ('cost_centres', models.BooleanField(default=False)),
                ('interest_calc', models.BooleanField(default=True)),
                ('maintain_inventory', models.BooleanField(default=True)),
                ('integrate_accounts', models.BooleanField(default=True)),
                ('multiple_price_level', models.BooleanField(default=True)),
                ('batches', models.BooleanField(default=True)),
                ('expirydate_batches', models.BooleanField(default=True)),
                ('joborder_processing', models.BooleanField(default=True)),
                ('sub_ledger', models.BooleanField(default=True)),
                ('cost_tracking', models.BooleanField(default=True)),
                ('job_costing', models.BooleanField(default=True)),
                ('discount_invoices', models.BooleanField(default=True)),
                ('Billed_Quantity', models.BooleanField(default=True)),
                ('gst', models.BooleanField(default=False)),
                ('tds', models.BooleanField(default=False)),
                ('tcs', models.BooleanField(default=False)),
                ('vat', models.BooleanField(default=False)),
                ('excise', models.BooleanField(default=True)),
                ('servicetax', models.BooleanField(default=True)),
                ('payroll', models.BooleanField(default=False)),
                ('multiple_addrss', models.BooleanField(default=True)),
                ('vouchers', models.BooleanField(default=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('currency_code', models.CharField(max_length=225)),
                ('decimal_places', models.CharField(max_length=225)),
                ('show_in_millions', models.BooleanField(default=False)),
                ('suffix_symbol', models.BooleanField(default=False)),
                ('symbol_and_amount', models.BooleanField(default=False)),
                ('after_decimal', models.CharField(max_length=225)),
                ('amount_in_words', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Costcentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225, null=True)),
                ('under', models.CharField(max_length=225)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
    ]
