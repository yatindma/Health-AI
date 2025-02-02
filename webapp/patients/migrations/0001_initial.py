# Generated by Django 2.2.6 on 2020-03-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientuid', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateTimeField(verbose_name='date published')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('street1', models.CharField(max_length=200)),
                ('street2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
