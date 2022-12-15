from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='название категории')
    color = models.CharField(max_length=100,
                             choices=[('btn-primary', 'Синий'), ('btn-secondary', 'Серый'), ('btn-success', 'Зеленный'),
                                      ('btn-danger', 'Красный'), ('btn-warning', 'Жёлтый'), ('btn-info', 'Голубой'),
                                      ('btn-light', 'Белый'), ('btn-dark', 'Чёрный')], blank=True, null=True)

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
    category = models.ManyToManyField(Category, through='Kit', through_fields=('test', 'category'))
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


class Kit(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Question(models.Model):
    description = models.TextField(verbose_name='Вопрос')
    test_id = models.ForeignKey('Test', verbose_name='Тест', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.test_id, self.description)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['test_id']


class Answer(models.Model):
    title = models.CharField(max_length=300, verbose_name='Ответ')
    question_id = models.ForeignKey(Question, to_field='id', related_name='answers', verbose_name='Вопрос',
                                    on_delete=models.CASCADE)
    right_false = models.BooleanField('Верный или отрицательный ответ')

    def __str__(self):
        return "{} {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['question_id']
