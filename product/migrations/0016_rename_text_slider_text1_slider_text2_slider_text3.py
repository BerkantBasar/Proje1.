# Generated by Django 4.1.2 on 2022-12-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_slider_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='text',
            new_name='text1',
        ),
        migrations.AddField(
            model_name='slider',
            name='text2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='text3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
