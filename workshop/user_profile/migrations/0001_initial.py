# Generated by Django 4.0.2 on 2022-02-11 19:12

import django.core.validators
from django.db import migrations, models
import workshop.helpers.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), workshop.helpers.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), workshop.helpers.validators.validate_only_letters])),
                ('picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do Not Show', 'Do Not Show')], max_length=11)),
            ],
        ),
    ]
