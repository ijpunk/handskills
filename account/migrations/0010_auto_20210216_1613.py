# Generated by Django 3.1.4 on 2021-02-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210209_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='users/'),
        ),
    ]
