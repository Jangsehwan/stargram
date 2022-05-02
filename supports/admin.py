from django.contrib import admin
from supports.models import Inquiry, Answer, Faq


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_by')
    list_filter = ('category',)
    search_fields = ('title',)


class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변들'


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'created_by')
    list_filter = ('category',)
    search_fields = ('title', 'email', 'phone',)
    inlines = [AnswerInline]
