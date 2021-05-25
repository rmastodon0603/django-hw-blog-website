from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    surname = models.CharField(max_length=100, null=False, blank=False, verbose_name="Фамилия")
    login = models.CharField(max_length=100, null=False, blank=False, verbose_name="Логин", unique=True)

    class Meta:
    	verbose_name = 'Автор'
    	verbose_name_plural = 'Авторы'

    def __str__(self):
    	return self.name + " " + self.surname

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    published = models.BooleanField(verbose_name='Опубликован')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
