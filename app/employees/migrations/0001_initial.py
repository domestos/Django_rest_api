# Generated by Django 2.1.4 on 2018-12-14 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Name')),
                ('first_work_day', models.DateField()),
                ('last_work_dat', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['first_work_day'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=80, unique=True, verbose_name='Position')),
            ],
            options={
                'verbose_name_plural': 'Локації',
                'verbose_name': 'Локація',
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='position_id', to='employees.Position'),
        ),
    ]
