# Generated by Django 4.2.1 on 2023-09-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0006_auto_20230906_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bills',
            name='recur_bills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]