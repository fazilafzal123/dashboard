# Generated by Django 3.2.6 on 2021-10-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_profile', '0005_alter_profile_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
