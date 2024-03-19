from django.db import models


# Create your models here.

class Author(models.Model):
    name_author = models.CharField(verbose_name='Автор курса', max_length=30)


class Product(models.Model):
    products = models.CharField(
        verbose_name='Наименование курса',
        max_length=30
        )


class Start_Product(models.Model):
    date_is_start = models.DateField(verbose_name='Дата начала курса')


class Price_Product(models.Model):
    price_is_learn = models.IntegerField(verbose_name='Стоимость курса')


class Lesson_Common(models.Model):
    name_lesson = models.CharField(
        verbose_name='Наименование урока',
        max_length=30
        )
    link_lesson = models.TextField(verbose_name='Ссылка на урок')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    is_paid = models.BooleanField('Поле оплаты', default=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    start_product = models.ForeignKey(
        Start_Product,
        on_delete=models.SET_NULL,
        null=True
        )
    price_product = models.ForeignKey(
        Price_Product,
        on_delete=models.SET_NULL,
        null=True
        )
