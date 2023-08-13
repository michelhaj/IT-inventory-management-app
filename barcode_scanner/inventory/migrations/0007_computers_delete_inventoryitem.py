# Generated by Django 4.2 on 2023-04-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0006_inventoryitem_delete_scannedbarcode"),
    ]

    operations = [
        migrations.CreateModel(
            name="Computers",
            fields=[
                (
                    "asset_tag",
                    models.CharField(
                        max_length=255, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "service_tag",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("department", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "computer_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("user", models.CharField(blank=True, max_length=255, null=True)),
                ("make", models.CharField(blank=True, max_length=255, null=True)),
                ("model", models.CharField(blank=True, max_length=255, null=True)),
                ("storage", models.CharField(blank=True, max_length=255, null=True)),
                ("cpu", models.CharField(blank=True, max_length=255, null=True)),
                ("ram", models.CharField(blank=True, max_length=255, null=True)),
                ("printer", models.BooleanField(max_length=3)),
                ("docking_station", models.BooleanField(max_length=3)),
                ("monitors", models.BooleanField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name="InventoryItem",
        ),
    ]