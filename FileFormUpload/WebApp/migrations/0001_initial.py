# Generated by Django 4.2.6 on 2023-11-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stdno', models.IntegerField()),
                ('Stdname', models.CharField(max_length=100)),
                ('ProfPic', models.FileField(blank=True, null=True, upload_to='')),
                ('StdAdd', models.CharField(max_length=100)),
            ],
        ),
    ]