# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class Book(TranslatableModel):
    release = models.DateTimeField()

    translations = TranslatedFields(
        title = models.CharField(max_length=250)
    )
