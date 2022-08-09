# Generated by Django 4.0.6 on 2022-08-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_card', '0002_stripecredential_credential_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripetransaction',
            name='credential_type',
            field=models.CharField(
                choices=[('TEST', 'TEST'), ('LIVE', 'LIVE')], max_length=255, null=True),
        ),
    ]