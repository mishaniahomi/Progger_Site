# Generated by Django 3.2.16 on 2022-12-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testforuser', '0006_rename_many_category_test_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='count',
        ),
    ]
