# Generated by Django 4.1.2 on 2022-12-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
