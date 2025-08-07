from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # or admin.StackedInline
    """
    Inline admin descriptor for Choice model.

    Attributes:
        model (Model): The model class to use for inline editing.
        extra (int): Number of extra empty forms to display.
    """
    model = Choice
    extra = 3  # Number of empty choices to display

class QuestionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Question model.

    Attributes:
        fieldsets (list): Fieldsets for organizing fields in the admin form.
        inlines (list): Inline models to display within the Question admin page.
    """
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
