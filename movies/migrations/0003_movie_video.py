# Generated by Django 3.2.12 on 2022-07-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220721_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='videolar/'),
        ),
    ]
