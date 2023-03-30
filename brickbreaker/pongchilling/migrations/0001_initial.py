# Generated by Django 4.1.5 on 2023-03-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('mdp', models.CharField(max_length=255, null=True)),
                ('currentscore', models.IntegerField()),
                ('topscore', models.IntegerField()),
                ('level', models.IntegerField()),
            ],
        ),
    ]