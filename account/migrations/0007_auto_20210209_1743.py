# Generated by Django 3.1.4 on 2021-02-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210209_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, choices=[('PLUMBER', 'Plumber'), ('ELECTRICIAN', 'Electrician'), ('CARPENTER', 'Carpenter'), ('AC REPAIRER', 'AC repairer'), ('FASHION DESIGNER', 'Fashion designer'), ('HAIR STYLIST', 'Hair stylist'), ('BRICKLAYER', 'Bricklayer')], max_length=150),
        ),
    ]
