# Generated by Django 5.1.3 on 2024-11-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.PositiveIntegerField()),
                ('glucose', models.PositiveIntegerField()),
                ('blood_pressure', models.PositiveIntegerField()),
                ('skin_thickness', models.PositiveIntegerField()),
                ('insulin', models.PositiveIntegerField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('age', models.PositiveIntegerField()),
                ('outcome', models.BooleanField()),
            ],
        ),
    ]
