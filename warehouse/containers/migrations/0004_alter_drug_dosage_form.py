# Generated by Django 4.1.7 on 2023-05-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "containers",
            "0003_alter_big_name_alter_cannula_name_alter_drug_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="drug",
            name="dosage_form",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Pills", "Pills"),
                    ("Nebulizer", "Nebulizer"),
                    ("Injection", "Injection"),
                    ("Ointment / Gel", "Ointment / Gel"),
                    ("Areosol", "Areosol"),
                    ("Rectal enema", "Rectal enema"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
