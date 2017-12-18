# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from library.forms import CommentForm
from library.models import Book, Comments, Genre
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'library/home.html', locals())


def list(request):
    books = Book.objects.all()
    all_title = "Все книги"
    context = {
        "books": books
    }
    return render(request, 'library/list.html', locals())


def genre_list(request, genre_id):
    books = Book.objects.filter(book_genre__id=genre_id)
    title = "Все книги/ "
    genre = get_object_or_404(Genre, id=genre_id)
    context = {
        "books": books,
    }
    return render(request, 'library/list.html', locals())


def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = Comments.objects.filter(comments_book=book_id)
    form_comment = CommentForm
    return render (request, 'library/book.html', {
        "book": book,
        "comments": comments,
        "form_comments": form_comment,
    })


def add_like(request, book_id):
    if book_id in request.COOKIES:
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
    else:
       book = get_object_or_404(Book, id=book_id)  # возвращает id статьи или 404.
       book.book_likes += 1 # Прибавляет единицу к article_likes
       book.save() # сохраняет
       return_path = request.META.get('HTTP_REFERER', '/')
       response = redirect(return_path)
       response.set_cookie (book_id, "test")
       return response # делает редирект на ту же страницу


def add_dislike(request, book_id):
    if book_id in request.COOKIES:
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
    else:
       book = get_object_or_404(Book, id=book_id)  # возвращает id статьи или 404.
       book.book_dislikes += 1  # Прибавляет единицу к article_likes
       book.save()  # сохраняет
       return_path = request.META.get('HTTP_REFERER', '/')
       response = redirect(return_path)
       response.set_cookie(book_id, "test")
       return response  # делает редирект на ту же страницу


def addcomment(request, book_id):
    if request.POST :
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.comments_author = request.user
            comment.comments_book = Book.objects.get(id=book_id)
            form.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            return response




