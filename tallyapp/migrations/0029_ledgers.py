# Generated by Django 4.0.4 on 2022-09-03 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0028_ledgers_vouchers_ledger'),
    ]

    operations = [
        migrations.CreateModel(
            name='ledgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger', models.CharField(max_length=225, null=True)),
                ('SubGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.subgroup')),
            ],
        ),
    ]
