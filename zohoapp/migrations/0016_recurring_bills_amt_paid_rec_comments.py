# Generated by Django 4.2.1 on 2023-09-26 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0015_recurring_bills_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bills',
            name='amt_paid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='rec_comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('customr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
