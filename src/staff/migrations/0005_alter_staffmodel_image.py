# Generated by Django 4.1.7 on 2023-04-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0004_alter_staffmodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffmodel",
            name="image",
            field=models.ImageField(
                default="grm_logo.jpg", upload_to="profile_pictures"
            ),
        ),
    ]