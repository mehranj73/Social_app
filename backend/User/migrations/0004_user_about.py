# Generated by Django 3.0.4 on 2020-04-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20200407_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, max_length=300, verbose_name='about'),
        ),
    ]