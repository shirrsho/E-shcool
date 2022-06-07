# Generated by Django 4.0.3 on 2022-05-06 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gradesApp', '0008_rename_branch_student_semester_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('body', models.TextField()),
                ('due', models.DateTimeField()),
                ('question', models.FileField(upload_to='assignments/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gradesApp.student')),
            ],
        ),
    ]
