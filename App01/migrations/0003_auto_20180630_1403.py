# Generated by Django 2.0.6 on 2018-06-30 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App01', '0002_auto_20180630_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gander',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='App01.gander'),
            preserve_default=False,
        ),
    ]
