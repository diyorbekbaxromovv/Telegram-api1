# Generated by Django 5.0.1 on 2024-03-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_type',
            field=models.CharField(choices=[('via_phone', 'via_phone'), ('via_email', 'via_email')], max_length=20),
        ),
        migrations.AlterField(
            model_name='usercodeverification',
            name='auth_type',
            field=models.CharField(choices=[('via_phone', 'via_phone'), ('via_email', 'via_email')], max_length=22),
        ),
    ]
