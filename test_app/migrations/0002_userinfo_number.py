# Generated by Django 4.1.3 on 2022-12-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='number',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
