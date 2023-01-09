# Generated by Django 4.1.4 on 2023-01-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadFiles', '0007_delete_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=30)),
                ('link', models.URLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
    ]