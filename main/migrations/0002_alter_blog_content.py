# Generated by Django 4.1.5 on 2023-01-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(help_text='Enter you blog text here.', max_length=2000),
        ),
    ]
