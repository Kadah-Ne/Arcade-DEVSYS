# Generated by Django 4.1.5 on 2023-03-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pongchilling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currentscore',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='topscore',
            field=models.IntegerField(null=True),
        ),
    ]
