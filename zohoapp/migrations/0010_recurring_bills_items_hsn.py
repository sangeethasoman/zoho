# Generated by Django 4.2.1 on 2023-09-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bills_items',
            name='hsn',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
