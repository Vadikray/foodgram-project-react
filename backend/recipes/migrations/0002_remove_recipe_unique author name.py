# Generated by Django 3.2 on 2023-03-16 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='recipe',
            name='unique author name',
        ),
    ]