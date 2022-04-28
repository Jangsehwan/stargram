from django.contrib import admin
from supports.models import Inquiry, Answer, Faq


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'created_by',
                    'updated_by', 'created_at', 'updated_at')

    # list_editable = ('question', 'answer',)


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 3
    min_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변들'


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone',
                    'content', 'image', 'created_at', 'updated_at')
    inlines = [AnswerInline]
    # readonly_fields = ('created_at', 'updated_at')
