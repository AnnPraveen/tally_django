# Generated by Django 4.0.4 on 2022-07-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0012_rename_currentbalance_sales_currentbalancep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='nameofitem',
            field=models.CharField(max_length=225, null=True),
        ),
    ]