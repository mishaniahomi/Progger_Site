# Generated by Django 3.2.16 on 2022-11-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('difficulty', models.FloatField()),
                ('timer', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
