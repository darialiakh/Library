# -*- coding: utf-8 -*-
from django.contrib import admin
from library.models import Genre, Book, Comments
# Register your models here.


class BookInline(admin.StackedInline):
    model = Comments
    extra = 0


class BookAdmin(admin.ModelAdmin):
    fields = ['book_title', 'book_image', 'book_author', 'book_year', 'book_genre', 'book_pages','book_lang', 'book_lang_origin', 'book_trans', 'book_publisher', 'book_publisher_city', 'book_description', 'book_text']
    exclude = ['book_like', 'book_dislike']
    list_display = ['book_title', 'book_author', 'book_genre', 'bit']
    inlines = [BookInline]
    list_filter = ['book_genre']
    search_fields = ['id', 'book_title', 'book_author', 'book_year', 'book_genre']


class GenreAdmin(admin.ModelAdmin):
    fields = ['genre']


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)