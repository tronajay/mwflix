# Generated by Django 2.2.24 on 2021-11-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
        ('movies', '0003_auto_20211013_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='platform',
            field=models.ManyToManyField(default=1, to='stream.Stream'),
        ),
    ]