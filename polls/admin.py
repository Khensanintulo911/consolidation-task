from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # or admin.StackedInline
    model = Choice
    extra = 3  # Number of empty choices to display

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
