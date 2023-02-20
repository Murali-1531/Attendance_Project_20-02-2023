# Generated by Django 4.1.2 on 2023-02-20 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_Log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PG_Students_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Markers_ID', models.CharField(max_length=100)),
                ('Student_Name', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('HR_1', models.CharField(max_length=10)),
                ('HR_2', models.CharField(max_length=10)),
                ('HR_3', models.CharField(max_length=10)),
                ('HR_4', models.CharField(max_length=10)),
                ('HR_5', models.CharField(max_length=10)),
                ('Student_Regno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance_Log.student_details_ug', to_field='Regno')),
            ],
            options={
                'db_table': 'PG_Students_Attendance',
            },
        ),
    ]
