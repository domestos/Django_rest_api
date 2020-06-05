# Generated by Django 2.1.4 on 2018-12-14 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20181214_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['position'], 'verbose_name': 'Positions', 'verbose_name_plural': 'Position'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='posit', to='employees.Position'),
        ),
    ]