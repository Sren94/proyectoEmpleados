# Generated by Django 5.0.1 on 2024-01-08 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dep', '0003_alter_dep_options_alter_dep_unique_together_and_more'),
        ('emp', '0004_empleado_skill'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Employee',
        ),
    ]