# Generated by Django 4.2.4 on 2023-09-12 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_voucher_voucher_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventvoucher",
            name="redeemed_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="voucher_redeemer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
