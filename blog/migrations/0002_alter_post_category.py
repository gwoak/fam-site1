# Generated by Django 3.2.9 on 2021-11-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategorised', max_length=255),
        ),
    ]
