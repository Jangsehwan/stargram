# Generated by Django 4.0.3 on 2022-04-28 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tkinter.tix


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', '일반'), ('2', '계정'), ('3', '기타')], default='3', max_length=2, verbose_name='카테고리')),
                ('title', models.CharField(max_length=80, verbose_name='질문 제목')),
                ('email', models.EmailField(blank=tkinter.tix.Tree, max_length=254, verbose_name='이메일')),
                ('is_email', models.BooleanField(default=False, verbose_name='이메일 수신 여부')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='문자메세지')),
                ('is_phone', models.BooleanField(default=False, verbose_name='문자메세지 수신여부')),
                ('content', models.TextField(verbose_name='문의 내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일시')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, null=True, verbose_name='질문 제목')),
                ('content', models.TextField(verbose_name='질문 내용')),
                ('category', models.TextField(choices=[('1', '일반'), ('2', '계정'), ('3', '기타')], max_length=2, verbose_name='카테고리')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='답변내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종수정일시')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_created_by', to=settings.AUTH_USER_MODEL)),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supports.inquiry')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
