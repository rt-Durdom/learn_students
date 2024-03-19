# Generated by Django 3.2.16 on 2024-03-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=30, verbose_name='Автор курса')),
            ],
        ),
        migrations.CreateModel(
            name='Price_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_is_learn', models.IntegerField(verbose_name='Стоимость курса')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(max_length=30, verbose_name='Наименование курса')),
            ],
        ),
        migrations.CreateModel(
            name='Start_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_is_start', models.DateField(verbose_name='Дата начала курса')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_student.author')),
                ('price_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_student.price_product')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_student.product')),
                ('start_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_student.start_product')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson_Common',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=30, verbose_name='Наименование урока')),
                ('link_lesson', models.TextField(verbose_name='Ссылка на урок')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_student.product')),
            ],
        ),
    ]
