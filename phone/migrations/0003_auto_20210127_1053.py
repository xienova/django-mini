# Generated by Django 2.2.3 on 2021-01-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='is_borrow',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
