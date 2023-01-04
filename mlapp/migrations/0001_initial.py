# Generated by Django 3.2 on 2023-01-03 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30, verbose_name='名字')),
                ('first_name', models.CharField(max_length=30, verbose_name='名前')),
                ('limit_balance', models.IntegerField(default=100000, verbose_name='残高')),
                ('education', models.IntegerField(choices=[(1, 'graduate_school'), (2, 'university'), (3, 'high_school'), (4, 'other')], default=0, verbose_name='学歴')),
                ('marriage', models.IntegerField(choices=[(1, 'married'), (2, 'single'), (3, 'others')], default=0, verbose_name='結婚歴')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('result', models.IntegerField(blank=True, null=True)),
                ('proba', models.FloatField(default=0.0)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('registered_date', models.DateField(default=datetime.date(2023, 1, 3))),
            ],
        ),
    ]
