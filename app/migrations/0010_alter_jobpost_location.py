# Generated by Django 4.1.7 on 2023-03-19 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobpost_type_alter_jobpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.location'),
        ),
    ]
