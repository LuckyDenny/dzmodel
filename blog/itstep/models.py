from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100, verbose_name= "ім'я")
    last_name = models.CharField(max_length=100, verbose_name= "прізвище")
    email = models.EmailField()
    phone = models.IntegerField(verbose_name= "телефон")
    date_of_birth = models.DateField(verbose_name= "дата народження")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= "Користувач")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Вчитель"
        verbose_name_plural = "Вчителі"

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Назва")
    description = models.TextField(verbose_name= "Опис")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name= "Викладачь")
    start = models.DateField(verbose_name= "Початок курсу")
    end = models.DateField(verbose_name= "Закынчення курсу")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name= "ім'я")
    last_name = models.CharField(max_length=100, verbose_name= "прізвище")
    email = models.EmailField()
    phone = models.IntegerField(verbose_name= "телефон")
    url = models.URLField(blank=True, null=True)
    date_of_birth = models.DateField(verbose_name= "дата народження")
    courses = models.ManyToManyField(Course, verbose_name= "Курси")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"