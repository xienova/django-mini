# Generated by Django 2.2.3 on 2021-02-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_auto_20210204_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='creater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone', to='account.User', to_field='name'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone', to='phone.PhoneDep', to_field='name'),
        ),
    ]
