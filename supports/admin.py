from ast import In
from django.contrib import admin
from .models import Inquiry, Answer, Faq


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'updated_by')
    list_filter = ('category',)
    search_fields = ('title',)


class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변들'


@admin.action(description='답변 완료 안내 발송')
def answer_complete(modeladmin, request, queryset):
    for query in queryset:
        if query.is_email:
            print(f'{query.created_by} = {query.is_email}')
        if query.is_phone:
            print(f'{query.created_by} = {query.is_phone}')


@admin.action(description='일괄 접수 처리')
def register_complete(modeladmin, request, queryset):
    queryset.update(status=Inquiry.STATUS_CHOICES[1][0])


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'category', 'created_at', 'created_by')
    list_filter = ('status', 'category',)
    search_fields = ('title', 'email', 'phone',
                     'user__username', 'user__phone', 'user__email',)
    inlines = [AnswerInline, ]
    actions = [answer_complete, register_complete]
