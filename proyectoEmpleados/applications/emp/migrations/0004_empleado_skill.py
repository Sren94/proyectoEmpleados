# Generated by Django 5.0.1 on 2024-01-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_skills_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='skill',
            field=models.ManyToManyField(to='emp.skills'),
        ),
    ]
