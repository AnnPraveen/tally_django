# Generated by Django 4.0.4 on 2022-08-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0018_remove_journal_credit_remove_journal_debit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sales',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
