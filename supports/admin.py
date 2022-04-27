from django.contrib import admin
from supports.models import Faq, Inquiry, Answer


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'answer', 'writer',
                    'created_at', 'last_modified_at', 'last_modified_writter')

    # list_editable = ('question', 'answer',)


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 3
    min_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변들'


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone_number', 'content',
                    'image', 'writter', 'created_at', 'last_modified_at', 'last_modified_writter')
    inlines = [AnswerInline]
    readonly_fields = ('created_at', 'last_modified_at')
