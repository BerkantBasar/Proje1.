# Generated by Django 4.1.2 on 2022-11-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_setting_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='pinterest',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
