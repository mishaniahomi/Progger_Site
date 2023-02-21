# Generated by Django 3.2.16 on 2022-12-13 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testforuser', '0004_auto_20221115_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='category',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='testforuser.question', verbose_name='Вопрос'),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testforuser.category')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testforuser.test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='many_category',
            field=models.ManyToManyField(through='testforuser.Kit', to='testforuser.Category'),
        ),
    ]