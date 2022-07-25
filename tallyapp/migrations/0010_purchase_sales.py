# Generated by Django 4.0.4 on 2022-07-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0009_auto_20220708_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierinvoiceno', models.CharField(max_length=225)),
                ('partyAccntname', models.CharField(max_length=225)),
                ('currentbalance', models.CharField(max_length=225, null=True)),
                ('purchaseledger', models.CharField(max_length=225)),
                ('nameofitem', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partyAccntname', models.CharField(max_length=225)),
                ('currentbalance', models.CharField(max_length=225, null=True)),
                ('salesledger', models.CharField(max_length=225)),
                ('nameofitem', models.CharField(max_length=225)),
            ],
        ),
    ]
