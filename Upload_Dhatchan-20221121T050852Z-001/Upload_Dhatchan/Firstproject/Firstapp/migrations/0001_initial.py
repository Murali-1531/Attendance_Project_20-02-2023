# Generated by Django 2.2.12 on 2022-10-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('ephone', models.IntegerField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
