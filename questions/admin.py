from django.contrib import admin

from .models import Question


class QuestionForm(admin.ModelAdmin):
    fieldsets = (
        ('Question Text', {
            'fields': ('first_line',)
        }),
        ('Additional Text', {
            'fields': ('last_line',),
            'classes': ('collapse',)
        }),
        ('Incorrect Answers', {
            'fields': ('first_choice', 'second_choice', 'third_choice')
        }),
        ('Correct Answer', {
            'fields': ('correct_choice',)
        }),
        ('Question Category', {
            'fields': ('category',)
        })
    )
    list_display = ('first_line', 'category')
    list_filter = ['category']
    search_fields = ['first_line']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('first_line', 'category')


admin.site.register(Question, QuestionForm)
