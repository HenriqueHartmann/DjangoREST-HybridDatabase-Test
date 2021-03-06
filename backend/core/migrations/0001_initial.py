# Generated by Django 3.1.1 on 2020-09-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.JSONField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.CharField(max_length=19)),
            ],
        ),
    ]
