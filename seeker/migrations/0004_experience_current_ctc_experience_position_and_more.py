# Generated by Django 4.1 on 2022-10-03 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
        ('recruiter', '0004_remove_jobpost_salary_package_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seeker', '0003_alter_seekerprofile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='current_ctc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='position',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='job_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='recruiter.jobpost'),
        ),
        migrations.AlterField(
            model_name='application',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='seeker.seekerprofile'),
        ),
        migrations.AlterField(
            model_name='education',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.educationspecialisation'),
        ),
        migrations.AlterField(
            model_name='education',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='seeker.seekerprofile'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='seeker.seekerprofile'),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
