# Generated by Django 4.2.1 on 2023-09-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0007_recurring_bills_recur_bills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurring_bills',
            name='recur_bills',
        ),
        migrations.AddField(
            model_name='recurring_bills',
            name='bills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]