# Generated by Django 4.2.1 on 2023-09-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0017_rec_comments_recur_bills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rec_comments',
            name='customr',
        ),
    ]
