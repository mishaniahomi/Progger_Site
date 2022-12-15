# Generated by Django 3.2.16 on 2022-12-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testforuser', '0009_alter_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(blank=True, choices=[('btn-primary', 'Синий'), ('btn-secondary', 'Серый'), ('btn-success', 'Зеленный'), ('btn-danger', 'Красный'), ('btn-warning', 'Жёлтый'), ('btn-info', 'Голубой'), ('btn-light', 'Белый'), ('btn-dark', 'Чёрный')], max_length=100, null=True),
        ),
    ]
