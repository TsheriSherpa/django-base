# Generated by Django 4.0.6 on 2022-08-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khalti', '0004_khaltitransaction_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khaltitransaction',
            name='transaction_status',
            field=models.CharField(choices=[('INITIATED', 'INITIATED'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('FAILED', 'FAILED')], max_length=255),
        ),
    ]
