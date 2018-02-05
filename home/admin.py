# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book

from hvad.admin import TranslatableAdmin
from django.shortcuts import redirect, reverse


class BookAdmin(TranslatableAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        lang = request.GET.get('language')
        url = reverse('admin:home_book_change', args=(obj.id,)) + '?language={lang}'.format(lang=lang)
        return redirect(url)

admin.site.register(Book, BookAdmin)
