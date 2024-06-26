# Generated by Django 4.2.7 on 2023-11-24 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostal_grievance', '0002_alter_studentquery_branch_alter_studentquery_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('no_of_rooms', models.IntegerField()),
                ('no_of_students', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_name', models.CharField(max_length=13)),
                ('mess_fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('room_fees', models.IntegerField()),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostel_room', to='hostal_grievance.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=30)),
                ('student_branch', models.CharField(max_length=30)),
                ('student_phone', models.IntegerField()),
                ('student_age', models.IntegerField()),
                ('address_area', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=40)),
                ('address_state', models.CharField(max_length=40)),
                ('medical_status', models.CharField(max_length=300)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostel_students', to='hostal_grievance.hostel')),
                ('mess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mess_students', to='hostal_grievance.mess')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_students', to='hostal_grievance.room')),
            ],
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_time', models.DateTimeField()),
                ('in_time', models.DateTimeField()),
                ('visitor_phone', models.IntegerField()),
                ('visitor_name', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_visitors', to='hostal_grievance.student')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=30)),
                ('staff_duty', models.CharField(max_length=30)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostel_staff', to='hostal_grievance.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('father_phone', models.IntegerField()),
                ('mother_phone', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parents', to='hostal_grievance.student')),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_status', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_fees', to='hostal_grievance.student')),
            ],
        ),
    ]
