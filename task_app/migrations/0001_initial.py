# Generated by Django 3.0.7 on 2020-07-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.TextField(blank=True, null=True)),
                ('end_date', models.TextField(blank=True, null=True)),
                ('user_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('real_name', models.TextField()),
                ('location', models.TextField()),
            ],
            options={
                'db_table': 'user_table',
                'managed': False,
            },
        ),
    ]
