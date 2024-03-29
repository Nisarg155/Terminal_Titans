# Generated by Django 5.0.2 on 2024-02-24 09:02

import hospital.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_user_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to=hospital.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='hospital_details',
            name='hospital_img',
            field=models.ImageField(upload_to=hospital.models.user_directory_path),
        ),
    ]
