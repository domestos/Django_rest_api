# Generated by Django 2.1.4 on 2018-12-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20181214_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='employees.Position'),
        ),
    ]
