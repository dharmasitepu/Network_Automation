# Generated by Django 3.2.9 on 2021-11-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_automation', '0002_alter_device_ssh_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ssh_port',
            field=models.IntegerField(default=22),
        ),
    ]
