# Generated by Django 4.0.6 on 2022-08-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_card', '0003_stripetransaction_credential_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripetransaction',
            name='currency',
            field=models.CharField(max_length=255, null=-1),
            preserve_default=-1,
        ),
        migrations.AddField(
            model_name='stripetransaction',
            name='customer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stripetransaction',
            name='transaction_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]