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


class Question(models.Model):
    description = models.TextField(verbose_name='Вопрос')
    test_id = models.ForeignKey('Test', verbose_name='Тест', on_delete= models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.test_id, self.description)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['test_id']

class Answer(models.Model):
    title = models.CharField(max_length=300, verbose_name='Ответ')
    question_id = models.ForeignKey(Question, related_name='answers', verbose_name='Вопрос', on_delete= models.CASCADE)
    right_false = models.BooleanField('Верный или отрицательный ответ')


    def __str__(self):
        return "{} {} {}".format(self.question_id, self.title, self.right_false)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['question_id']
