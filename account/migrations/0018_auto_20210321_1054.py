# Generated by Django 3.1.4 on 2021-03-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210321_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
