# Generated by Django 5.1 on 2025-02-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_customer_customerprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerprofile',
            name='confirm_password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
