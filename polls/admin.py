from django.contrib import admin
from django.contrib.admin import ModelAdmin


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'question_text', 'pub_year')
    list_display_links = ('id', 'question_text')
    list_per_page = 20
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    actions = ('cleanup_text',)

    fieldsets = [
        ("General", {"fields":['id', 'question_text'], "description": "General question info"}),
        ("Other", {"fields": ["pub_date"]})
    ]

    readonly_fields = ('id', )

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(question_text="")

# Register your models here.
from polls.models import Answer, Poll, Question
admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)


