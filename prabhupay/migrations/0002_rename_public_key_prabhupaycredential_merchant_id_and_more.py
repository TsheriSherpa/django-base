# Generated by Django 4.0.6 on 2022-08-19 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prabhupay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prabhupaycredential',
            old_name='public_key',
            new_name='merchant_id',
        ),
        migrations.RenameField(
            model_name='prabhupaycredential',
            old_name='secret_key',
            new_name='merchant_password',
        ),
    ]
