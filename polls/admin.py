from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'question_text']
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
