# Generated by Django 3.0.6 on 2020-06-05 14:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 5, 14, 5, 29, 566613, tzinfo=utc)),
        ),
    ]
