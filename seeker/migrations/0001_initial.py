# Generated by Django 4.1 on 2022-09-16 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('superuser', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0001_initial'),
        ('recruiter', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_profile', to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, to='superuser.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField(blank=True)),
                ('score', models.CharField(max_length=150)),
                ('desc', models.TextField(blank=True, max_length=2500)),
                ('mode', models.CharField(blank=True, choices=[('regular', 'Regular'), ('part_time', 'Part_time'), ('remote', 'Remote')], default='regular', max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='education.educationspecialisation')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seeker.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('shortlisted', 'Shortlisted'), ('interview', 'Interview'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='applied', max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.jobpost')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_profile', to='seeker.seekerprofile')),
            ],
        ),
    ]
