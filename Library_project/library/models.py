# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

SHORT_DESCRIPTION_LEN = 120


class Genre(models.Model):
    class Meta():
        db_table = "genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    genre = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.genre


class Book(models.Model):
    class Meta():
        db_table = "book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    book_title = models.CharField(max_length=100, verbose_name='Название')
    book_image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')
    book_author = models.CharField(max_length=50, verbose_name='Автор')
    book_year = models.CharField(max_length=4, verbose_name='Год')
    book_genre = models.ForeignKey(Genre, verbose_name='Жанр')
    book_pages = models.CharField(blank=True, max_length=4, verbose_name='Количество страниц')
    book_lang = models.CharField(blank=True, max_length=20, verbose_name='Язык')
    book_lang_origin = models.CharField(blank=True, max_length=20, verbose_name='Язык оригинала')
    book_trans = models.CharField(blank=True, max_length=50, verbose_name='Переводчик(и)')
    book_publisher = models.CharField(blank=True, max_length=20, verbose_name='Издательство')
    book_publisher_city = models.CharField(blank=True, max_length=20, verbose_name='Город печати')
    book_description = models.TextField(verbose_name='Описание')
    book_text = models.FileField(blank=True, null=True, upload_to="text/", default="", verbose_name='Текст')
    book_likes = models.IntegerField(default=0, verbose_name='Понравилось')
    book_dislikes = models.IntegerField(default=0, verbose_name='Не понравилось')

    def __str__(self):
        return self.book_title

    def get_short_description(self):
        if len(self.book_description) > SHORT_DESCRIPTION_LEN:
            return self.book_description[:SHORT_DESCRIPTION_LEN]
        else:
            return self.book_description

    def bit(self):
        if self.book_image:
            return u'<img src="%s" width="70"/>' % self.book_image.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True


class Comments(models.Model):
    class Meta():
        db_table = "comments"
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_book = models.ForeignKey(Book)
    comments_author = models.ForeignKey(User, default=None, blank=True, null=True, verbose_name='Автор')
    comments_date = models.DateTimeField(auto_now_add=True, auto_now=False)





