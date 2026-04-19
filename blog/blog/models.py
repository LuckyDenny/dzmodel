from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Назва")
    slug = models.SlugField(max_length=120, unique=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name = "Тег")
    slug = models.SlugField(max_length=120, unique=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name = "Заголовок")
    content = models.TextField(verbose_name = "Опис")
    slug = models.SlugField(max_length=120, unique=True)
    published_date = models.DateTimeField(auto_created=True, verbose_name = "Дата публікаціїї")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Автор")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name = "Тег")
    image = models.URLField(default='https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600nw-1037719192.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    comment = models.TextField(verbose_name="Коментар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Коментарій'
        verbose_name_plural = 'Коментарії'

