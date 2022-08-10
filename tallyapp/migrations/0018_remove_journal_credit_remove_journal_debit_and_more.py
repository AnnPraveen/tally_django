# Generated by Django 4.0.4 on 2022-08-09 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0017_journal_alter_purchase_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='debit',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='particularsby',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='particularsto',
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
    ]
