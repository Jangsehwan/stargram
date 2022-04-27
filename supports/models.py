from email.mime import image
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Faq(models.Model):

    CATEGORY_CHOICES = [
        ('일반', '일반'),
        ('계정', '계정'),
        ('기타', '기타'),
    ]

    question = models.TextField(verbose_name='질문')
    category = models.TextField(choices=CATEGORY_CHOICES, verbose_name='카테고리')
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True, auto_created=True, related_name='faq_creater')

    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    last_modified_at = models.DateTimeField(
        verbose_name='마지막 수정일', auto_now=True)
    last_modified_writter = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='faq_modifier', null=True, blank=True)


class Inquiry(models.Model):
    title = models.TextField(verbose_name='제목')
    email = models.EmailField(verbose_name='이메일')  # 체크박스로 수신유무결정
    phone_number = models.CharField(
        verbose_name='답변수신 폰번호', max_length=12)  # 체크박스로 수신유무결정
    content = models.TextField("문의 내용")
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    writter = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True, auto_created=True, related_name='inq_creater')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    last_modified_at = models.DateTimeField(
        verbose_name='마지막 수정일', auto_now=True)
    last_modified_writter = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='inq_modifier')


class Answer(models.Model):
    ref_inquiry = models.ForeignKey(to="Inquiry", on_delete=models.CASCADE)
    content = models.TextField(verbose_name='답변내용')
    writter = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True, auto_created=True, related_name='ans_creater')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    last_modified_at = models.DateTimeField(
        verbose_name='마지막 수정일', auto_now=True)
    last_modified_writter = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True, related_name='ans_modifier')
