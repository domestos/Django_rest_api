# Generated by Django 2.1.4 on 2018-12-16 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20181216_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
