# Generated by Django 4.2.1 on 2023-09-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0013_rename_hsn_recurring_bills_bill_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bills',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
