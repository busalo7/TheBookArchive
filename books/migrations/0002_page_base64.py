# Generated by Django 2.0.4 on 2018-05-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='base64',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]