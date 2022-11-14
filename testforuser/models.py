from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='название категории')

    class Meta:
        verbose_name = 'категорию теста'
        verbose_name_plural = 'категории тестов'
        ordering = ['name']

    def __str__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=300, verbose_name='название теста')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(null=True, verbose_name='изображение')
    difficulty = models.FloatField(verbose_name='сложность')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='категория')
    timer = models.PositiveSmallIntegerField(verbose_name='время на решение теста')

    def get_str_id(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('testdetailview', kwargs={'test_id': self.pk})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['title']

    def __str__(self):
        return self.title




