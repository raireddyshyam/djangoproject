# Generated by Django 4.2.6 on 2023-12-12 07:21

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
                ('stdno', models.IntegerField()),
                ('stdname', models.CharField(max_length=200)),
                ('stdmarks', models.FloatField()),
                ('stdresult', models.CharField(max_length=200)),
            ],
        ),
    ]
