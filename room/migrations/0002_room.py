# Generated by Django 4.2.7 on 2023-12-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('occupany', models.IntegerField()),
                ('availability', models.CharField(max_length=20)),
            ],
        ),
    ]