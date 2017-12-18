#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.forms import ModelForm
from library.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']

